"""
The Many Body System contains the Object-class of a collection of all bodies. 
This Object enables the interaction between the single Objects.
"""

import os
import numpy as np
import data_readout as data_readout
from One_Body import Atom 
import Forces
import Integration_Schemes 

# maybe needed in __init__: , file_path1:str, mass_pos, name_pos, file_path2:str=None, pos_pos, vel_pos
class Many_Body_System(object):
    def __init__(self:object) -> None:
        """
        The System calss object contains all necessary variables of all objects
        """
        self.heavy_objects = []  # here a list of all the objects are stored; NOT IN USE!
        #self.path = os.path.abspath(os.path.dirname(__file__))
        self.obj_names = []   # names of the objects
        self.all_mass = []  # has all the mass variables of all objects
        self.number_of_obj:int = None  
        self.all_current_position = []
        self.all_current_velocity = []
        self.all_current_acc = []
        self.all_ever_position = []
        self.all_ever_velocity = []
        self.all_ever_acc = []
        #self.simulation_result_file_for_ovito = data_readout.Creat_New_File()
        pass
    
    def Update_Movement(self, time_step:float=1,integration_method:str="Velocity Verlet") -> None:
        """
        Moves all objects of the system one timestep further
        """
        if integration_method == "Velocity Verlet": 
            self.Movement_by_Velocity_Verlet(time_step)
        elif integration_method == "Verlet":
            self.Movement_by_Verlet(time_step)
        elif integration_method == "Euler":
            self.Movement_by_Euler(time_step)
        pass

    def Movement_by_Verlet(self, time_step:float) -> None:
        """
        Updates velocity and position of one time-stepp using the Verlet algorithm.
        The first time stepp needs to be done with Euler or Velocity Verlet
        """
        self.Force_Matrixs(time_step)
        if len(self.all_ever_position) == 0:  # checking if former position is available; 
                self.Movement_by_Velocity_Verlet(time_step)
        else:
            next_pos_list = []
            next_vel_list = []
            for i in range(self.number_of_obj):  # I Noticed now: Maybe with arrays the formloop can be avoided... I hunch, I dont know yet
                next_pos,next_vel = Integration_Schemes.Verlet_Algorithem(
                    time_step, np.array(self.all_current_position[i]), np.array(self.all_current_velocity[i]), self.all_ever_position[-2][i]
                )
                next_pos_list.append(next_pos)
                next_vel_list.append(next_vel)
            self.all_current_position = next_pos_list
            self.all_current_velocity = next_vel_list
            self.all_ever_position.append(next_pos_list)
            self.all_ever_velocity.append(next_vel_list)
        pass

    def Movement_by_Velocity_Verlet(self, time_step) -> None:
        """
        Determines acc andu Updates velocity and postion 
        from timestepp n -> n+1 with Velocity Verlet
        """
        if len(self.all_ever_acc) < len(self.all_current_position):  # force matrix only needs to be calculated for 1. timestepp
            self.Force_Matrix()      #Appends acceleration of n    
            pass
        # determening position update
        next_pos = []
        for i in range(self.number_of_obj):    
            next_pos.append(Integration_Schemes.Velocity_Verlet_posAlgorithem(time_step,
                np.array(self.all_current_position[i]), np.array(self.all_current_velocity[i]), self.all_current_acc[i] 
                ))
        # updating position variables
        self.all_current_position = next_pos
        self.all_ever_position.append(self.all_current_position)
        self.Force_Matrix()  # Appends acceleration timestepp of n+1
        # determening velocity update
        next_vel = []
        for i in range(self.number_of_obj): 
            next_vel.append(Integration_Schemes.Velocity_Verlet_velAlgorithem(
                time_step, np.array(self.all_current_velocity[i]), self.all_ever_acc[-2][i], self.all_ever_acc[-1][i]
                ))
        # updating velocity variables
        self.all_current_velocity=next_vel
        self.all_current_velocity.append(next_vel)
        pass

    def Movement_by_Euler(self, time_step) -> None:
        """
        Updates position velocity and acceleration vectors with the Euler integration methode
        """
        next_pos_list = []
        next_vel_list = []
        self.Force_Matrixs()
        for i in range(len(self.number_of_obj)):
            next_vel , next_pos = Integration_Schemes.Euler_Algorithm(
                time_step, np.array(self.all_current_position[i]), np.array(self.all_current_velocity[i]), self.all_current_acc[i]
            )
            next_pos_list.append(next_pos)
            next_vel_list.append(next_vel)
        # Updating all variable lists
        self.all_current_position=next_pos_list
        self.all_current_velocity=next_vel_list
        self.all_ever_position.append(next_pos_list)
        self.all_ever_velocity.append(next_vel_list)
        pass

    def Force_Matrix(self) -> None:
        """
        Calculates all interactions between all bodies of System resulting in a nxn-Matrix.
        F_ij is a vector (np.array)! F_ij: "j is pulling i"
        dumps acceleration values into acc. lists (at least of two time stepps needs to be saved).
        Probably not the most efficiant way... Found it: Sum_ij(F_ij*mass_vec)=acc_i, along those lines...
        """
        Force_matrix = []  # force matrix of F = [[F_11,F12,..],[F_21,F_22,..]]
        for i in range(self.number_of_obj):
            one_obj_Force = []  # row i of matrix; list of all forces acting on object i
            for j in range(i,self.number_of_obj):
                if j == i:  # here the property of F_ij = -F_ji, F_ii=0 is used via if statements
                    one_obj_Force.append(0)
                    pass
                elif j > i:  # F_ij 
                    one_obj_Force.append(
                    np.array(Forces.Gravitational_force(
                        np.array(self.all_current_position[i]),np.array(self.all_current_position[j]), 
                        self.all_mass[i],self.all_mass[j])))
                elif j<i:  # F_ij = -F_ij
                    one_obj_Force.append(-Force_matrix[i][j])
            Force_matrix.append(one_obj_Force)
            self.all_current_acc.append(sum(one_obj_Force)/self.all_mass[i]) 
        self.all_ever_acc.append(self.all_current_acc)
        pass
                
    def Initialize_System(self, data_path:str) -> None:
        """
        Identifies all the inital conditions of the many body system;
        -reading the data from external file 
        -allocating an obj for all given initial conditions in the data file 
        """
        init_variables , names = data_readout.Read_File_pos_vel_mass(data_path)
        self.obj_names = names
        self.number_of_obj = len(names)
        for i in range(self.number_of_obj):
            obj_info = init_variables[i]  
            pos = obj_info[0]  
            vel = obj_info[1]
            mass = obj_info[2]
            self.all_current_position.append(pos)
            self.all_current_velocity.append(vel)
            self.all_mass.append(mass)
            self.Initializing_Object(pos ,vel, mass, self.obj_names[i])
        self.all_ever_position.append(self.all_current_position)
        self.all_ever_velocity.append(self.all_current_velocity)
        pass

    def Initializing_Object(self, position, velocity, mass, name) -> None:
        """
        Initializes the object of a single body - will not be used!
        """
        one_body = Atom(position, velocity, mass, name)
        self.heavy_objects.append(one_body)
        pass
    
    

# here I can test my progress
if __name__ == "__main__":

    pass

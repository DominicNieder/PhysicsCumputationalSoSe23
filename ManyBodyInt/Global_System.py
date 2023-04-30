"""
The Many Body System contains the Object-class of a collection of all bodies. 
This Object enables the interaction between the single Objects.
"""
from numba import njit
import sys
import numpy as np
import data_readout as data_readout
from One_Body import Physical_Obj 
import Forces

# maybe needed in __init__: , file_path1:str, mass_pos, name_pos, file_path2:str=None, pos_pos, vel_pos
class Many_Body_System(object):
    def __init__(self:object) -> None:
        """
        The time stepp of the System pertubation needs to be given
        The list of all the objects can be found here and carries all variables for all objects.
        """
        self.heavy_objects = []  # here a list of all the objects are stored
        self.obj_names = []   # names of the objects
        self.all_mass = []  # has all the mass variables of all objects
        self.number_of_obj:int = None
        self.all_current_position = []
        self.all_current_velocity = []
        self.all_position = []
        self.all_velocity = []
        pass
    
    def Movement(self):
        """
        Moves all objects of the system one time-stepp further
        """
        force_matrix = self.Force_Matrix()
        for i in range(self.number_of_obj):
            total_force = sum(force_matrix[i])
            total_acc = total_force/self.all_mass[i]  
            self.all_position.append(self.all_current_position[i])

        pass

    @njit
    def Force_Matrix(self):
        """
        Calculates all interactions between all bodies of System resulting in a nxn-Matrix.
        F_ij is a vector (np.array)! 
        """
        all_obj_Force = []  # force matrix of F = [[F_11,F12,..],[F_21,F_22,..]]
        for i in range(self.number_of_obj):
            one_obj_Force = []  # list of all forces acting on object i
            for j in range(i,self.number_of_obj):
                if j == i:  # here the property of F_ij = -F_ji, F_ii=0 is used via if statements
                    one_obj_Force.append(0)
                    pass
                elif j > i:  # F_ij 
                    one_obj_Force.append(
                    np.array(Forces.Gravitational_force(
                        self.all_current_position[i],self.all_current_position[j], 
                        self.all_mass[i],self.all_mass[j])))
                elif j<i:  # F_ji = -F_ij
                    one_obj_Force.append(-all_obj_Force[i][j])
        return(all_obj_Force)
                

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
            obj_info = init_variables[i]  # [position, velocity, mass]
            pos = np.array(obj_info[0])  # want to handle pos, vel as np.array
            vel = np.array(obj_info[1])
            mass = obj_info[2]
            self.all_current_position.append(pos)
            self.all_current_velocity.append(vel)
            self.all_mass.append(mass)
            self.Initializing_Body(pos ,vel, mass, self.obj_names[i])
        pass


    def Initializing_Object(self, position, velocity, mass, name) -> None:
        """
        Initializes the object of a single body 
        """
        one_body = Physical_Obj.Atom(position, velocity, mass, name)
        self.heavy_objects.append(one_body)
        pass


# here I can test my progress
if __name__ == "__main__":
    pass

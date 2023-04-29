"""
The Many Body System is the Object of a collection of all bodies. This Object enables the interaction 
between the single Objects.
"""
import sys

import data_readout as data_readout
from One_Body import Physical_Obj 
# maybe needed in __init__: , file_path1:str, mass_pos, name_pos, file_path2:str=None, pos_pos, vel_pos
class Many_Body_System():
    def __init__(self:object) -> None:
        """
        The list of all the objects can be found here
        """
        self.heavy_objects = []  # here a list of all the objects are stored
        self.obj_names = []   # names of the objects
        self.all_current_position = []
        self.all_current_velocity = []
        pass

    def Initialize_many_bodies(self, data_path:str) -> None:
        """
        Identifies all the inital conditions of the many body system;
        -reading the data from external files 
        -allocating an obj for all given in the data file 
        """
        init_variables , names = data_readout.readfile(data_path)
        self.obj_names = names
        for i in range(len(init_variables)):
            self.Initializing_Body(init_variables[i][0],init_variables[i][1],init_variables[i][2])
        pass

    def Initializing_Body(self, position, velocity, mass, name) -> None:
        """
        Initializes the object of a single body 
        """
        one_body = Physical_Obj(position, velocity, mass, name)
        self.heavy_objects.append(one_body)
        pass


if __name__ == "__main__":
    my_system = Many_Body_System()
    my_system.Initiating_bodies("/home/dompo/Documents/Studium/ComputationalPhysics_MaterialSciencesSoSe2023/ManyBodyInt/PlanetData")
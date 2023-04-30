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

    def Initialize_System(self, data_path:str) -> None:
        """
        Identifies all the inital conditions of the many body system;
        -reading the data from external file 
        -allocating an obj for all given in the data file 
        """
        init_variables , names = data_readout.readfile(data_path)
        self.obj_names = names
        for i in range(len(init_variables)):
            obj_info = init_variables[i]
            self.all_current_position.append(obj_info[0])
            self.all_current_velocity.append(obj_info[1])
            self.Initializing_Body(obj_info[0] ,obj_info[1],obj_info[2])
        pass

    def Initializing_Object(self, position, velocity, mass, name) -> None:
        """
        Initializes the object of a single body 
        """
        one_body = one_body.Atom(position, velocity, mass, name)
        self.heavy_objects.append(one_body)
        pass


if __name__ == "__main__":
    my_system = Many_Body_System()
    my_system.Initiating_bodies("/home/dompo/Documents/Studium/ComputationalPhysics_MaterialSciencesSoSe2023/ManyBodyInt/PlanetData")
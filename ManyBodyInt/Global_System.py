"""
The Many Body System is the Object of a collection of all bodies. This Object enables the interaction 
between the single Objects.
"""
import ManyBodyInt.data_readout as data_readout
import ManyBodyInt.One_Body as One_Body
# maybe needed in __init__: , file_path1:str, mass_pos, name_pos, file_path2:str=None, pos_pos, vel_pos
class Many_Body_System():
    def __init__(self:object) -> None:
        """
        The list of all the objects can be found here
        """
        self.heavy_objects = []  # here a list of all the objects are stored
        pass

    def Initiating_bodies(self, data_path:str) -> None:
        """
        Identifies all the inital conditions of the many body system;
        -reading the data from external files
        -allocating position 
        """
        init_variables:list, names:list =data_readout.readfile_pos_vel_mass(data_path)
        for i in range(len(init_variables)):
            self.Initializing_Body(init_variables[i][0],)
        pass

    def Initializing_Body(self, position, velocity, mass) -> None:
        self.heavy_objects.append()
        pass

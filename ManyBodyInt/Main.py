import sys 
import ManyBodyInt.data_readout 
import ManyBodyInt.Forces
from ManyBodyInt.Global_System import Many_Body_System
from ManyBodyInt.One_Body import Physical_Obj

"""
These are variables to execute my programm, change these for the necessary tasks
"""
work_dir = "/home/dompo/Documents/Studium/ComputationalPhysics_MaterialSciencesSoSe2023/ManyBodyInt"
data_directory = "/home/dompo/Documents/Studium/ComputationalPhysics_MaterialSciencesSoSe2023/ManyBodyInt/PlanetData"

### Planetary Movement in Solarsystem
name_pos:int = 1  # postion of name in data (start counting at 0)
mass_pos:int = 0  # ----"----- mass in data
pos_pos:list = [0,1,2] # planet position positioning in data (start counting at 0)
vel_pos:list = [0,1,2]  # planet velocity positioning in data 
# Unit transformation
mass_unit = 10**(29)  # kg
length_unit = 1.49597870691 *10**(11)  # Au - >m
time_unit = 86400  # day -> s
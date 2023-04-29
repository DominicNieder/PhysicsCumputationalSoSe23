import sys , os
import Forces
from Global_System import Many_Body_System
from One_Body import Physical_Obj

"""
These are variables to execute my programm, change these for the necessary tasks
"""
### Path to Data
path_to_main = os.path.abspath(os.path.dirname(__file__))  # working directory
data_directory = path_to_main +"/PlanetData"    # data directory
data_file_1 = data_directory + "/planets.dat"   # location file 1
data_file_2 = data_directory + "/planets2.dat"  # location file 2

### Planetary Movement in Solarsystem
name_pos:int = 1  # postion of name in data (start counting at 0)
mass_pos:int = 0  # ----"----- mass in data
pos_pos:list = [0,1,2] # planet position positioning in data (start counting at 0)
vel_pos:list = [0,1,2]  # planet velocity positioning in data 

# Unit transformation
mass_unit = 10**(29)  # kg
length_unit = 1.49597870691 *10**(11)  # Au -> m
time_unit = 86400  # day -> s

"""
The Code is implemented here
"""
# Main 
Solar_System_1 = Many_Body_System()
Solar_System_1.Initialize_many_bodies(data_file_1)
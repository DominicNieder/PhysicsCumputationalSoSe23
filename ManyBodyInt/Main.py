"""
copied from the .dat files...
    planets.dat:
        !% position and velocity data of all 9 planets in the solar system with Sun at origin
        !% position in units of AU ( 1AU = 1.49597870691E+11 meter )
        !% velocity in units of AU/day ( 1day = 86400 second )
    mass.dat:
        mass data of all 9 planets in the solar system the Sun
        mass in units of 10**29 kg
"""
import sys 
import ManyBodyInt.data_readout 
import ManyBodyInt.Forces
from ManyBodyInt.Global_System import Many_Body_System
from ManyBodyInt.One_Body import Physical_Obj

### These are variables to execute my programm
work_dir = 
data_directory = 
name_pos:int = 1  # postion of name in data (start counting at 0)
mass_pos:int = 0  # ----"----- mass in data
pos_pos:list = [0,1,2] # planet position positioning in data (start counting at 0)
vel_pos:list = [0,1,2]  # planet velocity positioning in data 


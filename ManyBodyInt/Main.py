import os  # handeling files
import numpy as np
from tqdm import tqdm  # for a nice progress bar 
import ast  # converts str([...]) to list:[...]
from Global_System import Many_Body_System  # The System class object
import data_readout  # functions for reading and writing files
import matplotlib.pyplot as plt  # for plotting - I am having trouble downloading ovito... 
from mpl_toolkits.mplot3d import Axes3D
"""
These are variables to execute my programm, change these for the necessary tasks
"""
### Path to Data
path_to_main = os.path.abspath(os.path.dirname(__file__))  # working directory
data_directory = path_to_main +"/PlanetData"    # data directory
data_file_1 = data_directory + "/planets1.dat"   # location file 1
data_file_2 = data_directory + "/planets2.dat"  # location file 2
name_sim_file = "/earth_sun"
### running options
time_step:float = 1/2  # day
simulation_period = 365 # days
integration_methods = ["Euler", "Verlet", "Velocity Verlet"]
# leads to 
number_of_iterations:int = int(simulation_period/time_step)

# Unit transformation 
mass_unit = 10**(29)  # -> kg
length_unit = 1.49597870691 *10**(11)  # m -> Au
time_unit = 86400  # s per day

"""
The Code is implemented here
"""
# Main 
Solar_System_1 = Many_Body_System()  # creating the object Solarsystem 
Solar_System_1.Initialize_System(data_file_1)  # initializing with data_file_1
all_orbitals , pathNname_sim_file = data_readout.Creat_New_File(path_to_main, name_sim_file)
#for i in range(Solar_System_1.number_of_obj):
#    print("position:Vector | velocity:Vector | Mass | Name")
#    print(Solar_System_1.all_ever_position[0][i], Solar_System_1.all_ever_velocity[0][i],Solar_System_1.all_mass[i],Solar_System_1.obj_names[i])
for j in tqdm(range(number_of_iterations)):
    Solar_System_1.Update_Movement(time_step)
    #for i in Solar_System_1.all_current_position:
    all_orbitals.write(str(Solar_System_1.all_current_position)+"\n")
    for i in range(Solar_System_1.number_of_obj):
        dot = []
        all_acc = Solar_System_1.all_current_acc[i].tolist()
        for x in range(2):
            dot.append(all_acc[x]*Solar_System_1.all_current_velocity[i][x])
        print('acc * vel', sum(dot))
all_orbitals.close()

x_e, y_e, z_e = [], [], []
x_s, y_s,z_s = [], [], []
file = open(pathNname_sim_file, "r")

for line in file:
    l = ast.literal_eval(line)
    x_e.append(l[1][0])
    y_e.append(l[1][1])
    z_e.append(l[1][2])
    x_s.append(l[0][0])
    y_s.append(l[0][1])
    z_s.append(l[0][2])


    
file.close()


ax = plt.figure().add_subplot(projection='3d')
ax.plot(x_e,y_e,z_e, "o", color="blue")
ax.plot(x_s,y_s,z_s, "o", color="red")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Solarsystem")
plt.show()

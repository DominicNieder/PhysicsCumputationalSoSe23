import os  # handeling files
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
data_file_1 = data_directory + "/planets.dat"   # location file 1
data_file_2 = data_directory + "/planets2.dat"  # location file 2
name_sim_file = "/all_orbital"
### running options
time_step:float = 1/2  # day
simulation_period = 1*365 # days
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
all_orbitals.close()

list_all_plantes_unsorted =[]
file = open(pathNname_sim_file, "r")

for line in file:
    l = ast.literal_eval(line)
    print(l)
    break
file.close()

"""
ax = plt.figure().add_subplot(projection='3d')

for i in Solar_System_1.all_ever_position:
    for j in i:
        list_all_plantes_unsorted.append(j)
        all_orbitals.write
ax.contour(list_all_plantes_unsorted)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Solarsystem")
plt.show()
"""
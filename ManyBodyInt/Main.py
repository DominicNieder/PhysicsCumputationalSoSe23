import os
from Global_System import Many_Body_System

"""
These are variables to execute my programm, change these for the necessary tasks
"""
### Path to Data
path_to_main = os.path.abspath(os.path.dirname(__file__))  # working directory
data_directory = path_to_main +"/PlanetData"    # data directory
data_file_1 = data_directory + "/planets.dat"   # location file 1
data_file_2 = data_directory + "/planets2.dat"  # location file 2

### running options
time_step:float = 1/2  # day
simulation_period = 500*365 # days
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
#for i in range(Solar_System_1.number_of_obj):
#    print("position:Vector | velocity:Vector | Mass | Name")
#    print(Solar_System_1.all_ever_position[0][i], Solar_System_1.all_ever_velocity[0][i],Solar_System_1.all_mass[i],Solar_System_1.obj_names[i])
print(type(number_of_iterations))
print(type(range(number_of_iterations)))
for j in range(number_of_iterations):
    Solar_System_1.Update_Movement(time_step)

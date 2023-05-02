"""
Here functions for reading/writing text/data files are located
"""
import os

def Creat_New_File(path:str, name_of_file:str = "Simulation", number_of_file:int=0) ->bool:
    """
    Creating a new File called ("path"+"name_of_file"+"number_of_file".txt)
    added to the name.
    Note that the .txt will be added automatically
    """
    while os.path.exists(path+name_of_file+str(number_of_file)+".txt"):  # iterate number until file does not exist
        number_of_file +=1
    location_and_name = path+name_of_file+str(number_of_file)+".txt"
    file = open(location_and_name, "w")
    return(file,location_and_name)

def Initialize_dataSheet_Ovito(text_wrapper, timestep, number_of_atoms):
    """
    Starts the Output format for trajectory readable by visualisation software ovito
    """
    text_wrapper.write("ITEM: TIMESTEP\n"+timestep)
    text_wrapper.write("ITEM: NUMBER OF ATOMS\n"+number_of_atoms)
    pass

def find_files(path:str) -> list:
    """
    Finds files in which to look for initialisation data for the objects.
    Returns list of str of the name of the files.
    Not needed for Ex. sheet 1
    """
    with os.scandir(path) as dir:
        files = []
        for entry in dir:
            if entry.is_file:
                print(entry.name)
                print(type(entry.name))
                files.append(entry.name)
    return(files)


# This function is not needed, as all variables are seved in one file now...
def Read_Dir(path:str) -> list:
    """
    Identifies all files of the path and reads all files;
    If its a directory: Identifies all files in directory
    """
    print("reading directory...")
    if os.path.isfile(path):
        print("    found file")
        init_conditions_of_system = Read_File_pos_vel_mass()
        return(init_conditions_of_system)
    elif os.path.isdir(path):
        file_names = find_files(path)
        numb_of_files = len(file_names)
        print("    files in directory: ",numb_of_files)
        init_of_collection_of_systems = []
        for j in range(numb_of_files):
            init_of_collection_of_systems.append(Read_File_pos_vel_mass(path+"/"+file_names[j]))  # [group]
        return(init_of_collection_of_systems)
    
def Read_File_pos_vel_mass(path_1:str):
    """
    Finds all positions velocities and mass of all objects. Rerturns objects in the form of
    [[xyz, v_xyz, mass], [...],... ], [name_1, name_2, ...]
    """
    with open(path_1, "r") as data_1:
        groups:list = []  # hold list of list of variables of all objects []
        names:list = []  # the index of names fitts to the variables in groups
        i = 0
        print("Reading data of file...")
        for line in data_1:
            pos:list = []
            vel:list = []
            group:list = []  # [pos, vel, mass] 
            pos.append(float(line.split()[0]))
            pos.append(float(line.split()[1]))
            pos.append(float(line.split()[2]))
            vel.append(float(line.split()[3]))
            vel.append(float(line.split()[4]))
            vel.append(float(line.split()[5]))
            mass = float(line.split()[6])
            names.append(line.split()[7])  # after vel. there is the name 
            #print('\n',names[i],"\npos:", pos,"\nvel",vel, "\nmass",mass)
            i+=1
            group.append(pos)
            group.append(vel)
            group.append(mass)
            groups.append(group)
        print("Finished reading data!")    
    return(groups, names)


# here I can try the different functions by them selfes
if __name__ == "__main__":
    import numpy as np
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    data = np.random.random(size=(3, 3, 3))
    z, x, y = data.nonzero()
    ax.scatter(x, y, z, c=z, alpha=1)
    plt.show()
    pass

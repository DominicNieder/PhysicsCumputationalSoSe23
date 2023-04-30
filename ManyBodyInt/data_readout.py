"""
Here functions for reading text/data files are located
"""
import os

def find_files(path:str) -> list:
    """
    Finds files in which to look for initialisation data for the objects.
    Returns list of str of the name of the files.
    Not needed for Ex. sheet 1
    """
    path = os.path.abspath(os.path.dirname(__file__))
    with os.scandir(path) as dir:
        files = []
        for entry in dir:
            if entry.is_file:
                print(entry.name)
                print(type(entry.name))
                files.append(entry.name)
    return(files)


# This function is not needed, as all variables are seved in one file now...
def Read_Dir(path_1:str) -> list:
    print("reading directory...")
    if os.path.isfile(path_1):
        print("    found file")
        init_conditions_of_system = Read_File_pos_vel_mass()
        return(init_conditions_of_system)
    elif os.path.isdir(path_1):
        file_names = find_files(path_1)
        numb_of_files = len(file_names)
        print("    files in directory: ",numb_of_files)
        init_of_collection_of_systems = []
        for j in range(numb_of_files):
            init_of_collection_of_systems.append(Read_File_pos_vel_mass(path_1+"/"+file_names[j]))  # [group]
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
        print("    reading data of file...")
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
        print("    finished reading data!")    
    return(groups, names)


# here I can try the different functions by them selfes
if __name__ == "__main__":
    pass

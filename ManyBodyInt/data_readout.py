"""
Here functions for reading/writing text/data files are located
"""
import os

def Creat_New_File(path:str, name_of_file:str = "Simulation", number_of_file:int=0):
    """
    Creating a new File called ("path"+"name_of_file"+"number_of_file".txt)
    added to the name.
    Note that the .txt will be added automatically
    """
    while os.path.exists(path+name_of_file+str(number_of_file)+".txt"):  # iterate number until file does not exist
        number_of_file +=1
    file = open(path+name_of_file+str(number_of_file)+".txt", "w")
    return(file)

def Write_into_File(path:str):
    pass        

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
    Test_text = [[0,3,4],[4,7,8],[4,93,9]]
    TEST=(Creat_New_File(os.path.abspath(os.path.dirname(__file__))))
    for i in Test_text:
        TEST.writelines(str(i)+"\n")
    TEST.close()
    pass

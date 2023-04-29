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
    with os.scandir(path) as dir:
        files = []
        for entry in dir:
            if entry.is_file:
                print(entry.name)
                print(type(entry.name))
                files.append(entry.name)
    return(files)

# this function was realised with the idea to read many data files and to be able to access the data
# freely afterwards - though I then decided to leave this for futer implementation if needed;
# Chose to reorganize the data into one file
def Read_Files(files:list, path) -> list:
    """
    Reads all the data files from the names given in "files".
    Copies the data into list. Saves all the data from all files in a list 
    of lists (alphabetical order of "files").
    """
    pass


def readfile_pos_vel_mass(path_1:str) -> list:
    """
    Finds all positions velocities and mass of objects.
    """
    with open(path_1, "r") as data_1:
        groups:list = []  # has all the necessary variables of all objects
        names:list = []  # the index of names fitts to the variables in groups
        for line in range(len(data_1)):
            pos:list = []
            vel:list = []
            group:list = []  # [pos, vel, mass] 
            pos.append(float(data_1[line].split()[0]))
            pos.append(float(data_1[line].split()[1]))
            pos.append(float(data_1[line].split()[2]))
            vel.append(float(data_1[line].split()[3]))
            vel.append(float(data_1[line].split()[4]))
            vel.append(float(data_1[line].split()[5]))
            mass = float(data_1[line].split()[6])
            names.append(data_1[line].split()[3])  # after vel. there is the name 
            print(names[line],"\npos:", pos,"\nvel",vel, "\mass",mass)
            group.append(pos).append(vel).append(mass)
            groups.append(group)
    return(groups, names)


#if __name__ == "__main__":

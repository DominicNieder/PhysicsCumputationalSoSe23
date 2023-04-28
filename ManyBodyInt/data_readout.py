"""
Here functions for reading text/data files are located
"""
import os
with os.scandir("/home/dompo/Documents/Studium/ComputationalPhysics_MaterialSciencesSoSe2023/ManyBodyInt") as dir:
    for entry in dir:
        if entry.is_file:
            print(entry.name)

"""
def read(path:str):
    with open(path,"r") as data:
        for line in range(len(data)/2):
            pos = []
            vel = []
            pos.append(float(planets_data[line].split()[0]))
            pos.append(float(planets_data[line].split()[1]))
            pos.append(float(planets_data[line].split()[2]))
            line +=1
            vel.append(float(planets_data[line].split()[0]))
            vel.append(float(planets_data[line].split()[1]))
            vel.append(float(planets_data[line].split()[2]))
            name = planets_data[line+1].split()[3]
            print("name","\npos:", pos,"\nvel",vel)
            for line2 in mass_data:
                comp = ine2.split()
                if comp[1] == name:
                    mass = float(comp[0])
"""
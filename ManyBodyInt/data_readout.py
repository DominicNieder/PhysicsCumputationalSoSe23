

with open(path_massNnames, "r") as mass_data:


    with open(path_posNvel,"r") as planets_data:
        for line in range(len(planets_data)/2):
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

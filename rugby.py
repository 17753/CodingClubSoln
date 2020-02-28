num = 0 
loop = True
name = []
age =  []
mass = []
senior_junior = []
counter = 0
print("please enter the name,age and weight of player [please hit enter]")
while loop:
    print("please enter the name,age and weight of player [please hit enter]")      
    name.append(input())
    age.append(input())
    mass.append(input())
    counter +=1 
    for i in range(len(name)):
        if '#' in name and "0" in age and "0" in mass:
            name.remove("#")
            age.remove("0")
            mass.remove("0") 
            loop = False
for i in range(0,len(name),1):
    if int(age[i]) > 18 or int(mass[i]) > 80:
        senior_junior.append("senior")
    else:
        senior_junior.append("junior")
for i in range(0,len(name),1):      
    print(str(name[i]), str(senior_junior[i]))


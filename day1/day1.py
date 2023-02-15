with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

elfs = []
calories = 0
for line in lines: 
    if line == '':
        elfs.append(calories)
        calories = 0
    else:
        calories += int(line)


print(max(elfs)) #Respuesta 1

elfs.sort()
n = len(elfs)-1
print(elfs[n] + elfs[n-1] + elfs[n-2]) #Respuesta 2


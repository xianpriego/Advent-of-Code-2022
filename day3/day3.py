with open("./day3/input3.txt") as f:
    rucksacks = [x.strip() for x in f.readlines()]



divided_rucksacks = []
group_of_three = []

i = 0
for rucksack in rucksacks:
    median = int(len(rucksack) / 2)
    divided_rucksacks.append(set(rucksack[:median]).intersection(rucksack[median:]))
    if i<(len(rucksacks)-3):
        if i % 3 == 0:
            group_of_three.append(set(rucksacks[i]).intersection(set(rucksacks[i+1]), set(rucksacks[i+2]) ))
    i+=1


print(group_of_three)

sum1 = 0
sum2 = 0
for intersection in divided_rucksacks:
    for x in intersection:
        val1 = ord(x)
        if val1 >= 97:
            sum1 += val1 - 96
        else:
            sum1 += val1 - 38

    
for intersection in group_of_three:
    for y in intersection:
        val2 = ord(y)
        if val2 >= 97:
            sum2 += val2 - 96
        else:
            sum2 += val2 - 38
    
    

print(sum1) #First answer
print(sum2) #Second answer








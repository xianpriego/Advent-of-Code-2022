with open("input.txt") as f:
    pairs = [[x.strip().split(",")[0].split("-"), x.strip().split(",")[1].split("-")] for x in f.readlines()]

    

def contained1(x,y): 
    if int(x[0]) < int(y[0]):
        return int(x[1]) >= int(y[1])
    elif int(x[0]) > int(y[0]):
        return int(x[1]) <= int(y[1])
    else:
        return int(x[1]) >= int(y[1]) or int(x[1]) <= int(y[1])

def contained2(x,y):
    return not (int(x[1]) < int(y[0]) or int(y[1]) < int(x[0]))

sum1 = 0
sum2 = 0
for pair in pairs:
    if contained1(pair[0], pair[1]):
        sum1+=1
    if contained2(pair[0], pair[1]):
        sum2+=1



print(sum1) #first answer
print(sum2) #second answer

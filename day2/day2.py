with open("input2.txt") as f:
    rounds = [x.strip().split() for x in f.readlines()]

scores1 = {'AX': 3, 'AY': 6, 'AZ': 0, 'BX' : 0, 'BY' : 3, 'BZ' : 6, 'CX' : 6, 'CY' : 0, 'CZ' : 3}
scores2 = {'X' : 1, 'Y' : 2, 'Z' : 3}

scores3 = {'X' : 0, 'Y' : 3, 'Z' : 6}
scores4 = {'AX': 'C', 'AY': 'A', 'AZ': 'B', 'BX' : 'A', 'BY' : 'B', 'BZ' : 'C', 'CX' : 'B', 'CY' : 'C', 'CZ' : 'A'}
scores5 = {'A' : 1, 'B' : 2, 'C' : 3}


score1 = 0
score2 = 0
for round in rounds:
    score1 += scores1[round[0] + round[1]] + scores2[round[1]]
    score2 += scores3[round[1]] + scores5[scores4[round[0] + round[1]]]

print(score1) #Respuesta 1
print(score2) #Respuesta 2

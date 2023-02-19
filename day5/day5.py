import re 

with open('input.txt') as file:
    stack_strings, lines = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))


moves = []
for line in lines:  
    values = [int(s) for s in line.split() if s.isdigit()]
    moves.append(values)
print(stack_strings)
print(moves)

#We have stored in a list of lists of three numbers that represents the movements

#Now we have implement the cargo and initilize it to its initial state given in the input.
# Cargo will be implemented with a list of stacks, for example, the move [3, 4, 6] it's doing
# 3 times the following operation -> insert the element given by unstack(stack4) in stack6

"""
     [W]         [J]     [J]        
     [V]     [F] [F] [S] [S]        
     [S] [M] [R] [W] [M] [C]        
     [M] [G] [W] [S] [F] [G]     [C]
 [W] [P] [S] [M] [H] [N] [F]     [L]
 [R] [H] [T] [D] [L] [D] [D] [B] [W]
 [T] [C] [L] [H] [Q] [J] [B] [T] [N]
 [G] [G] [C] [J] [P] [P] [Z] [R] [H]
  1   2   3   4   5   6   7   8   9 
"""

string_indexes = [i for i,string in enumerate(stack_strings[-1]) if string.isdigit()] #Here we are storing the possible positions of the letters in the input
cargo = [[],[],[],[],[],[],[],[],[]]

def initialize_cargo(stack_strings, string_indexes, cargo):
    for line in stack_strings[:-1]:
        stack_number = 0
        for index in string_indexes:
            value = line[index]
            if value != " ":
                cargo[stack_number].insert(0, line[index])
            stack_number += 1
    return cargo

cargo = initialize_cargo(stack_strings, string_indexes, cargo)
              





#PART 1:
for move in moves:
    for _ in range(move[0]):
        removed = cargo[move[1] - 1].pop()
        cargo[move[2] - 1].append(removed)
        
for stack in cargo:
    print(stack.pop()) #ANSWER 1

print("-----------------------------------------------")


cargo = [[],[],[],[],[],[],[],[],[]]
initialize_cargo(stack_strings, string_indexes, cargo)

for move in moves:
    removed = cargo[move[1] - 1][-move[0]:]  #We store the elements to be moved
    cargo[move[1] - 1] = cargo[move[1] - 1][:-move[0]] #We remove this element from the origin list
    for element in removed: #We insert the elements on the destination list
        cargo[move[2] - 1].append(element)


for stack in cargo:
    print(stack.pop()) #ANSWER 2


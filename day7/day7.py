
FILENAME = "input.txt"
DOLAR = '$'
CD = 'cd'
DIR = 'dir'
LS = 'ls'
UMBRAL = 100000
TOTAL_DISK_SPACE = 70000000
UPDATE_SPACE = 30000000


import time

def readFile(filename: str) -> str:
    '''
    Reads the file
    '''
    with open(filename) as file:
        commandOutput = [line.split() for line in file.readlines()]

    
    return commandOutput


def multiply_file_content(file_path, n):
    with open(file_path, 'r') as file:
        file_content = file.read()
        new_content = file_content * n
        
    with open(file_path, 'w') as file:
        file.write(new_content)



def fileSystem(commands: list, index: int, lenOfCommands: int) -> list:

    filesSumSize = 0
    file_system = [filesSumSize,[]] #Initialize it with an empty list

    
    while index < lenOfCommands: #Iterate over the list of commands

        if CD in commands[index]:
            end = commands[index].pop()
            if end == '..':
                file_system[0] = filesSumSize
                return file_system, index+1
            else:
                subFileSystem, newIndex = fileSystem(commands, index+1, lenOfCommands)
                file_system[1].append(subFileSystem) #Add to the fileSystem the return of the recursive call
                filesSumSize += subFileSystem[0]
                index = newIndex #We must update the index to skip commands read by recursive calls

        elif LS in commands[index]:
            index+=1
            while index < lenOfCommands and DOLAR not in commands[index]:
                if DIR not in commands[index]:
                    filesSumSize += int(commands[index][0])
                index+=1
        
    
    #if While ends then we have read all the commands so we have to return the actual file_system and index
    file_system[0] = filesSumSize
    return file_system, index



def compute_first_solution(fileSystem) -> int:

    solution = 0

    match fileSystem:

        case [size, []]:
            if size <= UMBRAL:
                return size
            else:
                return 0
        case [size, directories]:
            for directory in directories:
                solution += compute_first_solution(directory)
            if size <= UMBRAL:
                solution += size
                return solution
            else:
                return solution
    

def compute_second_solution(fileSystem, used_space, minimo) -> int:
    
    match fileSystem:

        case [size, []]:
            free_space = TOTAL_DISK_SPACE - used_space + size
            if free_space >= UPDATE_SPACE and minimo > size:
                return size
            return minimo
        
        case [size, directories]:
            free_space = TOTAL_DISK_SPACE - used_space + size
            if free_space >= UPDATE_SPACE:
                if minimo > size:
                    minimo = size
                for directory in directories:
                    minimo = compute_second_solution(directory, used_space, minimo)
                return minimo
            
            
            return minimo
                


if __name__ == '__main__':
    commandOutput = readFile(FILENAME)
    lenght = len(commandOutput)
    fileSystem, _ = fileSystem(commandOutput, 0, lenght)
    print("The first solution is: ", compute_first_solution(fileSystem))
    print("The second solution is: ", compute_second_solution(fileSystem, fileSystem[0], TOTAL_DISK_SPACE))


    













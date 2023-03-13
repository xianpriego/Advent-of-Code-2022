
FILENAME = "day6/input.txt"

def readFile(filename: str) -> str:
    '''
    Reads the file
    '''
    with open(filename) as file:
        letters = file.read()
    
    return letters
    
def isMarker(possibleMarker: str) -> bool:
    '''
    Returns true if all characters are different
    '''
    characters = []
    for ch in possibleMarker:
        if ch in characters:
            return False
        else:
            characters.append(ch)
    return True   
    
def firstPart(datastream: str) -> int:
    for i in range(3, len(datastream)):
        possibleMarker = datastream[i-3 : i+1]
        if isMarker(possibleMarker):
            return i+1
            
def secondPart(datastream: str) -> int:
    for i in range(13, len(datastream)):
        possibleMarker = datastream[i-13 : i+1]
        if isMarker(possibleMarker):
            return i+1
    
if __name__ == '__main__':
    
    datastream = readFile(FILENAME)

    print("First Solution: ", firstPart(datastream))
    print("Second Solution: ", secondPart(datastream))
        


        

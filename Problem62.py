from collections import Counter

def Solve():

    target = 5
    cubeDigitCounter = Counter()
    firstCubeDict = dict()

    n = 0
    while True:
        n += 1
        cube = n ** 3
        cubeDigits = ''.join(sorted([x for x in str(cube)]))
        cubeDigitCounter[cubeDigits] += 1
        if cubeDigitCounter[cubeDigits] == 1:
            firstCubeDict[cubeDigits] = cube

        if cubeDigitCounter[cubeDigits] == target:
            return(firstCubeDict[cubeDigits])

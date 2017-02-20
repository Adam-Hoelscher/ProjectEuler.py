from Functions import IsPrime
from itertools import permutations

def Solve():

    target = 8
    replace = target - 5
    length  = replace + 1

    while True:
        fixedDigitCount = length - replace

        # the last digit must be fixed; otherwise too many of the substitutions will be even
        fixedDigitIndexes = permutations(range(length-1), fixedDigitCount - 1)
        fixedDigitIndexes = [list(x) + [length-1] for x in fixedDigitIndexes]

        # the last digit must be one of [1,3,7,9]; otherwise all substitutions will be not prime
        fixedDigitValues = permutations(range(10), fixedDigitCount - 1)
        fixedDigitValues = sum([[list(x) + [y] for y in [1,3,7,9]] for x in fixedDigitValues], [])

        # print(fixedDigitIndexes)
        # print(fixedDigitValues)
        # return 0

        for fixedDigitIndexSet in fixedDigitIndexes:
            for fixedDigitValueSet in fixedDigitValues:
                testDigits = ['x'] * length
                for i in range(len(fixedDigitIndexSet)):
                    testDigits[fixedDigitIndexSet[i]] = str(fixedDigitValueSet[i])
                count = 0
                for x in range(9, -1, -1):
                    if x == 0 != fixedDigitIndexSet[0]: break
                    testValue = int(''.join(testDigits).replace('x', str(x)))
                    if IsPrime(testValue):
                        count += 1
                        if count == target:
                            return testValue
        length += 1

from Functions import IsPrime
from itertools import permutations

def Solve():

    # don't test 9 digits numbers. sum([1:9]) = 45 -> all 9-digit pandigital numbers are divisble by 9
    for length in range(8,0,-1):
        digits = range(1, length + 1)
        numbers = [x for x in permutations(digits)][::-1]
        for n in numbers:
            test = int(''.join([str(x) for x in n]))
            if IsPrime(test):
                return(test)

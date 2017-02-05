from Functions import PrimeFactors
from functools import reduce
from operator import mul

def Solve():
    stop = False
    n = 0
    step = 1
    while not stop:
        n += step
        step += 1
        factors = PrimeFactors(n, self = False)
        try:
            countFactors = reduce(mul,((1+x) for x in factors.values()))
        except:
            countFactors = 1
        stop = countFactors > 500
    return(n)
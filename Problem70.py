from Functions import PrimeSieve, GCD, PrimeFactors
from collections import Counter

def Solve():

    limit = 10**7

    minRatio = limit

    primeFactors = [[] for x in range(limit)]
    for n in range(2,limit):
        if len(primeFactors[n]) == 0:
            for i in range(n, limit, n):
                primeFactors[i].append(n)
    primeFactors = [set(x) for x in primeFactors]

    def phi(x):
        return sum(len(primeFactors[x] & other) == 0 for other in primeFactors[:x+1])-1

    for n in range(limit-1, 1, -1):
        tot = phi(n)
        if Counter([x for x in str(n)]) == Counter([x for x in str(tot)]):
            print(n)
            if n/tot < minRatio:
                minRatio = n/tot
                minN = n

    return minN

if __name__=='__main__':
    import cProfile
    cProfile.run('Solve()', sort='cumtime')

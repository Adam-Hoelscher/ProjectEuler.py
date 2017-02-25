from Functions import PrimeSieve
from Functions import IsPrime


def Solve():

    target = 5

    sieve = PrimeSieve(float('inf'))

    # prime the data so that we exclude 2 and 5. 2 and 5 will never be part of a set that meets the condition.
    # this invalidates a target value of 1, but that case is trivial (it's 2). as we enter the loop, it will look like
    # we ran the loop to generate 2,3,5,7 and then dropped 2 and 5 from primes and removed sets containing them from
    # valid sets
    primes = [sieve.__next__() for x in range(4)]
    primes.remove(2)
    primes.remove(5)
    validSets = [{3}]
    primeIndex = len(primes) - 1

    while True:
        nextPrime = primes[primeIndex]
        smallerPrimes = primes[:1+primeIndex]
        while nextPrime >= max(primes):
            primes.append(sieve.__next__())
        nextValidSets = validSets[:]
        append = nextValidSets.append
        append({nextPrime})
        pairsWith = set()
        add = pairsWith.add
        for p in primes:
            if IsPrime(int(str(p) + str(nextPrime))):
                if IsPrime(int(str(nextPrime) + str(p))):
                    add(p)
        for currentSet in validSets:
            if currentSet - pairsWith == set():
                candidateSet = set(currentSet)
                candidateSet.add(nextPrime)
                if len(candidateSet) >= target:
                    return sum(candidateSet)
                append(set(candidateSet))
        validSets = nextValidSets
        primeIndex += 1


if __name__ == '__main__':

    from time import clock

    start = clock()
    print(Solve(), clock() - start)

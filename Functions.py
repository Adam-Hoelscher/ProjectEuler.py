from collections import Counter
from functools import lru_cache, reduce


@lru_cache(None)
def IsPrime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    else:
        if not n % 2:
            return False
        for f in range(3, 1 + int(n ** .5), 2):
            if not n % f:
                return False
        return True

@lru_cache(None)
def PrimeFactors(n, self=True, unique=False):

    factors = []

    if n >= 2:
        p = 2
        while n % p == 0:
            factors.append(p)
            n //= p
        for p in range(3, 1 + int(n ** .5), 2):
            while n % p == 0:
                factors.append(p)
                n //= p
            if n == 1:
                break

    if n > 1 and self: factors.append(n)

    if unique:
        factors = set(factors)
    else:
        factors = Counter(factors)
    return factors

@lru_cache(None)
def PrimeFactors2(n, self=True, unique=False):
    factors = dict()
    if n < 2:
        return factors
    for p in PrimeSieve(1 + int(n ** .5)):
        while n % p == 0:
            factors.setdefault(p, 0)
            factors[p] += 1
            n //= p
            if unique:
                factors[p] = 1
        if n == 1:
            break
    if n > 1 and self: factors[n] = 1
    return factors

@lru_cache(None)
def Factors(x):
    from math import sqrt, ceil
    facs = []
    for n in range(1, ceil(sqrt(x))):
        if x % n == 0:
            facs.append(n)
    for fac in facs[1:][::-1]:
        facs.append(x // fac)
    if abs(sqrt(x) - round(sqrt(x))) < 1e-6:
        facs.append(round(sqrt(x)))
    return facs

@lru_cache(None)
def IsPanDig(x, end=9, begin=1):
    temp = list(str(x))
    temp.sort()
    return temp == [str(y) for y in range(begin, end + 1)]

def GCD(x, y=None):

    numbers = set()

    for i in [x, y]:
        if hasattr(x, "__iter__"):
            numbers.update(i)
        else:
            numbers.update([i])

    numbers = set(filter(bool, numbers))

    def GCDpair(x, y):
        if x == 0:
            return y
        else:
            return GCDpair(y % x, x)

    return reduce(GCDpair, numbers)

def LCM(x, y=None):

    numbers = set()

    for i in [x, y]:
        if hasattr(x, "__iter__"):
            numbers.update(i)
        else:
            numbers.update([i])

    numbers = set(filter(bool, numbers))

    def LCMpair(x, y):
        return x // GCD(x, y) * y

    return reduce(LCMpair, x)

def PrimeSieve(valLimit=float('inf'), lengthLimit=float('inf')):

    def FastPrimeSieve(valLimit, lengthLimit=float('inf')):
        valLimit = int(valLimit)
        primeList = [False, False, True] + [True, False] * ((valLimit - 2) // 2)

        # note that we have currently found no primes
        currentLength = 0

        for number, numberIsPrime in enumerate(primeList):
            if currentLength == lengthLimit:
                break
            if numberIsPrime:
                for k in range(number * number, valLimit, number):
                    primeList[k] = False
                yield number
                currentLength += 1

    def InfPrimeSieve(lengthLimit=float('inf')):
        """
        algorithm is Sieve of Eratosthenes with optimization of starting at
        square of primes.
        """

        # dictionary holding lists of the primes that are a factor of the composite
        composites = {}

        # set the number that we are testing for primality
        number = 2

        # note that we have currently found no primes
        currentLength = 0

        while number < valLimit and currentLength < lengthLimit:
            if number not in composites:
                '''
                since number is not a composite it is a new prime. mark the
                square of the prime, since the square is the first multiple of
                the prime that is not a multiple of another prime
                '''
                yield number
                composites[number ** 2] = [number]
            else:
                '''number is composite. composites[number] is the list of primes
                that divide it. mark the *next* multiple of each prime as having
                that prime as a factor'''
                for p in composites[number]:
                    composites.setdefault(p + number, []).append(p)
                del composites[number]

            number += 1

    '''
    some problems require a fixed list of primes and some require that we
    can extend the list at will. The fixed list is much faster to generate 
    and then be done with, so use that whenever possible
    '''
    if valLimit==float('inf'):
        temp = InfPrimeSieve(lengthLimit)
    else:
        temp = FastPrimeSieve(valLimit, lengthLimit)

    return(temp)


if __name__ == '__main__':
    from time import clock

    limit = 10000

    start = clock()
    y = [PrimeFactors(x) for x in range(limit)]
    # print(y)
    print(clock() - start)

    start = clock()
    z = [PrimeFactors2(x) for x in range(limit)]
    # print(z)
    print(clock() - start)

    print(y == z)

    limit = 100000000

    start = clock()
    y = [PrimeFactors(x) for x in range(limit-1000, limit)]
    # print(y)
    print(clock() - start)

    start = clock()
    z = [PrimeFactors2(x) for x in range(limit-1000, limit)]
    # print(z)
    print(clock() - start)

    print(y == z)

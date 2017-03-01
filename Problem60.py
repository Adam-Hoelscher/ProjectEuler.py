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


def Solve1():

    target = 5

    # cheat: use the finite sieve since I already know the answer.
    sieve = PrimeSieve(10**4)

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
        while nextPrime >= max(primes):
            primes.append(sieve.__next__())
        nextValidSets = validSets[:]
        append = nextValidSets.append
        append({nextPrime})
        pairsWith = set()
        add = pairsWith.add
        for p in primes:
            if IsPrime(int(str(p) + str(nextPrime))):
                if (int(str(nextPrime) + str(p))) in primes:
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


def Solve2():
    from Functions import PrimeSieve
    from Functions import IsPrime as is_prime
    from time import clock

    def Cat(a, b):
        return int(str(a) + str(b))

    def PrimePairSet(set):
        a = set[0]
        b = set[1]
        if not is_prime(Cat(a, b)):
            return False
        if not is_prime(Cat(b, a)):
            return False

        return True

    # Section 1
    tick = clock()
    sieve = PrimeSieve(10 ** 4)
    primes = [i for i in sieve]
    tock = clock()
    print("Primes prepared in {} seconds.".format(tock - tick))

    # Section 2
    tick = clock()
    candidates = []
    for i, a in enumerate(primes):
        candidates.append([])
        for j, b in enumerate(primes[i + 1:]):
            if PrimePairSet([a, b]):
                candidates[i].append(b)
    tock = clock()
    print("Prime pairs found in {} seconds.".format(tock - tick))

    # Section 3
    tick = clock()
    for i, a_pairs in enumerate(candidates):
        a = primes[i]
        for b in a_pairs:
            b_pairs = candidates[primes.index(b)]
            for c in b_pairs:
                if c in a_pairs:
                    c_pairs = candidates[primes.index(c)]
                    for d in c_pairs:
                        if d in a_pairs and d in b_pairs:
                            d_pairs = candidates[primes.index(d)]
                            for e in d_pairs:
                                if e in a_pairs and e in b_pairs and e in c_pairs:
                                    print([a, b, c, d, e], sum([a, b, c, d, e]))
    tock = clock()
    print("Solution found in {} seconds.".format(tock - tick))

if __name__ == '__main__':

    import cProfile
    cProfile.run('print(Solve())',  sort = 'cumtime')
    cProfile.run('print(Solve1())', sort = 'cumtime')
    cProfile.run('print(Solve2())', sort = 'cumtime')


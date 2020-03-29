from Functions import PrimeSieve
from Functions import IsPrime


def Solve(target = 5):

    sieve = PrimeSieve(float('inf'))

    def TestPair(a, b):

        if not IsPrime(int(str(a) + str(b))):
            return (False)

        if not IsPrime(int(str(b) + str(a))):
            return (False)

        return(True)

    # prime the data so that we exclude 2 and 5. 2 and 5 will never be part
    # of a set that meets the condition. this invalidates a target value of 1,
    # but that case is trivial (it's 2). as we enter the loop, it will look
    # like we ran the loop to generate 2,3,5,7 and then dropped 2 and 5 from
    # primes and removed sets containing them from valid sets
    if target == 1:
        return(2)
    primes = [sieve.__next__() for x in range(3)]
    primes.remove(2)
    primes.remove(5)
    validSets = [{3}]

    # run until we find a solution
    while True:

        # move to the next prime
        p1 = sieve.__next__()

        # make a copy so that we can loop through it and add to the original
        loopSets = validSets[:]

        # loop through all smaller primes and build a set of primes that the
        # new one will work with
        pairsWith = set()
        for p0 in primes:
            if TestPair(p0, p1):
                pairsWith.add(p0)

        # check each of the existing sets to see if we can add the new prime
        # to each of them.
        for currentSet in loopSets:

            # use set difference to make sure the new prime is compatible with
            # all primes in the set we're checking
            if currentSet - pairsWith == set():

                # construct a new valid set
                candidateSet = currentSet.copy()
                candidateSet.add(p1)

                # if the new set has the desired length we're done
                if len(candidateSet) == target:
                    return sum(candidateSet)

                # if we're not done then we need to extend the list of
                # valid sets
                validSets.append(set(candidateSet))

        # the new prime by itself is a valid set
        validSets.append({p1})

        # add the new prime to the list of primes
        primes.append(p1)


def Solve1(target = 5):

    sieve = PrimeSieve(float('inf'))

    def TestPair(a, b):

        if not IsPrime(int(str(a) + str(b))):
            return (False)

        if not IsPrime(int(str(b) + str(a))):
            return (False)

        return(True)

    def TestCanAdd(current, new):
        for c in current:
            if not TestPair(c, new):
                return(False)
        return(True)

    [sieve.__next__() for x in range(3)]
    validSets = [{3}]

    while True:
        p = sieve.__next__()

        currentSets = validSets[:]
        for set in currentSets:
            temp = set.copy()
            if TestCanAdd(temp, p):
                temp.add(p)
                if len(temp) == target:
                    return(sum(temp))
                validSets.append(temp)

        validSets.append({p})


def Solve2():

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


if __name__ == '__main__':
    print(Solve())
    import cProfile
    for i in [4,5]:
        cProfile.run('print(Solve('+str(i)+'))',  sort = 'cumtime')
        # cProfile.run('print(Solve())',  sort = 'cumtime')
    # cProfile.run('print(Solve1())', sort = 'cumtime')
    # cProfile.run('print(Solve2())', sort = 'cumtime')

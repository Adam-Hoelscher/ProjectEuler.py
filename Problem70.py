from collections import Counter


def Solve(limit=10**7, verbose=False):

    phi = []
    nonCoPrime = [[] for x in range(limit)]
    for currentNumber, currentList in  enumerate(nonCoPrime):
        if verbose: print(currentNumber)
        if currentNumber > 1:
            currNumberIsPrime = len(currentList)==0
            currentList.append([currentNumber, currNumberIsPrime])
            for ncpNumber in currentList:
                if ncpNumber[1]:
                    for futureNumber in range(currentNumber+ncpNumber[0], limit, ncpNumber[0]):
                        nonCoPrime[futureNumber].append([currentNumber, currNumberIsPrime])
        phi.append(currentNumber - len(currentList))

    ratios = []
    for ind in range(limit):
        xSet = sorted(str(ind))
        xPhiSet = sorted(str(phi[ind]))
        if xSet == xPhiSet and ind > 1:
            ratios.append(ind/phi[ind])
        else:
            ratios.append(float('inf'))

    minRatio = min(ratios)
    minN = ratios.index(minRatio)

    print(minN, phi[minN])
    return minN


def Solve1(limit=10**7, verbose=False):

    coPrimePairs = [(1,2),(1,3)]

    # generate odd/even and even/odd pairs
    ind = 0
    while ind < len(coPrimePairs):
        m = coPrimePairs[ind][1]
        n = coPrimePairs[ind][0]
        temp = []
        temp.append((m, 2*m-n))
        temp.append((m, 2*m+n))
        temp.append((n, m+2*n))
        for pair in temp:
            if pair[1] < limit:
                coPrimePairs.append(pair)
        ind += 1

    if verbose: print(coPrimePairs)
    return 0


def Solve2(limit=10**7, verbose=False):

    minRatio = float('inf')

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
            if verbose: print(n)
            if n/tot < minRatio:
                minRatio = n/tot
                minN = n

    return minN


if __name__=='__main__':
    import cProfile
    cProfile.run('print(Solve(10**4))')
    # print(Solve())

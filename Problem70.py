def Solve(limit=10**7, verbose=False):

    composites = {}

    minRatio = float('inf')
    minN = 0

    for n in range(2, limit):
        if n not in composites:
            composites[n] = [n]
        for p in composites[n]:
            composites.setdefault(p + n, []).append(p)

        totient = n
        for x in composites[n]:
            totient //= x
            totient *= (x-1)

        if (sorted([c for c in str(totient)]) == sorted([c for c in str(n)])):
            if (minRatio > (n / totient)):
                if verbose:
                    print(n, totient)
                minRatio = n / totient
                minN = n

        del composites[n]

    return minN

if __name__=='__main__':
    import cProfile
    limit = 10**7
    # Solve(10**3)
    # for i in range(1, 8):
    #     print("i equal " + str(i))
    #     cProfile.run('Solve(10**' + str(i) +')', sort='cumtime')
    # print(Solve(10**7, True))
    cProfile.run('Solve(' + str(limit) + ',True)', sort='cumtime')

def Solve(limit=10**7, verbose=False):

    composites = {}

    count = 0

    for n in range(2, limit+1):
        if n not in composites:
            composites[n] = [n]
        for p in composites[n]:
            composites.setdefault(p + n, []).append(p)

        totient = n
        for x in composites[n]:
            totient //= x
            totient *= (x-1)

        count += totient

        del composites[n]

    return count

if __name__=='__main__':
    import cProfile
    # limit = 8
    limit = 10 ** 6
    verbose = False
    cProfile.run('print(Solve(' + str(limit) + ',' + str(verbose) + '))')
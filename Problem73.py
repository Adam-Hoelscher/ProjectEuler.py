from Functions import GCD
from math import ceil

def Solve(limit=12000, verbose=False):

    count = 0

    for d in range(2, limit+1):
        if verbose and not d % 100: print(d)
        low = d//3 + 1
        high = ceil(d/2)
        for n in range(low, high):
            if GCD(n, d) == 1:
                if verbose: print(n,d)
                count += 1

    return count

def Solve2(limit=12000, verbose=False):

    composites = {}

    count = 0

    for n in range(2, limit+1):
        if n not in composites:
            composites[n] = [n]
        for p in composites[n]:
            composites.setdefault(p + n, []).append(p)

        adj = 0

        totient = n
        for x in composites[n]:
            totient //= x
            totient *= (x-1)
            if n//3 + 1 > x or x > ceil(n/2):
                adj += 1

        count += totient - adj

        del composites[n]

    return count

if __name__=='__main__':
    import cProfile
    limit = 12000
    limit = 8
    verbose = True
    verbose = False
    cProfile.run('print(Solve2(' + str(limit) + ',' + str(verbose) + '))')
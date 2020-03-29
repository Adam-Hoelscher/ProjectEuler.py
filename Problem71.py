from fractions import Fraction

def Solve(limit=10**6, verbose=False):

    maxFraction = Fraction(0,1)

    for d in range(2, limit+1):
        if d % 7 != 0:
            n = int(d*3/7)
            f = Fraction(n, d)
            if verbose: print(f)
            if f > maxFraction:
                maxFraction = f

    return maxFraction.numerator

if __name__ == '__main__':
    print(Solve())
    import cProfile
    limit = 10 ** 6
    verbose = False
    cProfile.run('Solve(' + str(limit) + ',' + str(verbose) + ')')

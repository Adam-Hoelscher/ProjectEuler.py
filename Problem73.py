from Functions import GCD
from fractions import Fraction

def Solve(limit=12000, verbose=False):

    count = 0
    band = set()

    for d in range(2, limit+1):
        if verbose: print(d)
        low = d//3
        high = d//2 + 1
        for n in range(low, high):
            f = Fraction(n, d)
            if Fraction(1,3) < f < Fraction(1,2):
                band.add(f)


    return len(band)

if __name__=='__main__':
    import cProfile
    limit = 12000
    # limit = 8
    verbose = True
    # verbose = False
    cProfile.run('print(Solve(' + str(limit) + ',' + str(verbose) + '))')
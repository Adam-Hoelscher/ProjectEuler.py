from fractions import Fraction
from collections import Counter

def Solve():

    prod = Fraction(1)

    for n in range(1, 10):
        for d in range(n+1, 10):
            f = 9 * n * d / (10 * n - d)
            if int(f) == f and f < 10:
                f = int(f)
                print (f, n, d, str(10 * n + f) + '/' + str(d + 10 * f), str(n) + '/' + str(d))
                prod *= Fraction(n,d)

    return(prod.denominator)

def Solve2():

    prod = Fraction(1)
    for d in set(range(1,100)) - set(range(0,100,10)):
        for n in set(range(1,d)) - set(range(0,100,10)):
                f1 = Fraction(n, d)
                n_set = Counter([int(x) for x in str(n)])
                d_set = Counter([int(x) for x in str(d)])
                try:
                    n2 = [x for x in (n_set - d_set)][0]
                    d2 = [x for x in (d_set - n_set)][0]
                    n_diff = n_set - Counter([n2])
                    d_diff = d_set - Counter([d2])
                    f2 = Fraction(n2, d2)
                    if n_diff == d_diff and len(n_diff) != 0 and f1 == f2:
                        prod *= f1
                except:
                    pass

    return(prod.denominator)

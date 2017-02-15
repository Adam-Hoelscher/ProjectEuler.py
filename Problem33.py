from fractions import Fraction

def Solve():
    pec = Fraction(1)
    for d in range(1,100):
        for n in range(1,d):
            f1 = Fraction(n, d)
            n_set = set([int(x) for x in str(n)])
            d_set = set([int(x) for x in str(d)])
            n2 = [x for x in set(n_set) - set(d_set)]
            d2 = [x for x in set(d_set) - set(n_set)]
            if len(n2) == len(d2) == 1 and
                  d2[0] != 0 and
                  n2[0] != n:
                f2 = Fraction(n2[0], d2[0])
                if f1 == f2:
                    print(n, d)
                    pec *= f1

    return(pec.denominator)
    
            
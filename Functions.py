def IsPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    f = 3
    while f < 1 + n ** .5:
        if n % f == 0:
            return False
        else:
            f += 2
    return True

def PrimeFactors(n, self = True, unique = False):

    factors = dict()
    f = 2
    while n > 1:
        while n % f == 0:
            try:
                if not unique:
                    factors[f] += 1
                else:
                    factors[f] = 1
            except:
                factors[f] = 1
            n /= f
        f += 1
        if f**2 > n:
            if n > 1 and self: factors[f] = 1
            break
    return factors

def Factors(x):
    from math import sqrt, ceil
    facs = []
    for n in range(1, ceil(sqrt(x))):
        if x % n == 0:
            facs.append(n)
    for fac in facs[1:][::-1]:
        facs.append(x // fac)
    if abs(sqrt(x) - round(sqrt(x))) < 1e-6:
        facs.append(round(sqrt(x)))
    return facs

def IsPanDig(x, end = 9, begin = 1):
    temp = [str(y) for y in str(x)]
    temp.sort()
    return temp == [str(y) for y in range(begin, end + 1)]

def GCD(x, y = None):

    if not hasattr(x, "__iter__"):
        x = [x]
    if not hasattr(y, "__iter__"):
        y = [y]

    x = [*x, *y]
    x = [z for z in x if z != None]

    def GCDpair(x,y):
        if x == 0:
            return(y)
        else:
            return(GCDpair(y % x,x))

    if len(x) == 1:
        return(x)
    elif len(x) == 2:
        return(GCDpair(x[0],x[1]))
    else:
        return(GCDpair(x[0],GCD(x[1:])))

def LCM(x, y = None):

    if not hasattr(x, "__iter__"):
        x = [x]
    if not hasattr(y, "__iter__"):
        y = [y]

    x = [*x, *y]
    x = [z for z in x if z != None]

    def LCMpair(x,y):
        return(x // GCD(x,y) * y)

    if len(x) == 1:
        return(x)
    elif len(x) == 2:
        return(LCMpair(x[0],x[1]))
    else:
        return(LCMpair(x[0],LCM(x[1:])))

def PrimeSieve(n):

    primes = dict()
    for i in range(2, n):
        try:
            primes[i]
        except:
            primes[i] = True
            factors = range(i, n, i)
            for f in factors[1:]:
                primes[f] = False

    return [i for i in primes if primes[i] == True]

def IsPrime(n):
    if n < 3:
        return(False)
    if (n % 2 == 0):
        return(False)
    f = 3
    while (f < 1 + n ** .5):
        if (n % f == 0):
            return(False)
        else:
            f += 2
    return(True)

def PrimeFactors(n, self = True):
    p = n
    temp = {}

    if p == 1: return(temp)
    if p == 2:
        temp[2] = 1
        return(temp)

    f = 2
    while (n % f == 0):
        n //= f
        try:
            temp[f] += 1
        except:
            temp[f] = 1

    f = 3
    while (n > 1):
        while (n % f == 0):
            n //= f
            try:
                temp[f] += 1
            except:
                if (p != f or self):
                    temp[f] = 1
        f += 2


    return(temp)

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

def IsPanDig(x, base = 9):
    temp = [str(y) for y in str(x)]
    temp.sort()
    return(temp == [str(y) for y in range(1, base + 1)])

def IsPrime(n):
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

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

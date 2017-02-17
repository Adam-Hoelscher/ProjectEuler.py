from Functions import IsPrime

def Solve():

    TruncPrimes = []

    def left(n):
        while len(str(n)) > 1:
            if not IsPrime(n):
                return(False)
            n = int(str(n)[1:])
        return(IsPrime(n))

    def right(n):
        while len(str(n)) > 1:
            if not IsPrime(n):
                return(False)
            n = int(str(n)[:-1])
        return(IsPrime(n))

    n = 11
    while len(TruncPrimes) < 11:
        if left(n) and right(n):
            TruncPrimes += [n]
        n += 2

    return(sum(TruncPrimes))
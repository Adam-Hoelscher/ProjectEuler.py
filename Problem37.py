from Functions import IsPrime

def Solve():

    TruncPrimes = []

    def Possible(n):
        digs = [int(x) for x in str(n)[1:]]
        evens = [z for z in digs if z % 2 == 0]
        if len(evens) > 0:
            return(False)
        elif 5 in digs:
            return(False)
        return(True)

    def left(n):
        while len(str(n)) > 1:
            if n in TruncPrimes:
                return True
            if not IsPrime(n):
                return(False)
            n = int(str(n)[1:])
        return(IsPrime(n))

    def right(n):
        while len(str(n)) > 1:
            if n in TruncPrimes:
                return True
            if not IsPrime(n):
                return(False)
            n = int(str(n)[:-1])
        return(IsPrime(n))

    n = 21
    while len(TruncPrimes) < 11:
        if Possible(n):
            if left(n) and right(n):
                TruncPrimes += [n]
        n += 2

    return(sum(TruncPrimes))

if __name__ == '__main__':
    print(Solve())
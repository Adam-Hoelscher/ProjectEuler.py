from Functions import IsPanDig, PrimeSieve

def Solve():

    primes = PrimeSieve(987654321)[::-1]

    for i in primes:
    #for i in range(987654321, 0, -1):
        if IsPanDig(i):
            return(i)
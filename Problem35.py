from Functions import PrimeSieve

def Solve():

    limit = 1000000
    primes = PrimeSieve(limit)
    CircPrimes = []

    for n in [x for x in primes]:
        if n >= 10:
            digs = [int(x) for x in str(n)]
            evens = [z for z in digs if z % 2 == 0]
            if len(evens) > 0:
                primes.remove(n)
            elif 5 in digs:
                primes.remove(n)

    def rotate(n):
        z = [x for x in str(n)]
        z = z[1:] + [z[0]]
        return(int(''.join(z)))

    for i in [x for x in primes]:
        n = i
        if i in primes:
            temp = []
            while n in primes:
                primes.remove(n)
                temp.append(n)
                n = rotate(n)
            if n == i:
                CircPrimes = CircPrimes + temp

    return(len(CircPrimes))

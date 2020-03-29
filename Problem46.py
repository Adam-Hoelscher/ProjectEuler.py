from Functions import IsPrime

def Solve():

    primes = set([2])

    n = 1
    while True:
        n += 2
        if IsPrime(n):
            primes.add(n)
        else:
            stop = True
            for p in primes:
                diff = n - p
                if ((diff/2)**.5).is_integer():
                    stop = False
                    break
            if stop:
                return(n)


if __name__ == '__main__':
    print(Solve())

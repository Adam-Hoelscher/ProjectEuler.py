from Functions import PrimeSieve

def Solve():

    limit = 1000000
    primes = set(PrimeSieve(limit))
    CircPrimes = set()

    for n in set(primes):
        if n >= 10:
            digits = set(int(x) for x in str(n))
            if digits.intersection(range(0, 10, 2)):
                primes.remove(n)
            elif 5 in digits:
                primes.remove(n)

    def rotate(n):
        z = list(str(n))
        z = z[1:] + z[:1]
        return(int(''.join(z)))

    for i in primes:

        if i in CircPrimes:
            continue

        else:

            n = i
            temp = set()

            while n not in temp:

                if n not in primes:
                    break
                else:
                    temp.add(n)
                    n = rotate(n)

            else:
                CircPrimes.update(temp)

    return(len(CircPrimes))


if __name__ == '__main__':
    print(Solve())

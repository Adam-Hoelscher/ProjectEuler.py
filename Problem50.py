from Functions import PrimeSieve

def Solve():

    limit = 1000000
    primes = [x for x in PrimeSieve(limit)]
    maxLength = 1
    maxPrime = 2

    for i in range(0,len(primes)-1):
        length = maxLength
        if i+length > len(primes): break
        sumPrime = sum(primes[i:i + length])
        while sumPrime < limit:
            if sumPrime in primes:
                maxLength = length
                maxPrime = sumPrime
            sumPrime += primes[i+length]
            length += 1

    return(maxPrime)


if __name__ == '__main__':
    print(Solve())

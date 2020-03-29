from Functions import IsPrime

def Solve():
    primes = [2]
    test = 1
    while len(primes) <= 10_000:
        test += 2
        if IsPrime(test):
            primes.append(test)
    return test


if __name__ == '__main__':
    print(Solve())

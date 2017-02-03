from Functions import IsPrime

def Solve():
    primes = [2]
    test = 1
    while len(primes) < 10001:
        test += 2
        #print(test, Functions.IsPrime(test))
        if IsPrime(test):
            primes.append(test)
    return(test)
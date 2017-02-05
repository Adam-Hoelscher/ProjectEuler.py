from Functions import IsPrime

def Solve():
    return(2 + sum (i for i in range(3,2000000,2) if IsPrime(i)))

from Functions import IsPrime

def Solve():
    
    def PrimeCount(a,b):
        n = 0
        def f(n): return(n**2 + a*n + b)
        while IsPrime(f(n)): n += 1
        return(n)
    
    Counts = dict(
            [(PrimeCount(a,b), a*b)
            for a in range(-999, -1, 2)
            for b in [p for p in range(1, 999, 2) if IsPrime(p)]]
            )
    
    return(Counts[max(Counts.keys())])
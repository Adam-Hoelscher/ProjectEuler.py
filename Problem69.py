from Functions import GCD, IsPrime, PrimeSieve

def Solve(limit=1_000_000):

    prime = PrimeSieve(valLimit=limit)
    prod = 1
    while prod < limit:
        p = next(prime)
        prod *= p

    prod = prod // p
    return prod


def Solve2():

    limit = 10000
    composites = [x for x in range(2,limit) if not IsPrime(x)]

    def totient(x):
        return len([p for p in range(1, x) if GCD(x,p) == 1])

    ratios = [y/totient(y) for y in composites]
    m = max(ratios)
    return(composites[ratios.index(m)])


if __name__ == '__main__':
    print(Solve())

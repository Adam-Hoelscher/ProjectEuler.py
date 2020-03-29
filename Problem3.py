from Functions import PrimeSieve

def Solve(p=600851475143):
    prime = PrimeSieve()
    f = next(prime)
    while not p == 1:
        if p % f == 0:
            p = p / f
        else:
            f = next(prime)
    return f


if __name__ == '__main__':
    print(Solve())

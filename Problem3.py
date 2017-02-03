def Solve():
    p = 600851475143
    f = 2
    while (p != 1):
        if (p % f == 0):
            p = p / f
        else:
            f += 1
    return(f)
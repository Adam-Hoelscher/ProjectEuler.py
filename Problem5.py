def Solve():
    p = 1
    for c in range(1, 21):
        i = p
        while (p % c != 0):
            p += i
    return(p)
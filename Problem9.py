def Solve():
    stop = False
    for c in range(1000,1,-1):
        for b in range(999-c, 1,-1):
            a = 1000 - b - c
            stop = c**2 == a**2 + b**2
            if stop: break
        if stop: break
    return(a*b*c)
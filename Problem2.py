def Solve():
    temp = 0
    a = 1
    f = 1
    while (f < 4000000):
        if (f%2 == 0): temp += f
        f, a = f + a, f
    return(temp)

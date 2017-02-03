def Solve():
    t1 = t2 = 0
    for i in range(101):
        t1 += i
        t2 += i ** 2
    return(t1**2 - t2)
def Solve():
    j = set()
    for a in range(2, 101):
        for b in range(2, 101):
            j.add(a**b)
    return(len(j))
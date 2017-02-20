from math import log

def Solve():

    n = 3
    d = 2
    count = 0

    for x in range(1000):
        n0 = n
        d0 = d
        n = n0 + d0 * 2
        d = n0 + d0
        if int(log(n,10)) > int(log(d,10)):
            count += 1

    return count

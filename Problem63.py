from math import log

def Solve():

    limit = 1
    while log(9 ** limit, 10) >= limit - 1:
        limit += 1

    count = 0
    for n in range(1,10):
        for e in range(1, limit):
            test = n ** e
            if int(1 + log(test, 10)) == e:
                count += 1

    return count
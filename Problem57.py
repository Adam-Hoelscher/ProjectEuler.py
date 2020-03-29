from math import log

def Solve():

    n = 3
    d = 2
    count = 0

    for x in range(1_000):
        n, d = n + d * 2, n + d
        if int(log(n,10)) > int(log(d,10)):
            count += 1

    return count


if __name__ == '__main__':
    print(Solve())

from collections import Counter

limit = 61

def Solve():

    # limit = 10
    # limit = 7

    maxD = 0
    maxX = 0

    def fD(x, y):
        return int(x**2 - d * y**2 - 1)

    r = 0
    squares = set([x**2 for x in range(1, 1+int(limit**.5))])

    y = 2
    for d in range(2, limit+1):

        if sum([d + x in squares for x in [-2, 0, 2]]):
        # if d in squares:
            continue

        x = .5
        y = 0
        while not x == int(x):
            y += 1
            x = (1 + d * y ** 2) ** .5

        # print(d, int(x))
        if x > maxX:
            maxX = int(x)
            maxD = d

    return(maxD)


def Solve2():

    # limit = 10
    # limit = 7

    maxD = 0
    maxX = 0

    def fD(x, y):
        return int(x**2 - d * y**2 - 1)

    r = 0
    squares = set([x**2 for x in range(1, 1+int(limit**.5))])

    y = 2
    for d in range(2, limit+1):

        if sum([d + x in squares for x in [-2, 0, 2]]):
            continue

        x = 0
        y = 1
        f = fD(x, y)
        while f:
            if f < 0:
                x += 1
            else:
                y += 1
            f = fD(x, y)

        # print(d, int(x))
        if x > maxX:
            maxX = int(x)
            maxD = d

    return(maxD)


def Solve3():

    # limit = 100
    leastX = Counter()
    stopLength = limit - int(limit ** .5)

    x = 1
    while len(leastX) < stopLength:
        x += 1
        lowY = int(max(((x**2 - 1)/limit)**.5, 1))
        if (x+lowY)%2 == 0:
            lowY += 1
        for y in range(lowY, x, 2):
            d = (x**2-1)/(y**2)
            if int(d) == d <= limit and not d in leastX.keys():
                d = int(d)
                for f in range(1, int(d**.5)+1):
                    if d % (f**2) == 0:
                        leastX[d//(f**2)] = x
                        # print(x, '^2 - ', d//(f**2), '*', y, '^2 = 1', sep='')
                break

    return leastX.most_common(1)[0][0]


def Solve4():

    maxD = 0
    maxX = 0

    def stepGen(d):
        mods = [x**2 % d for x in range(d)][::-1]
        cycle = []
        step = 0
        while len(mods):
            if mods.pop() == 1:
                cycle.append(step)
                step = 0
            step += 1
        yield cycle[0]
        cycle[0] += step
        while True:
            cycle = cycle[1:] + [cycle[0]]
            yield cycle[0]

    squares = set([x**2 for x in range(1, 1+int(limit**.5))])

    for d in range(2, limit + 1):

        if sum([d + x in squares for x in [-2, 0, 2]]):
            continue

        x_step = stepGen(d)
        x = x_step.__next__() #burn the first step, so that y != 0

        while True:
            x += x_step.__next__()
            y = ((x**2-1)/d)**.5
            if y.is_integer():
                # print(d, x)
                if x > maxX:
                    maxX = x
                    maxD = d
                break

    return(maxD)


if __name__=='__main__':
    from time import clock
    s = clock()
    print(Solve(), clock() - s)
    s = clock()
    print(Solve4(), clock() - s)

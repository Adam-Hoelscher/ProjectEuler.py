def Solve():

    limit = 1000
    # limit = 7

    maxD = 0
    maxX = 0

    def fD(x, y):
        return int(x**2 - d * y**2 - 1)

    y = 2
    for d in range(2, limit+1):

        if int(d**.5) == d**.5:
            continue

        x = .5
        y = 0
        while not x == int(x):
            y += 1
            x = (1 + d * y ** 2)**.5

        if x > maxX:
            maxX = int(x)
            maxD = d

        print(d, x)

    return(maxD)



if __name__=='__main__':
    from time import clock
    s = clock()
    print(Solve(), clock() - s)
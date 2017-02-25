def Solve():

    limit = 10000

    def nextFraction(s, a = 0, b = 1):

        a, b = -a, int((s-a**2)/b)
        i = int((s ** .5 + a)/b)
        a -= i * b

        return [i, a, b]

    def findPeriod(n):
        root = n ** .5
        i = int(root)
        a = -i
        b = 1
        fraction = [[i, a, b]]
        while True:
            next = nextFraction(n, a, b)
            a = next[1]
            b = next[2]
            if  b == 0:
                return 0
            for i, f in enumerate(fraction[::-1]):
                if f == next:
                    return (i+1)
            fraction.append(next)

    return sum([(findPeriod(x) % 2) for x in [n for n in range(2, limit + 1) if not n**.5 == int(n**.5)]])


if __name__=='__main__':
    from time import clock
    s = clock()
    print(Solve(), clock() - s)
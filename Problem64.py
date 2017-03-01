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
        fraction = []
        next = [i, -i, 1]
        while True:
            fraction.append(next)
            next = nextFraction(n, *next[1:])
            if  next[2] == 0:
                return 0
            for i, f in enumerate(fraction[::-1]):
                if f == next:
                    return (i+1)

    return sum([(findPeriod(x) % 2) for x in [n for n in range(2, limit + 1) if not (n**.5).is_integer()]])


if __name__=='__main__':
    from time import clock
    s = clock()
    print(Solve(), clock() - s)
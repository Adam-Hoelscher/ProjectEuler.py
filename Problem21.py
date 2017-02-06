def Solve():

    temp = 0

    def factors(x):
        f = [1]
        for d in range(2, int(x**.5)):
            if x%d == 0:
                f.append(d)
                f.append(x//d)
        return(f)

    def d(n):
        return(sum(factors(n)))

    def a(n):
        test = d(n)
        return(n == d(test) and n != test)

    temp = sum([x for x in range(10000) if a(x)])

    return(temp)

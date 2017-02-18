def Solve():

    def Pent(n):
        return(n*(3*n-1)//2)

    def IsPent(p):
        n = (0.5 + (0.25 + 6 * p)**0.5)/3
        return(n.is_integer())

    PentNums = set()

    k = 1
    while True:
        Pk = Pent(k)
        for Pa in PentNums:
            Pj = Pk - Pa
            Pz = Pj + Pk
            if Pj in PentNums and IsPent(Pz):
                return(Pk-Pj)
        PentNums.add(Pk)
        k += 1

def Solve2():

    return('This function is too slow. Use Solve()')

    def Pent(n):
        return(n*(3*n-1)//2)

    def IsPent(p):
        n = (0.5 + (0.25 + 6 * p)**0.5)/3
        return(n.is_integer())

    PentNums = set()

    j = 1
    while True:
        Pj = Pent(j)
        for Pa in PentNums:
            Pk = Pj + Pa
            Pz = Pj + Pk
            if IsPent(Pk) and IsPent(Pz):
                return(Pk-Pj)
        PentNums.add(Pj)
        j += 1

def Solve3():
    import itertools

    pentagonals = set()

    def pentagonal_number(x):
        # Return the pentagonal number Px
        return x * ((3 * x) - 1) / 2

    def is_pentagonal(x):
        # Check if x is pentagonal
        return ((0.5 + (0.25 + (6 * x)) ** 0.5) / 3).is_integer()

    def check(x, y):
        return is_pentagonal(x + y) and (x - y) in pentagonals

    for n in itertools.count():
        a = pentagonal_number(n)
        for p in pentagonals:
            if check(a, p):
                return(a - p)
        else:
            pentagonals.add(a)
            continue  # Continue if the inner loop didn't end prematurely
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


if __name__ == '__main__':
    print(Solve())
    import cProfile
    cProfile.run('print(Solve())')

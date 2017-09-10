def Solve():

    def IsTri(t):
        n = -.5+(.25+2*t)**.5
        return (n.is_integer())

    def IsPent(p):
        n = (0.5+(0.25+6*p)**0.5)/3
        return(n.is_integer())

    def Hex(n):
        return(n*(2*n-1))

    n = 1
    # loop through the Hex numbers. They're more sparse
    while True:
        n += 1
        h = Hex(n)
        if IsTri(h) and IsPent(h) and h != 40755:
            return(h)

if __name__ == '__main__':
    import cProfile
    cProfile.run('Solve()')

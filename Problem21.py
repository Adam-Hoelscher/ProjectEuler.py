from Functions import Factors

def Solve():

    temp = 0

    def d(n):
        return(sum(Factors(n)))

    def a(n):
        test = d(n)
        return(n == d(test) and n != test)

    temp = sum([x for x in range(10000) if a(x)])

    return(temp)

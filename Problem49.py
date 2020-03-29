from Functions import IsPrime

def Solve():

    beg = 1489

    while beg < 10000:
        then = beg + 3330
        end = then + 3330
        if set([x for x in str(beg)]) == set([x for x in str(then)]) == set([x for x in str(end)]):
            if IsPrime(beg) and IsPrime(then) and IsPrime(end):
                return(int(str(beg) + str(then) + str(end)))
        beg += 2


if __name__ == '__main__':
    print(Solve())

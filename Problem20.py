from math import factorial as fact

def Solve():
    return(sum([int(x) for x in str(fact(100))]))


if __name__ == '__main__':
    print(Solve())

def Solve():
    temp = 2**1000
    temp = sum([int(x) for x in str(temp)])
    return(temp)


if __name__ == '__main__':
    print(Solve())

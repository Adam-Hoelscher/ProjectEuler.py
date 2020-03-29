def Solve():

    temp = [n ** n for n in range(1,1001)]
    return(str(sum(temp))[-10:])


if __name__ == '__main__':
    print(Solve())

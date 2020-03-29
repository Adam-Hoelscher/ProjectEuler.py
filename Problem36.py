def Solve():

    temp = 0

    for x in range(1, 1000000, 2):
        if str(x) == str(x)[::-1]:
            b = bin(x)[2:]
            if b == b[::-1]:
                temp += x

    return(temp)


if __name__ == '__main__':
    print(Solve())

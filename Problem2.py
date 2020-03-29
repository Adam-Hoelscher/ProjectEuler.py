def Solve():
    temp = 0
    a, b =  1, 2
    while b < 4_000_000:
        temp += b
        for i in range(3):
            a, b = b, a + b
    return temp


if __name__ == '__main__':
    print(Solve())

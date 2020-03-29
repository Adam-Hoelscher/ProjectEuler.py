def Solve():
    temp = 0
    for x in range(999, 99, -1):
        for y in range(990, 99, -11):
            test = x*y
            if (test > temp):
                string = str(test)
                if (string==string[::-1]):
                    temp = test


if __name__ == '__main__':
    print(Solve())

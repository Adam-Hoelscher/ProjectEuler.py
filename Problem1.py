def Solve():
    return sum(x for x in range(1_000) if x % 3 == 0 or x % 5 == 0)


if __name__ == '__main__':
    print(Solve())

def Solve():
    p = 1
    for c in range(1, 21):
        i = p
        while p % c:
            p += i
    return p


if __name__ == '__main__':
    print(Solve())

def Solve():
    p = 1
    for c in range(1, 21):
        i = p
        while (p % c != 0):
            p += i
    return(p)

def Solve2():
    from Functions import LCM
    return(LCM(range(1,21)))

if __name__ == '__main__':
    print(Solve())

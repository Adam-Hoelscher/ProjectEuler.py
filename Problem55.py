def Solve():
    count = 0
    for n in range(1,10000):
        for i in range(50):
            n += int(str(n)[::-1])
            if str(n) == str(n)[::-1]:
                break
            elif i == 49:
                count += 1
    return count
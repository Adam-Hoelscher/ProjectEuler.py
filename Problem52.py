def Solve():

    add = 0
    target = 6

    while True:
        baseDigits = ['1'] + [d for d in str(add)]
        test = int(''.join(baseDigits))
        baseDigits.sort()
        for m in range(2, target + 1):
            mult = test * m
            testDigits = [d for d in str(mult)]
            testDigits.sort()
            if baseDigits != testDigits:
                break
            elif m == target:
                return(test)


        add += 1
def Solve():
    digits = '0'
    i = 0
    temp = 1
    while len(digits) <= 1000000:
        i += 1
        digits += str(i)
    for p in range(7):
        temp *= int(digits[10**p])
    return(temp)

    
if __name__ == '__main__':
    print(Solve())

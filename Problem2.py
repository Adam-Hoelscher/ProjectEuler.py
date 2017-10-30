def Solve():
    temp = 0
    fib = (1,2)
    while (fib[1] < 4000000):
        temp += fib[1]
        for i in range(3):
            fib = (fib[1], fib[0]+fib[1])
    return(temp)

if __name__ == '__main__':
    print(Solve())
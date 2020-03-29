def Solve():
    
    p = 5
    
    def s(x):
        return(x == sum([int(d)**p for d in str(x)]))
    
    d = 1
    while d*(9**p) > int(d*'9'): d += 1

    return(sum([l for l in range(2,int(d*'9')+1) if s(l)]))


if __name__ == '__main__':
    print(Solve())

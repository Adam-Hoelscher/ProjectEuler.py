from  math import factorial as Fact

def Solve():
    
    n = 1000000
    d = list(range(10))
#    n = 3
#    d = list(range(3))
    temp = str()
    
    n -= 1
    while len(d) > 0:

        f = Fact(len(d)-1)
        t = n//f
        n = n%f

        temp += str(d[t])
        d = d[:t]+d[t+1:]
    
    return (temp)


if __name__ == '__main__':
    print(Solve())

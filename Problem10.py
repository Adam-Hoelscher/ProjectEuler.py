from Functions import IsPrime

def Solve():

    max = 2000000
    temp = {n:True for n in range(2,max)}
    for n in temp.keys():
        if temp[n]:
            for k in range(2*n, max, n):
                temp[k] = False
    return(sum(x for x in temp if temp[x]))


if __name__ == '__main__':
    print(Solve())

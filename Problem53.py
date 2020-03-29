from math import factorial

def Solve():

    target = 1000000
    count = 0

    def nCr(n,r):
        return factorial(n)//(factorial(r)*factorial(n-r))

    for n in range(23, 101):
        for r in range(int(n/2),0,-1):
            length = nCr(n,r)
            if length > target:
                count += 2
                if r == n/2:
                    count -= 1
            else:
                break

    return count

    
if __name__ == '__main__':
    print(Solve())

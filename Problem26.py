from math import log

def Solve():
    
    def RepLen(x):
        c = 1
        l = 0
        r = dict()
        while True:
            l += 1
            c = c % x
            try:
                return(l - r[c])
            except:
                r[c] = l
            c *= 10
    
    digits = [RepLen(x) for x in range(1,1000)]
    return(digits.index(max(digits))+1)
    
    
if __name__ == '__main__':
    print(Solve())
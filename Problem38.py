from Functions import IsPanDig
from collections import Counter

def Solve():

    result = 0

    def UniqDigits(n):
        x = Counter([y for y in str(n)])
        return(max(x.values()) == 1)

    for n in range(9876 + 1):
        if UniqDigits(n):
            temp = str(n)
            m = 1
            while len(temp) < 9:
                m += 1
                temp += str(n*m)
                if not UniqDigits(temp):
                    break
            if IsPanDig(temp) and n > 1:
                result = max(int(temp), result)

    return(result)

    
if __name__ == '__main__':
    print(Solve())

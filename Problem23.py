from Functions import Factors
          
def Solve():
    
    lim = 28123
    Abundant = [n for n in range(1, lim) if sum(Factors(n)) > n]
    s = (num + n for i, num in enumerate(Abundant) for n in Abundant[i:])
    s = set(n for n in set(s) if n <= lim)
    return(sum(set(range(1, lim + 1)) - s))
      
def Solve2():
    
    Abundant = [x for x in range(1,28123) if (sum(Factors(x)) > x)]

    SumsOfAbundant = set()
    
    for x in range(len(Abundant)):
        for y in range(x, len(Abundant)):
            SumsOfAbundant.add(Abundant[x] + Abundant[y])

    temp = set(range(28123)) - SumsOfAbundant
    return(sum(temp))

def Solve3():
    
    Abundant = [x for x in range(1,28123) if (sum(Factors(x)) > x)]

    def IsSumOfAbundant(x):
        l = 0
        r = len(Abundant) - 1
        while (l <= r):
            if Abundant[l] + Abundant[r] > x:
                r -= 1
            elif Abundant[l] + Abundant[r] < x:
                l += 1
            else:
                return(True)
        return(False)
    
    temp = [x for x in range(28123) if not IsSumOfAbundant(x)]
    return(sum(temp))
                
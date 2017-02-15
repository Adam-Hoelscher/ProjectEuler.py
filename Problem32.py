from itertools import permutations as Perms
from Functions import IsPanDig

def Solve():
    
    combos = set()
    panProds = set()
    
    for p in Perms(range(1,10)):
        p = p[0:5]
        p = ''.join([str(y) for y in p])
        combos.add(p[0:5])

    for c in combos:
        for cut in range(1,3):
            left  = int(c[0:cut])
            right = int(c[cut:5])
            prod = int(left) * int(right)
            check = str(left) + str(right) + str(prod)
            if IsPanDig(check):
                panProds.add(prod)
                
    return(sum(panProds))
    
    
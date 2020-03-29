from itertools import permutations
from Functions import PrimeSieve

def Solve():

    primes = [x for x in PrimeSieve(18)][::-1]
    digits = set([str(x) for x in range(0,10)])

    candidates = []

    # find all possible combinations for last 3 digits
    for test in range(0, 1000, primes[0]):
        testStr = str(test).zfill(3)
        # test the digits directly rather using `set` object, massive speed difference
        # if len(set(d for d in testStr)) == len(testStr):
        if testStr[0] != testStr[1] != testStr[2] and testStr[0] != testStr[2]:
            candidates.append((testStr, digits - set([d for d in testStr])))

    for p in primes[1:]:
        nextCandidates = []
        for cand in candidates:
            for nextDig in cand[1]:
                testStr = nextDig + cand[0][:2]
                if int(testStr) % p == 0:
                    setDigits = nextDig + cand[0]
                    nextCandidates.append((setDigits, digits - set([d for d in setDigits])))
        candidates = nextCandidates[:]

    # convert the candidate values from strings to numbers
    candidates = [int(x[1].pop() + x[0]) for x in candidates]
    return(sum(candidates))

def Solve2():
    # found on forums
    i = 17
    vars = []
    ten = set(range(10))
    while i < 100:
        t = str(i)
        if t[0] != t[1] and t[1] != 0 and t[0] != 0:
            vars.append(['0' + t, ten - {0, int(t[0]), int(t[1])}])
        i += 17
    while i < 1000:
        t = str(i)
        if t[0] != t[1] and t[1] != t[2] and t[0] != t[2]:
            vars.append([t, ten - {int(t[0]), int(t[1]), int(t[2])}])
        i += 17
    for div in [13, 11, 7, 5, 3, 2]:
        tmp = []
        for var in vars:
            for a in var[1]:
                if int(str(a) + var[0][:2]) % div == 0:
                    tmp += [[str(a) + var[0], var[1] - {a}]]
        vars = tmp[:]
    return(sum([int(str([y for y in x[1]][0]) + x[0]) for x in vars]))

def Solve3():

    # my original algorithm. naive. VERY SLOW!
    numbers = permutations([x for x in range(0,10)])

    #exclude numbers starting in 0 and numbers which will not meet condition for 5
    numbers = [x for x in numbers if x[0] != 0 or x[5] != 0]

    primes = [x for x in PrimeSieve(18)]

    temp = 0
    for n in numbers:
        counter = 1
        while counter <= len(primes):
            test = int(''.join([str(x) for x in n[counter : counter + 3]]))
            if test % primes[counter - 1] != 0:
               break
            counter += 1
        if counter > len(primes):
            temp += int(''.join([str(x) for x in n]))

    return(temp)

    
if __name__ == '__main__':
    print(Solve())

from itertools import permutations
    

def Solve():

    size = 5

    maxStr = 0

    sumLines = []
    for i in range(size):
        sumLines.append([i, i+size, i+size+1])
    sumLines[size-1][2] = size

    allDigits = range(1,2*size+1)

    # the first digit cannot be any higher than 1 more than the size of ring.
    for first in range(size+1,0,-1):

        '''since we're searching from high to low, if we've found anything then it will be higher than anything we
        are yet to find'''
        if maxStr:
            break

        remain = set(range(first+1, 2*size+1)) - {first}

        for outerDigits in permutations(remain, size-1):

            if not max(allDigits) in outerDigits:
                continue

            for innerDigits in permutations(set(allDigits)-set(outerDigits)-{first}):

                perm = [first] + [x for x in outerDigits] + [y for y in innerDigits]

                total = 0
                found = True
                string = ''
                for line in sumLines:
                    check = sum([perm[x] for x in line])
                    if not total:
                        total = check
                    elif check != total:
                        found = False
                        break
                    string += ''.join([str(perm[x]) for x in line])
                if found:
                    if int(string) > int(maxStr):
                        # print(perm)
                        maxStr = int(string)

    return maxStr


def Solve1():

    '''first attempt. absolute brute force. took about 20 seconds to run.'''
    size = 5

    maxStr = '0'
    sets = []
    for i in range(size):
        sets.append([i, i+size, i+size+1])
    sets[size-1][2] = size
    for perm in permutations(range(1,2*size+1)):
        if min(perm[0:size]) != perm[0]:
            continue
        total = 0
        found = True
        string = ''
        for s in sets:
            check = sum([perm[x] for x in s])
            if not total:
                total = check
            elif check != total:
                found = False
                break
            string += ''.join([str(perm[x]) for x in s])
        if found:
            if int(string) > int(maxStr) and len(string) < 17:
                # print(perm)
                maxStr = string

    return maxStr



# if __name__=='__main__':
#     from time import clock
#     s = clock()
#     print(Solve(), clock()-s)

if __name__ == '__main__':
    import cProfile
    cProfile.run('Solve()')
    # cProfile.run('Solve1()')

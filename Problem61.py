def Solve():

    target = 6

    def FigNums(s):
        current = 1
        n = 1
        while current <= 9999:
            yield current
            n += 1
            current += (1+(n-1)*(s-2))

    FigurateNumbers = []
    for s in range(3, target+3):
        numbers = [x for x in FigNums(s) if x >= 1000]
        for n in numbers:
            FigurateNumbers.append({'n': n, 's': s, 'l': str(n)[0:2], 'r': str(n)[2:4]})

    depth = 0
    tree = [FigurateNumbers[:]]
    while 0 <= depth < target:
        if not len(tree[depth]):
            tree = tree[:-1]
            depth -= 1
            tree[depth] = tree[depth][1:]
            continue
        fNum = tree[depth][0]
        usedShapes = [x[0]['s'] for x in tree]
        notF = [x for x in FigurateNumbers if
                x['n'] != fNum['n'] and x['l'] == fNum['r'] and not x['s'] in usedShapes]
        if depth == target - 2:
            notF = [x for x in notF if x['r'] == tree[0][0]['l']]
        if len(notF):
            tree.append(notF)
            depth += 1
            if depth == target - 1:
                return sum([x[0]['n'] for x in tree])
        else:
            tree[depth] = tree[depth][1:]


if __name__ == '__main__':
    print(Solve())

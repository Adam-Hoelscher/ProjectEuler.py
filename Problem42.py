def Solve():

    file = open('C:/ProjectEuler/p042_words.txt')
    words = file.read()
    file.close()

    words = words.replace('"','')
    words = words.split(',')

    maxLen = max([len(y) for y in words])
    maxScore = maxLen * 26

    Triangles = [1]
    t = 1
    while max(Triangles) < maxScore:
        t += 1
        Triangles.append(max(Triangles) + t)

    count = 0
    for w in words:
        score = sum([ord(c) + 1 - ord('A') for c in w])
        if score in Triangles:
            count += 1

    return(count)

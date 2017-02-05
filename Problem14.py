def Solve():

    lengths = {}
    maxLen = 0
    maxKey = 0

    def Col(n):
        if n%2 == 0:
            return(n/2)
        else:
            return(3*n + 1)

    for i in range(1, 1000000):
        n = i
        count = 0
        stop = False
        while (n != 1):
            try:
                count += lengths[n]
                break
            except:
                n = Col(n)
                count += 1
        lengths[i] = count
        if count > maxLen:
            maxLen = count
            maxKey = i

    return(maxKey)

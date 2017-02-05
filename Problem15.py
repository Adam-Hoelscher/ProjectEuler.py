def Solve():
    temp = [[0 for x in range(21)] for y in range(21)]
    for x in range(21):
        for y in range(21):
            try:
                left = temp[x-1][y  ]
            except:
                left = 0
            try:
                top  = temp[x  ][y-1]
            except:
                top  = 0
            if (x == y == 0):
                temp[0][0] = 1
            else:
                temp[x][y] = left + top
    return(temp[x][y])

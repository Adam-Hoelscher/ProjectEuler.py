def Solve():
    pos   = 1
    temp  = 1
    width = 2
    while width <= 1001:
        for i in range(4):
            pos += width
            temp += pos
        width += 2

    return(temp)
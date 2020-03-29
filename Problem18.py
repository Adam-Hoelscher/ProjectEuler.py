def Solve():

    file = open('C:/ProjectEuler/p018_triangle.txt', 'r')
    data = file.read()
    file.close()

    data = data.split('\n')
    data = [x.split(' ') for x in data[:-1]]
    data = [[int(y) for y in x] for x in data]

    for r in range(len(data)-1, 0, -1):
        for c in range(r, 0, -1):
            left  = data[r][c-1]
            right = data[r][c]
            add   = max(left, right)
            data[r-1][c-1] += add

    return (int(data[0][0]))


if __name__ == '__main__':
    print(Solve())

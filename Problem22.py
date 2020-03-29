def Solve():

    file = open('C:/ProjectEuler/p022_names.txt', 'r')
    data = file.read()
    file.close()

    temp = data.replace('"','')
    temp = temp.split(',')
    temp.sort()
    temp = [(x+1)*sum([ord(z)-64 for z in y]) for (x,y) in enumerate(temp)]
    temp = sum(temp)
    
    return(temp)


if __name__ == '__main__':
    print(Solve())

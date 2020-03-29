def Solve():
    maxDigitalSum = 0
    for a in range(1,100):
        for b in range(1,100):
            z = a ** b
            z = sum([int(d) for d in str(z)])
            maxDigitalSum = max(maxDigitalSum, z)
            
    return maxDigitalSum

    
if __name__ == '__main__':
    print(Solve())

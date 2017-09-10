from Functions import IsPrime

def Solve():
    pos   = 1
    width = 2
    prime = 0
    total = 1
    while True:
        for i in range(3):
            pos += width
            if IsPrime(pos): prime += 1
        pos += width #we know this one isn't prime; it's a perfect square
        total += 4
        if prime * 10 < total:
            return width + 1
        width += 2

if __name__ == '__main__':
    import cProfile
    cProfile.run('Solve()')
from time import time

doAll = False
doAll = True

Problems = []
start = 1
i = start
while (True):
    try:
        Problems.append(__import__('Problem' + str(i)))
        i += 1
    except:
        break

def main():
    begin = time()
    for i, p in enumerate(Problems):
        startTime = time()
        solution = p.Solve()
        stopTime = time()
        ms = 1000 * (stopTime - startTime)
        print(start + i, f'{ms:10.3f} ms')
    print(time() - begin)

if __name__ == '__main__':
    main()

import time

Problems = []
i = 0
while (True):
    i += 1
    try:
        Problems.append(__import__('Problem' + str(i)))
    except:
        i -= 1
        break

if False:
    begin = time.clock()
    for i, p in enumerate(Problems):
        startTime = time.clock()
        print(i + 1, p.Solve(), time.clock() - startTime)
    print(time.clock() - begin)
else:
    startTime = time.clock()
    print('Problem', i, Problems[i-1].Solve(), time.clock() - startTime)

from time import clock

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

if doAll:
    begin = clock()
    for i, p in enumerate(Problems):
        startTime = clock()
        print(start + i, p.Solve(), clock() - startTime)
    print(clock() - begin)
else:
    startTime = clock()
    print('Problem', i, Problems[i-1].Solve(), clock() - startTime)

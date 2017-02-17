#!/usr/bin/python3
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

    # print("Problem", i, Problems[i].Solve(), time.clock() - startTime)

startTime = time.clock()
print('Problem', i, Problems[i-1].Solve(), time.clock() - startTime)

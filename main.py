#!/usr/bin/python
import time

Problems = ['Placeholder']
i = 0
while (True):
    i += 1
    try:
        Problems.append(__import__('Problem' + str(i)))
    except:
        i -= 1
        break
    startTime = time.clock()
    # print("Problem", i, Problems[i].Solve(), time.clock() - startTime)

print(Problems[i].Solve())
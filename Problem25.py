#actually problem 25

def Solve():
    index = 2
    prior = 1
    fib = 1
    while len(str(fib))< 1000:
        index += 1
        fib, prior = fib + prior, fib
    return index
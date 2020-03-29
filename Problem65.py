from fractions import Fraction

def Solve():

    c = 100

    fractions = [2]
    for k in range(1, int(c/3)+2):
        fractions.append(1)
        fractions.append(2*k)
        fractions.append(1)

    temp = Fraction(fractions[c-1])
    for f in fractions[c-2::-1]:
        temp = 1/temp + f
    return sum([int(d) for d in str(temp.numerator)])


if __name__ == '__main__':
    print(Solve())
    from time import clock
    s = clock()
    print(Solve(), clock() - s)

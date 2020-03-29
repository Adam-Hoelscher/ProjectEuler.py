from collections import Counter

def Solve():

    counts = Counter()

    for a in range(1, 1000):
        for b in range(a, 1000-a):
            c = (a**2 + b**2)**.5
            p = a + b + c
            if c == int(c) and p <= 1000:
                counts[int(p)] += 1

    return(counts.most_common(1)[0][0])


if __name__ == '__main__':
    print(Solve())

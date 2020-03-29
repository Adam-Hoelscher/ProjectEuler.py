from Functions import PrimeFactors

def Solve():

    length = 4
    beg = 2

    while True:
        for step in range(length-1, -1, -1):
            if len(set(PrimeFactors(beg + step))) != length:
                beg += step+1
                break
            if step == 0:
                return(beg)


def Solve2():
    def prime_factors(n):
        """Returns all the prime factors of a positive integer"""
        factors = []
        d = 2
        while n > 1:
            while n % d == 0:
                factors.append(d)
                n /= d
            d += 1
            if d * d > n:
                if n > 1: factors.append(n)
                break
        return factors

    one = set(prime_factors(1))
    two = set(prime_factors(2))
    three = set(prime_factors(3))
    four = set(prime_factors(4))

    for i in range(5, 200000):
        one = set(two)
        two = set(three)
        three = set(four)
        four = set(prime_factors(i))
        if (len(one) >= 4 and len(two) >= 4 and len(three) >= 4 and len(four) >= 4):
            return(i - 3)


if __name__ == '__main__':
    print(Solve())

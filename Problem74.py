from math import factorial


def Solve(length=60, limit=1_000_000):

    def step(x):
        return sum(factorial(int(d)) for d in str(x))

    def chain_len(x, seen=None, cache={}):

        if x in cache:
            return cache[x]

        else:
            seen = seen or set()

            if x in seen:
                answer = 0

            else:
                seen.add(x)
                next_x = step(x)
                next_len = chain_len(next_x, seen)
                answer = next_len + 1

            cache[x] = answer
            return answer

    def seeds(length=60, limit=1_000_000):
        for i in range(1, limit):
            if chain_len(i) == length:
                yield i

    return len(list(seeds()))


if __name__ == '__main__':
    print(Solve())

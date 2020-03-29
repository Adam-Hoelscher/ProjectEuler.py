def Solve(limit=100):
    sq_sum = sum(range(limit + 1)) ** 2
    sum_sq = sum(x ** 2 for x in range(limit + 1))
    return sq_sum - sum_sq


if __name__ == '__main__':
    print(Solve())

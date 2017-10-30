def Solve(val=200, coins=[1,2,5,10,20,50,100,200]):

    if val < 0:
        return(0)
    if val == 0 or len(coins) == 1:
        return(1)
    else:
        # sort so that the largest coin is first
        coins.sort(reverse=True)
        usingFewer = Solve(val, coins[1:])
        if val >= coins[0]:
            makingSmaller = Solve(val - coins[0], coins)
        else:
            makingSmaller = 0
        return(usingFewer + makingSmaller)

def Solve2(val=200, coins=[1,2,5,10,20,50,100,200]):

    if val == 0 or len(coins) == 1:
        return(1)
    else:
        # sort so that the largest coin is first
        coins.sort(reverse=True)
        largeCoinValue = coins[0]
        maxOfLargeCoin = val // largeCoinValue
        tempCount = 0
        smallCoins = coins[1:]
        for largeCoinNum in range(maxOfLargeCoin+1):
            smallerValue = val - largeCoinNum * largeCoinValue
            tempCount += Solve2(smallerValue, smallCoins)
        return(tempCount)


if __name__ == '__main__':
    import cProfile
    cProfile.run('print(Solve())')
    cProfile.run('print(Solve2())')
    # cProfile.run('print(makeCoin(50,[25,1]))')
    # print(Solve())

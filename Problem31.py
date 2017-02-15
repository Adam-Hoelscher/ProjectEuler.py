def Solve():
    
    coins = [1, 2, 5, 10, 20, 50, 100, 200][::-1]
    
    def Count(val, coins):
        if val == 0 or len(coins) == 1:
            temp = 1
        else:
            numBig = val // coins[0]
            temp = sum([Count(val - x*coins[0], coins[1:]) for x in range(numBig+1)])
#            temp = oCount + numBig
        return(temp)
    
    return(Count(200, coins))

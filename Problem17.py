def Solve():

    def Words(n):
        if n >= 1000:
            return('onethousand' + Words(n-1000))
        if n >= 100:
            temp = Words(n//100) + 'hundred'
            if (n%100):
                temp += 'and'
                temp += Words(n%100)
            return(temp)
        if n > 19:
            tens = n // 10
            temp = {2: 'twenty',
                    3: 'thirty',
                    4: 'forty',
                    5: 'fifty',
                    6: 'sixty',
                    7: 'seventy',
                    8: 'eighty',
                    9: 'ninety'}
            temp = temp[tens]
            return(temp + Words(n%10))
        else:
            temp = {0: '',
                    1: 'one',
                    2: 'two',
                    3: 'three',
                    4: 'four',
                    5: 'five',
                    6: 'six',
                    7: 'seven',
                    8: 'eight',
                    9: 'nine',
                    10:'ten',
                    11:'eleven',
                    12:'twelve',
                    13:'thirteen',
                    14:'fourteen',
                    15:'fifteen',
                    16:'sixteen',
                    17:'seventeen',
                    18:'eighteen',
                    19:'nineteen'}[n]
            return(temp)

    words = ''
    for i in range(1,1001):
        words += Words(i)

    return(len(words))


if __name__ == '__main__':
    print(Solve())

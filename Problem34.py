from math import factorial as Fact

def Solve():

    digits = 1
    while digits*Fact(9) > int('9'*digits):
        digits += 1
    digits -= 1

    temp = 0
    for i in range(3,int('9'*digits)):
        if sum([Fact(int(x)) for x in str(i)]) == i:
            temp += i

    return(temp)

    
if __name__ == '__main__':
    print(Solve())

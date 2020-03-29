from datetime import date

def Solve():

    days = []
    for year in range(1901, 2001):
        for month in range(1, 13):
            test = date(year, month, 1)
            if test.weekday() == 6:
                days.append(test)

    return(len(days))


if __name__ == '__main__':
    print(Solve())

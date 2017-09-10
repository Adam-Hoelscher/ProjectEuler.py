def Solve(to = 10**6):

    # replaced original function with a version that uses a dict
    # improved from 3.9 seconds to 2.7
    def Col(n):
        if n%2:
            return (3 * n + 1)
        else:
            return(n/2)

    lengths = {1:1}

    def FindLength(x):
        l = lengths.get(x, 0)
        if l:
            temp = l
        else:
            NextColl = Col(x)
            temp = 1 + FindLength(NextColl)
            lengths[x] = temp
        return(temp)

    temp = [FindLength(x) for x in range(1, to, 2)]
    return(temp.index(max(temp)))

# def Solve(to = 10**6):
#
#     lengths = {}
#     maxLen = 0
#     maxKey = 0
#
#     def Col(n):
#         if n%2:
#             return (3 * n + 1)
#         else:
#             return(n/2)
#
#     for i in range(1, to):
#         n = i
#         count = 0
#         stop = False
#         while (n != 1):
#             try:
#                 count += lengths[n]
#                 break
#             except:
#                 n = Col(n)
#                 count += 1
#         lengths[i] = count
#         if count > maxLen:
#             maxLen = count
#             maxKey = i
#
#     return(maxKey)

if __name__ == '__main__':
    import cProfile
    cProfile.run('Solve()')

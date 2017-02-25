from collections import Counter

def Solve():

    file = open('C:/ProjectEuler/p059_cipher.txt')
    cipherText = file.read()
    file.close()

    cipherText = [int(x) for x in cipherText.split(',')]
    length = len(cipherText)
    commonChar = ' ' #assuming the plan text is english, spaces are more prevalent than any letter
    temp = 0

    for charSet in range(3):
        cipher = cipherText[charSet:length:3]
        commonCharCount = 0
        pwCode = 0
        for pwLetter in range(ord('a'), ord('z')+1):
            charCount = Counter()
            plain = [chr(pwLetter ^ cLetter) for cLetter in cipher]
            for plainLetter in plain:
                charCount[plainLetter] += 1
            if charCount[commonChar] > commonCharCount:
                commonCharCount = charCount[commonChar]
                pwCode = pwLetter
        plainValue = sum([pwCode ^ cLetter for cLetter in cipher])
        temp += plainValue

    return temp
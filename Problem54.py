from collections import Counter
from operator import itemgetter

def Solve():

    faceCards = {'T': 10, 'J':11, 'Q':12, 'K':13, 'A':14}

    def HandScore(hand):
        values = Counter()
        suits  = set()
        for card in hand:
            rank = card[0]
            try:
                v = int(rank)
            except:
                v = faceCards[rank]
            values[v] += 1
            suits.add(card[1])
        isStraight = max(values.keys()) == min(values.keys()) + 4 and len(values) == 5
        isFlush = suits.pop() == 5
        if isStraight and isFlush:
            score = 8
        elif max(values.values()) == 4:
            score = 7
        elif max(values.values()) == 3 and max(values.values()) == 2:
            score = 6
        elif isFlush:
            score = 5
        elif isStraight:
            score = 4
        elif max(values.values()) == 3:
            score = 3
        elif values.most_common(2)[0][1] == 2 and values.most_common(2)[1][1] == 2:
            score = 2
        elif values.most_common(2)[0][1] == 2:
            score = 1
        else:
            score =  0

        tieBreakSet = values.most_common()
        tieBreakSet = [(y,x) for (x,y) in tieBreakSet]
        tieBreakSet.sort(reverse = True)
        tieBreakSet = sum([[x]*y for y, x in tieBreakSet],[])
        tieBreak = 0
        for v in tieBreakSet:
            tieBreak *= 15
            tieBreak += v

        score *= 15**5
        score += tieBreak

        return score

    file = open('./data/p054_poker.txt')
    hands = file.read()
    file.close()

    hands = hands.split('\n')
    count = 0
    blah = []
    i = 0
    for hand in hands:
        try:
            hand = hand.split(' ')
            hand1 = hand[0:5]
            hand2 = hand[5:10]
            score1 = HandScore(hand1)
            score2 = HandScore(hand2)
            if score1 > score2:
                count += 1
        except:
            pass

    return count


if __name__ == '__main__':
    print(Solve())

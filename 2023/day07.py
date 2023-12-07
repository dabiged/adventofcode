from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from collections import Counter

test_input=[
'32T3K 765',
'T55J5 684',
'KK677 28',
'KTJJT 220',
'QQQJA 483'
]

global p1_cardrank
p1_cardrank={}
for i,v in enumerate([2,3,4,5,6,7,8,9,'T','J','Q','K','A']):
    p1_cardrank[str(v)]=i

global p2_cardrank
p2_cardrank={}
for i,v in enumerate(['J',2,3,4,5,6,7,8,9,'T','Q','K','A']):
    p2_cardrank[str(v)]=i

class Hand():
    def __init__(self,inputcards):
        self.inputcards=inputcards
        self.cards=Counter(self.inputcards)

    def cardscore(self):
        score=''
        for card in self.inputcards:
            score+=str(p1_cardrank[card]).zfill(2)
        return score

    def score(self):
        if len(set(self.cards)) == 1:
            # Five of a kind
            return '6'+self.cardscore()
        if len(set(self.cards)) == 2:
            for c,n in dict(self.cards).items():
                if n==4:
                    # Four of a kind
                    return '5'+self.cardscore()
                elif n==3:
                    # Full house
                    return '4'+self.cardscore()
        if len(set(self.cards)) == 3:
            for c,n in dict(self.cards).items():
                if n==3:
                    # triple
                    return '3'+self.cardscore()
                elif n==2:
                    # two pair
                    return '2'+self.cardscore()
        if len(set(self.cards)) == 4:
            return '1'+self.cardscore()
        if len(set(self.cards)) == 5:
            return self.cardscore()


class WildHand():
    def __init__(self,inputcards,originalcards=None):
        self.inputcards=inputcards
        if originalcards == None:
            self.originalcards=inputcards
        else:
            self.originalcards=originalcards
        self.cards=Counter(self.inputcards)

    def cardscore(self):
        score=''
        for card in self.originalcards:
            score+=str(p2_cardrank[card]).zfill(2)
        return score

    def score(self):
        if len(set(self.cards)) == 1:
            # Five of a kind
            return '6'+self.cardscore()
        if len(set(self.cards)) == 2:
            for c,n in dict(self.cards).items():
                if n==4:
                    # Four of a kind
                    return '5'+self.cardscore()
                elif n==3:
                    # Full house
                    return '4'+self.cardscore()
        if len(set(self.cards)) == 3:
            for c,n in dict(self.cards).items():
                if n==3:
                    # triple
                    return '3'+self.cardscore()
                elif n==2:
                    # two pair
                    return '2'+self.cardscore()
        if len(set(self.cards)) == 4:
            return '1'+self.cardscore()
        if len(set(self.cards)) == 5:
            return self.cardscore()

    def wildscore(self):
        if 'J' not in self.inputcards:
            return self.score()
        possible_scores=[]
        for replacement in p2_cardrank.keys():
            if replacement == 'J':
                pass
            else:
                possiblehand=self.inputcards.replace('J',replacement,1)
                newHand=WildHand(possiblehand,self.originalcards)
                possible_scores.append(int(newHand.wildscore()))
        return str(max(possible_scores))


class Game():
    def __init__(self,data):
        self.data=data
        self.parse()

    def parse(self):
        self.players=[]
        for row in self.data:
            hand=row.split()[0]
            bid=row.split()[1]
            self.players.append((hand,bid))

        self.players.sort(key=lambda x: int(Hand(x[0]).score()))
    def score(self):
        score=0
        for i,j in enumerate(self.players):
            bid=j[1]
            score+=((i+1)*int(bid))
        return score

class WildGame():
    def __init__(self,data):
        self.data=data
        self.parse()

    def parse(self):
        self.players=[]
        for row in self.data:
            hand=row.split()[0]
            bid=row.split()[1]
            self.players.append((hand,bid))

        self.players.sort(key=lambda x: int(WildHand(x[0]).wildscore()))

    def score(self):
        for hand,bid in self.players:
            print(hand, WildHand(hand).wildscore())
        score=0
        for i,j in enumerate(self.players):

            bid=j[1]
            score+=((i+1)*int(bid))
        return score




def part1(inputdata=test_input):
    myg=Game(inputdata)
    return myg.score()

def part2(inputdata=test_input):
    myg=WildGame(inputdata)
    return myg.score()


def day07_01():
    """Run part 1 of Day 7's code"""
    path = "./input/07.txt"
    print("0701:", part1(file_to_str_array(path)))


def day07_02():
    """Run part 2 of Day 1's code"""
    print(part2())
    path = "./input/07.txt"
    print("0702:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    #day07_01()
    day07_02()

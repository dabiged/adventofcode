"""
Advent of Code Day 04 2021
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class BingoCard():
    def __init__(self,number,inputcard):
        self.card={}
        self.cardid=number
        for row,line in enumerate(inputcard):
            for col,number in enumerate(line):
                self.card[row,col]=(int(number),False)


    def mark_num(self,num):
        for location,cardnum in self.card.items():
            if cardnum[0] == num:
                self.card[location]=(num,True)
                return None

    def isWinner(self):
        if self.isRowWinner() or self.isColWinner():# or self.is1DiagWinner() or self.is2DiagWinner():
            return True
        return False

    def isColWinner(self):
        for col in range(0,5):
            Winner=True
            for row in range(0,5):
                Winner = Winner and self.card[(row,col)][1]
            if Winner:
                return Winner

    def isRowWinner(self):
        for row in range(0,5):
            Winner=True
            for col in range(0,5):
                Winner = Winner and self.card[row,col][1]
            if Winner:
                return Winner

    def is1DiagWinner(self):
        Winner=True
        for diag in range(0,5):
            Winner=Winner and self.card[diag,diag][1]
        if Winner:
            return Winner

    def is2DiagWinner(self):
        Winner=True
        for diag in range(0,5):
            Winner=Winner and self.card[diag,4-diag][1]
        if Winner:
            return Winner


    def score(self,num):
        score=0
        for row in range(0,5):
            for col in range(0,5):
                if not self.card[(row,col)][1]:
                    score += self.card[(row,col)][0]
        return self.cardid, score*int(num)

class BingoGame():
    def __init__(self,inputfile):
        self.inputdata=file_to_str_array(inputfile)

        self.numbersCalled=self.inputdata[0].split(',')

        self.bingocards={}

        self.buildcards()

    def buildcards(self):
        thiscard=[]
        cardnumber=0
        for row,vals in enumerate(self.inputdata[2:]):
            if row %6 ==5:
                cardnumber+=1
                self.bingocards[cardnumber]=BingoCard(cardnumber,thiscard)
                thiscard=[]
            else:
                thiscard.append(vals.replace("  "," ").split(" "))


    def playgame(self):
        for numcalled in self.numbersCalled:
            for card in self.bingocards.values():
                card.mark_num(int(numcalled))
            for card in self.bingocards.values():
                if card.isWinner():
                    cardid,score = card.score(numcalled)
                    return cardid, score

    def get_worst(self):
        while len(self.bingocards.values())>0:
            cardid,score = self.playgame()
            del(self.bingocards[cardid])
        return cardid,score


def day04_01(inputfile):
    """Run part 1 of Day 4's code"""
    mygame=BingoGame(inputfile)
    return mygame.playgame()


def day04_02(inputfile):
    """Run part 2 of Day 4's code"""
    mygame=BingoGame(inputfile)
    return mygame.get_worst()

if __name__ == "__main__":
    PATH = "./input/day04.txt"
    print('0401:',day04_01(PATH)[1])
    print('0402:',day04_02(PATH)[1])

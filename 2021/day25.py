"""
AOC day 25 2018
"""
from collections import defaultdict
from lib.filehelper import file_to_str_array
from copy import deepcopy
# pylint: disable=missing-module-docstring

class Board():
    def __init__(self,inputstrs):
        self.input=inputstrs
        self.board=[]
        self.processinput()

    def processinput(self):
        for line in self.input:
            self.board.append(line)

    def move(self,cucumberchar):
        for rownum,row in enumerate(self.board):
            if row[-1] == cucumberchar and row[0] == '.':
                # This is required because str is immutable.
                thisrow=list()
                thisrow.append(cucumberchar)
                [thisrow.append(i) for i in row[1:-1].replace(cucumberchar+'.','.'+cucumberchar)]
                thisrow.append('.')
                self.board[rownum]="".join(thisrow)
                continue
            self.board[rownum]=row.replace(cucumberchar+'.','.'+cucumberchar)

    def transpose(self):
        self.board=[list(x) for x in zip(*self.board)]
        self.board=["".join(x) for x in self.board]

    def countchanges(self,oldboard):
        numchanges=0
        for oldrow,newrow in zip(oldboard,self.board):
            for oldchar,newchar in zip(oldrow,newrow):
                if oldchar!=newchar:
                    numchanges+=1
        return numchanges

    def step(self):
        oldboard=deepcopy(self.board)
        self.move('>')
        self.transpose()
        self.move('v')
        self.transpose()
        count=self.countchanges(oldboard)
        return count

    def run(self):
        numchanges=1
        numsteps=0
        while numchanges>0:
            numsteps+=1
            numchanges= self.step()
            print(self)
        return numsteps

    def __repr__(self):
        output=''
        for row in self.board:
            output+=row+'\n'
        return output

def day25_01():
    """Run part 1 of Day 25's code"""
    inputfile='input/day25.txt'
    myboard=Board(file_to_str_array(inputfile))
    result=myboard.run()
    print(f'2501: {result} ')

if __name__ == "__main__":
    day25_01()

"""
AOC day 06 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Board:
    """
    A checker board like playing area of squares containing sources.
    Each source is allocated an increasing letter and its location on the board is a capital.

    """
    def __init__(self,listofsource, halo=2):
        self.alphabet = {num:char for num,char in enumerate("abcdefghijklmnopqrstuvwxyz")}
        self.sources={}
        sourcenum=0
        for source in listofsource:
            self.sources[self.alphabet[sourcenum]]=tuple([int(i) for i in source.split(", ")])
            sourcenum+=1
        self.board=[]
        for row in range(0,self.source_row_max()+halo):
            thisrow = ["." for col in range(0,self.source_col_max()+halo)]
            self.board.append(thisrow)
        for key, location in self.sources.items():
            row, col = location
            self.board[col][row] = key.upper()

    def __repr__(self):
        """
        A helper method that allows us to run
        > print(mysquare)
        to return a human readable representation of the cuts.
        """
        gridplot=""
        for thisrow in self.board:
            gridplot+="".join(thisrow)+"\n"
        return gridplot


    def source_col_max(self):
        return max([self.sources[source][0]  for source in self.sources])

    def source_row_max(self):
        return max([self.sources[source][1]  for source in self.sources])

    def source_col_min(self):
        return min([self.sources[source][0]  for source in self.sources])

    def source_row_min(self):
        return min([self.sources[source][1]  for source in self.sources])


def day06_01():
    """Run part 1 of Day 06's code"""
    path = "./input/06/input.txt"
    print(f'0601: {result}')

def day06_02():
    """Run part 2 of Day 06's code"""
    path = "./input/06/input.txt"
    print(f'0602: {result}')

if __name__ == "__main__":
    day06_01()
    day06_02()

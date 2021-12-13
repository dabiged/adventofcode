"""
AOC day 13 2018
"""
from collections import defaultdict
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


class Board():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.board=defaultdict(lambda: '.')
        self.processinputfile()

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)
        self.dotlocs=[]
        self.folds=[]
        self.maxx=0
        self.maxy=0
        for line in self.input:
            if ',' in line:
                coords = line.split(',')
                x=int(coords[0])
                y=int(coords[1])
                self.maxx=max(self.maxx,x)
                self.maxy=max(self.maxy,y)
                self.board[(x,y)]='#'

            elif len(line) == 0:
                pass
            elif  line.startswith('fold along'):
                self.folds.append(line.replace('fold along ',''))
        return None

    def fold(self,foldinst):
        direction,value = foldinst.split('=')
        value=int(value)
        if direction == 'y':
            for x in range(self.maxx+1):
                self.board[(x,value)]='-'
            for y in range(0,value):
                for x in range(0,self.maxx+1):
                    if self.board[(x,y)] == '.':
                        self.board[(x,y)]= self.board[(x,2*value-y)]
            self.maxy=value-1


        elif direction == 'x':
            for y in range(self.maxy+1):
                self.board[(value,y)]='|'
            for x in range(0,value):
                for y in range(0,self.maxy+1):
                    if self.board[(x,y)] == '.':
                        self.board[(x,y)]= self.board[(2*value-x,y)]
            self.maxx=value-1

    def part2(self):
        for fold in self.folds:
            self.fold(fold)

    def part1(self):
        self.fold(self.folds[0])
        count=0
        for x in range(self.maxx+1):
            for y in range(self.maxy+1):
                if self.board[(x,y)]=='#':
                    count+=1
        return count


    def __repr__(self):
        output=''
        for y in range(self.maxy+1):
            thisy=''
            for x in range(self.maxx+1):
                thisy+=self.board[(x,y)]
            output+=thisy+'\n'
        return output



def day13_01():
    """Run part 1 of Day 13's code"""
    inputfile='input/day13.txt'
    testboard=Board(inputfile)
    result=testboard.part1()
    print(f'1301: {result} Hashes after the first fold')

def day13_02():
    """Run part 2 of Day 13's code"""
    inputfile='input/day13.txt'
    testboard=Board(inputfile)
    testboard.part2()
    result='CAFJHZCK'
    print(f'1302: {result} Is the activation key.')

if __name__ == "__main__":
    day13_01()
    day13_02()

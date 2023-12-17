from lib.filehelper import get_string_lists_from_file, get_map_from_file
# pylint: disable=missing-module-docstring
import itertools
from collections import defaultdict

test_input=[
['##..##..',
'#.##.#..',
'..#...##',
'......##',
'#.##.#..',
'##..##..',
'#.##.#..'],
['#...##..#',
'#....#..#',
'..##..###',
'#####.##.',
'#####.##.',
'..##..###',
'#....#..#']]

class Sheet():
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.map={}
        self.parse()
        self.score=self.check_all()

    def parse(self):
        for r,rch in enumerate(self.inputdata):
            for c,ch in enumerate(rch):
                self.map[c+r*1j]=ch
        self.numrows=r
        self.numcols=c

    def check_symmetric_rows(self,rownum):
        symmetric=True
        for i in range(rownum+1):
            mirror_side1 = rownum-i
            mirror_side2 = rownum+1+i
            if mirror_side1 >self.numrows or mirror_side1 < 0 or mirror_side2 >self.numrows or mirror_side2 <0:
                continue
            else:
                row1="".join([self.map[mirror_side1*1j+col] for col in range(self.numcols+1)])
                row2="".join([self.map[mirror_side2*1j+col] for col in range(self.numcols+1)])
                symmetric = symmetric and row1 == row2
        return symmetric

    def check_symmetric_cols(self,colnum):
        symmetric=True
        for i in range(colnum+1):
            # 0: 0,1; 1: 1,2, 0,3 2: 2,3 1,4, 0,5
            mirror_side1 = colnum-i
            mirror_side2 = colnum+1+i
            if mirror_side2 >self.numcols or mirror_side1 < 0 :
                continue
            elif mirror_side1 >self.numcols or mirror_side2 < 0 :
                continue
            else:
                col1="".join([self.map[mirror_side1+row*1j] for row in range(self.numrows+1)])
                col2="".join([self.map[mirror_side2+row*1j] for row in range(self.numrows+1)])
                symmetric = symmetric and col1 == col2
        return symmetric


    def check_all(self):
        sym=set()
        for i in range(0,self.numrows):
            if self.check_symmetric_rows(i):
                sym.add((i+1,0))
        for i in range(0,self.numcols):
            if self.check_symmetric_cols(i):
                sym.add((0,i+1))
        return sym


    def flips(self):
        allsyms=set()
        for k,v in self.map.items():
            if v == '#':
                self.map[k] = '.'
            elif v == '.':
                self.map[k] = '#'

            newscore = self.check_all()
            if len(newscore) != 0:
                for sym in newscore:
                    allsyms.add(sym)
            self.map[k]=v
        for sym in allsyms:
            if sym not in self.score:
                return sym


def part1(inputdata=test_input):
    tot_rows, tot_cols= 0,0
    for i,sheetinput in enumerate(inputdata):
        mys=Sheet(sheetinput)
        thisscore=mys.check_all()
        rows,cols=next(iter(thisscore))
        tot_rows+=rows
        tot_cols+=cols
    return tot_rows*100+tot_cols



def part2(inputdata=test_input):
    rows,cols = 0,0
    for i,sheetinput in enumerate(inputdata):
        mys=Sheet(sheetinput)
        newscore=mys.flips()
        rows+=newscore[0]
        cols+=newscore[1]

    return rows*100+cols

def day13_01():
    """Run part 1 of Day 7's code"""
    path = "./input/13.txt"
    print("1301:", part1(get_map_from_file(path)))


def day13_02():
    """Run part 2 of Day 1's code"""
    path = "./input/13.txt"
    print("1302:", part2(get_map_from_file(path)))


if __name__ == "__main__":
    day13_01()
    day13_02()

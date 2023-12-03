from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

test_input=[
'467..114..',
'...*......',
'..35..633.',
'......#...',
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..']


class schematic():
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.board=defaultdict(lambda: '.')
        self.parse()

    def parse(self):
        loc=0+0j
        for row in self.inputdata:
            for char in row:
                self.board[loc]=char
                loc+=1
            loc= 0+(loc.imag+1)*1j

    def symbols(self):
        symbol_locations=[]
        for loc,char in self.board.items():
            if not char.isnumeric() and not char.isalpha() and char != '.':
                symbol_locations.append(loc)
        return symbol_locations

    def get_num(self,location):
        if not self.board[location].isnumeric():
            raise RuntimeError
        number=''
        row=int(location.imag)*1j
        mincol=int(location.real)
        maxcol=int(location.real)
        done=False
        while not done:
            mincol+=-1
            if not self.board[mincol+row].isnumeric():
                mincol+=1
                done=True
        done=False
        while not done:
            maxcol+=1
            if not self.board[maxcol+row].isnumeric():
                done=True
        return int("".join([self.board[a+row] for a in range(mincol,maxcol)]))

    def score_p1(self):
        allnum={}
        for location in self.symbols():
            neighbours=set()
            for re in [-1, 0, 1]:
                for im in [-1, 0, 1]:
                    checkloc=location+re+im*1j
                    if self.board[checkloc].isnumeric():
                        neighbours.add(self.get_num(checkloc))
            allnum[location]=neighbours
        total=0
        for _,v in allnum.items():
            for i in v:
                total+=i
        return total

    def score_p2(self):
        allnum={}
        for location in self.symbols():
            neighbours=set()
            for re in [-1, 0, 1]:
                for im in [-1, 0, 1]:
                    checkloc=location+re+im*1j
                    if self.board[checkloc].isnumeric():
                        neighbours.add(self.get_num(checkloc))
            if len(neighbours) == 2 and self.board[location] == '*':
                i=1
                for n in neighbours:
                    i=i*n
                allnum[location]=i

        total=0
        for _,v in allnum.items():
            total+=v
        return total


def part1(inputdata=test_input):
    mys=schematic(inputdata)
    return mys.score_p1()

def part2(inputdata=test_input):
    mys=schematic(inputdata)
    return mys.score_p2()


def part1(inputdata=test_input):
    mys=schematic(inputdata)
    return mys.score_p1()

def part2(inputdata=test_input):
    mys=schematic(inputdata)
    return mys.score_p2()

def day03_01():
    """Run part 1 of Day 1's code"""
    path = "./input/03.txt"
    print("0301:", part1(file_to_str_array(path)))


def day03_02():
    """Run part 2 of Day 1's code"""
    path = "./input/03.txt"
    print("0302:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day03_01()
    day03_02()

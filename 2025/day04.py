from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring
testdata='''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''


class Warehouse():
    def __init__(self,grid):
        self.input=grid
        self.grid=defaultdict(str)
        self.process()

    def process(self):
        loc=0
        for i in self.input:
            for char in i:
                self.grid[loc]=char
                loc+=1
            loc-=int(loc.real)
            loc+=1j

    def accessible(self,pos):
        if self.grid[pos] != '@':
            return False
        numtaken=0
        for delta in [ 1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j ]:
            if self.grid[pos+delta] == '@':
                numtaken+=1
        if numtaken < 4:
            return True
        return False

    def how_many_accessible(self):
        num_accessible=0
        for i in self.grid.keys():
            if self.accessible(i):
                num_accessible+=1
        return num_accessible

    def remove_accessible(self):
        removeme=[]
        for i in self.grid.keys():
            if self.accessible(i):
                removeme.append(i)
        for j in removeme:
            self.grid[j]='x'
        return len(removeme)

        
    def __repr__(self):
        numrows=max([int(i.imag) for i in self.grid.keys()])
        numcols=max([int(i.real) for i in self.grid.keys()])
        output=''
        for i in range(-1,numcols+2):
            for j in range(-1,numrows+2):
                loc=i*1j+j
                output+=self.grid[loc]
            output+='\n'
        return output


testdata=testdata.split('\n')

def part1(inputdata=testdata):
    my=Warehouse(inputdata)
    print(my)
    return my.how_many_accessible()


def part2(inputdata=testdata):
    my=Warehouse(inputdata)
    print(my)
    removed=my.remove_accessible()
    total_removed=removed
    while removed>0:
        removed=my.remove_accessible()
        total_removed+=removed
    return total_removed

def day04_01():
    """Run part 1 of Day 04's code"""
    #part1(testdata)
    path = "./input/04.txt"
    print("0401:", part1(file_to_str_array(path)))


def day04_02():
    """Run part 2 of Day 04's code"""
    part2(testdata)
    path = "./input/04.txt"
    print("0402:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day04_01()
    day04_02()

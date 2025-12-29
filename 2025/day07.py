from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring
testdata='''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''


testdata=testdata.split('\n')

def propagate_tachyons(tachyons,splitters):
    new_tachyons=defaultdict(int)
    for pos,count in tachyons.items():
        if pos in splitters:
            new_tachyons[pos-1] += count
            new_tachyons[pos+1] += count
        else:
            new_tachyons[pos]+=count
    return new_tachyons

class Manifold():
    def __init__(self,grid):
        self.input=grid
        self.grid=defaultdict(str)
        self.start=None
        self.activerow=1
        self.numsplits=0
        self.tachyons=defaultdict(int)
        self.splitters=[]
        self.process()

    def process(self):
        self.maxrows , self.maxcols= -1,-1
        loc=0
        for i in self.input:
            splitters=set()
            for char in i:
                self.grid[loc]=char
                if char == 'S':
                    self.start=loc
                    self.tachyons[int(self.start.real)]=1
                if char == '^':
                    splitters.add(int(loc.real))
                loc+=1
                self.maxrows=max(int(loc.imag),self.maxrows)
                self.maxcols=max(int(loc.real),self.maxcols)
            if len(splitters) >0:
                self.splitters.append(splitters)
            loc-=int(loc.real)
            loc+=1j

    def step(self):
        for loc in self.grid.keys():
            if int(loc.imag) == self.activerow:
                if self.grid[loc-1j] in ['|','S']:
                    if self.grid[loc] == '^':
                        self.grid[loc+1], self.grid[loc-1] = '|','|'
                        self.numsplits+=1
                    else:
                        self.grid[loc]='|'
        self.activerow+=1

    def run_part2(self):
        for row in self.splitters:
            self.tachyons=propagate_tachyons(self.tachyons,row)

        return sum(self.tachyons.values())



    def run(self,grfx=False):
        while self.activerow <= self.maxrows:
            self.step()
            if grfx:
                print(self.activerow)
                print(self)
        return self.numsplits


    def __repr__(self):
        output=''
        for i in range(-1,self.maxcols+2):
            for j in range(-1,self.maxrows+2):
                loc=i*1j+j
                output+=self.grid[loc]
            output+='\n'
        return output


def part1(inputdata=testdata):
    my=Manifold(inputdata)
    return my.run()


def part2(inputdata=testdata):
    my=Manifold(inputdata)
    return my.run_part2()

def day07_01():
    """Run part 1 of Day 07's code"""
    path = "./input/07.txt"
    print("0702:", part1(file_to_str_array(path)))


def day07_02():
    """Run part 2 of Day 07's code"""
    #part2(testdata)
    path = "./input/07.txt"
    print("0702:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day07_01()
    day07_02()

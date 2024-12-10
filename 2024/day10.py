from lib.filehelper import file_to_str_array
from collections import defaultdict
from collections import deque
# pylint: disable=missing-module-docstring

testdata1='''1011911
2111811
3111711
4567654
1118113
1119112
1111101'''

testdata='''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

class Grid:
    def __init__(self,inputdata):
        # Store the input data for later (part 2)
        self.inputdata=inputdata
        self.grid=defaultdict(str)
        for rownum,row in enumerate(inputdata):
            for colnum, char in enumerate(row):
                self.grid[colnum+rownum*1j]=int(char)
        self.numrows=max([int(i.imag) for i in self.grid.keys()])
        self.numcols=max([int(i.real) for i in self.grid.keys()])
        
    def __str__(self):
        # helper method to print the grid
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                output+=str(self.grid[re+im*1j])
            output+='\n'
        return output

    def get_neighbours(self,point):
        neighbors=[]
        for i in [1, -1, 1j, -1*1j]:
            candidate=point+i
            if 0 <= candidate.real <= self.numrows and 0<=candidate.imag <= self.numcols:
                neighbors.append(candidate)
        return neighbors

    def find_trail_start(self):
        output=[]
        for k,v in self.grid.items():
            if v == 0:
                output.append(k)
        return output

    def score_trail(self,start):
        zero_to_nine=[]
        tocheck=deque()
        tocheck.append([start])
        print(tocheck)
        while len(tocheck)>0:
            currpath=tocheck.popleft()
            if self.grid[currpath[0]] == 0 and self.grid[currpath[-1]] == 9:
                if currpath not in zero_to_nine:
                    zero_to_nine.append(currpath)
            else:
                currval=currpath[-1]
                for neighbour in self.get_neighbours(currval):
                    if self.grid[neighbour] == self.grid[currval] +1:
                        tocheck.append(currpath+[neighbour])
            print(tocheck)
        uniq_peaks=set()
        uniq_trails=list()
        for i in zero_to_nine:
            uniq_peaks.add(i[-1])
            if i not in uniq_trails:
                uniq_trails.append(i)

        return len(uniq_peaks),len(uniq_trails)

    def score(self):
        peak_score=0
        trail_score=0
        for trail_start in self.find_trail_start():
            peak_score += self.score_trail(trail_start)[0]
            trail_score += self.score_trail(trail_start)[1]
        return peak_score,trail_score


def part1(inputdata=testdata.split('\n')):
    g=Grid(inputdata)
    return g.score()[0]

def part2(inputdata=testdata.split('\n')):
    g=Grid(inputdata)
    return g.score()[1]


def day10_01():
    """Run part 1 of Day 10's code"""
    path = "./input/10.txt"
    print("1001:", part1(file_to_str_array(path)))


def day10_02():
    """Run part 2 of Day 10's code"""
    path = "./input/10.txt"
    print("1002:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    part1()
    day10_01()
    day10_02()





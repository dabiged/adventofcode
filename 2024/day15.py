from lib.filehelper import file_to_str_array
from collections import defaultdict
from collections import deque
import re
# pylint: disable=missing-module-docstring

testdata='''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
'''

class Warehouse:
    def __init__(self,data):
        inputdata=data.split('\n\n')
        grid=inputdata[0]
        self.instructions=inputdata[1]
        self.grid=Grid(grid)
        dirs={'>':1,'<':-1,'^':-1j,'v':1j}

    def step(self,direction=None):
        if direction=None:
            direction=self.instructions.pop(0)
        print(direction)
        print(dirs[direction])
        self.grid.step(dirs[direction])


class Grid:
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.diag_neighbours=[up*1j+down for up in [-1,1] for down in [-1,1] ]
        self.direct_neighbours=[1,-1,1j,-1j]
        self.reset_grid()
        self.robot_pos=0

    def reset_grid(self):
        self.grid=defaultdict(str)
        for rownum,row in enumerate(self.inputdata):
            for colnum, char in enumerate(row):
                if char == '@':
                    self.robot_pos=colnum+rownum*1j
                self.grid[colnum+rownum*1j]=char

    def is_empty(self,pos):
        return self.grid[pos] == '.'

    def is_wall(self,pos):
        return self.grid[pos] == '#'

    def can_move(self,pos,direction):
        if self.isempty(pos+direction):
            return True
        if self.is_wall(pos_direction):
            return False
        return self.can_move(self,pos+direction,direction)

    def move(self,pos,direction):
        if self.grid[pos+direction] == '.':
            self.grid[pos+direction],self.grid[pos] = self.grid[pos],self.grid[pos+direction]
        elif self.grid[pos+direction] == 'O':
            self.move(pos+direction,direction)
            self.grid[pos+direction],self.grid[pos] = self.grid[pos],self.grid[pos+direction]
        if self.grid[pos] == self.robot_pos:
            self.robot_pos=pos+direction


    def on_grid(self,point):
        return 0<= point.imag <= self.numrows and 0<= point.real <= self.numcols

    def step(self,direction):
        if self.can_move(self.robot_pos,direction):
            self.move(self.robot_pos,directioN)

    def score(self):
        output=0
        for k,v in self.grid.items():
            if v == 'O':
                output+=int(k.real)+int(k.imag)*100
        return output


    def __len__(self):
        return self.numrows*self.numcols

    def __str__(self):
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                if re+im*1j == self.robot_pos:
                    output+='@'
                else:
                    output+=self.grid[re+im*1j]
            output+='\n'
        return output

def part1(inputdata=testdata.split('\n')):
    g=Grid(inputdata)
    print(g)

def part2(inputdata=testdata.split('\n')):
    pass


def day15_01():
    """Run part 1 of Day 15's code"""
    path = "./input/15.txt"
    print("1501:", part1(file_to_str_array(path)))


def day15_02():
    """Run part 2 of Day 15's code"""
    path = "./input/15.txt"
    print("1502:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    part1()
    #day15_01()
    #day15_02()

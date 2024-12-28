from lib.filehelper import file_to_str_array, get_bald_string_list_from_file, get_file
from collections import defaultdict
from collections import deque
import re
# pylint: disable=missing-module-docstring

testdata='''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
'''

testdata1='''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''

class Warehouse:
    def __init__(self,data):
        ''' data is a list, with 2 elements:
        0: grid object as a string
        1: instructions as a string containing newlines'''
        inputdata=data
        grid=inputdata[0]
        self.instructions=list(inputdata[1].strip().replace('\n',''))
        self.grid=Grid(grid.split('\n'))
        self.dirs={'>':1,'<':-1,'^':-1j,'v':1j}

    def step(self,direction=None):
        if direction==None:
            direction=self.instructions.pop(0)
        self.grid.step(self.dirs[direction])


class Grid:
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.diag_neighbours=[up*1j+down for up in [-1,1] for down in [-1,1] ]
        self.direct_neighbours=[1,-1,1j,-1j]
        self.robot_pos=0
        self.reset_grid()
        self.stepnum=0

    def reset_grid(self):
        self.grid=defaultdict(str)
        for rownum,row in enumerate(self.inputdata):
            for colnum, char in enumerate(row):
                if char == '@':
                    self.robot_pos=colnum+rownum*1j
                    self.grid[colnum+rownum*1j]='.'
                else:
                    self.grid[colnum+rownum*1j]=char
        self.numrows=rownum
        self.numcols=colnum

    def is_empty(self,pos):
        return self.grid[pos] == '.'

    def is_wall(self,pos):
        return self.grid[pos] == '#'

    def can_move(self,pos,direction):
        if self.is_empty(pos+direction):
            return True
        if self.is_wall(pos+direction):
            return False
        return self.can_move(pos+direction,direction)

    def move(self,pos,direction):
        if self.grid[pos+direction] == '.':
            self.grid[pos+direction],self.grid[pos] = self.grid[pos],self.grid[pos+direction]
        elif self.grid[pos+direction] == 'O':
            self.move(pos+direction,direction)
            self.grid[pos+direction],self.grid[pos] = self.grid[pos],self.grid[pos+direction]


    def on_grid(self,point):
        return 0<= point.imag <= self.numrows and 0<= point.real <= self.numcols

    def step(self,direction):
        self.stepnum+=1
        if self.can_move(self.robot_pos,direction):
            self.move(self.robot_pos,direction)
            self.robot_pos+=direction

    def score(self):
        output=0
        for k,v in self.grid.items():
            if v == 'O':
                output+=(int(k.real)+(int(k.imag)*100))
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
        output+=f'{self.stepnum}\n'
        return output

def part1(inputdata=testdata.split('\n\n')):
    w=Warehouse(inputdata)
    while len(w.instructions)>0:
        w.step()
    return w.grid.score()


def part2(inputdata=testdata.split('\n')):
    pass


def day15_01():
    """Run part 1 of Day 15's code"""
    path = "./input/15.txt"
    inputdata=get_file(path)
    print("1501:", part1(inputdata.split('\n\n')))


def day15_02():
    """Run part 2 of Day 15's code"""
    path = "./input/15.txt"
    print("1502:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day15_01()
    #day15_02()

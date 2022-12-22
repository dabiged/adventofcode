from lib.filehelper import get_bald_string_list_from_file
# pylint: disable=missing-module-docstring
from collections import defaultdict
import time
import copy


test_data='''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''.split('\n')

def blankspace():
    return ' '

class Maze():
    def __init__(self,maze,instr):
        self.inputmaze=maze
        self.instr=instr
        self.dirs=[]
        self.maze=defaultdict(blankspace)
        self.dims=None
        self.draw=True
        self.part1=False

    def parse(self):
        maxcol=0
        for rownum,row in enumerate(self.inputmaze):
            for colnum,char in enumerate(row):
                maxcol=max(maxcol,colnum)
                self.maze[colnum+rownum*1j]=char
        self.maxdims=(rownum+1,maxcol+1)

    def parseinstr(self):
        self.dirs=[self.instr[0]]
        for char in self.instr[1:]:
            if char.isnumeric() and self.dirs[-1].isnumeric():
                self.dirs[-1]+=char
            elif char.isnumeric() and self.dirs[-1].isalpha():
                self.dirs.append(char)
            elif char in ['L','R']:
                self.dirs.append(char)
            else:
                raise ValueError

    def start_walk(self):
        self.direction=1
        for col in range(self.maxdims[1]):
            if self.maze[col+0*1j] == '.':
                self.currloc=col+0*1j
                break

    def walk(self,instr):
        if instr == 'L':
            self.direction*=-1j
        elif instr == 'R':
            self.direction*=1j
        elif instr.isnumeric():
            instr=int(instr)
            for _ in range(instr):
                nextloc= self.currloc+self.direction
                if self.maze[nextloc] not in ['#', ' ']:
                    if self.direction == 1j and self.draw:
                        self.maze[self.currloc]='v'
                    if self.direction == -1j and self.draw:
                        self.maze[self.currloc]='A'
                    if self.direction == 1 and self.draw:
                        self.maze[self.currloc]='>'
                    if self.direction == -1 and self.draw:
                        self.maze[self.currloc]='<'
                    self.currloc=nextloc
                elif self.maze[nextloc] == '#':
                    pass
                elif self.maze[nextloc] == ' ':
                    if self.part1:
                        self.currloc=self.wrap()
                    else:
                        nextloc,nextdir =self.cubewrap()
                        if self.maze[nextloc] == '#':
                            pass
                        else :
                            self.currloc=nextloc
                            self.direction=nextdir

    def wrap(self):
        if self.direction == 1:
            for col in range(0,int(self.currloc.real)):
                if self.maze[col +int(self.currloc.imag)*1j] not in ['#',' ']:
                    return col+int(self.currloc.imag)*1j
                elif self.maze[col +int(self.currloc.imag)*1j]=='#':
                    return self.currloc
        if self.direction == 1j:
            for row in range(0,int(self.currloc.imag)):
                if self.maze[int(self.currloc.real)+row*1j] not in ['#',' ']:
                    return self.currloc.real+row*1j
                elif self.maze[self.currloc.real+row*1j]=='#':
                    return self.currloc
        if self.direction == -1j:
            for row in range(self.maxdims[0], int(self.currloc.imag),-1):
                if self.maze[int(self.currloc.real)+row*1j] not in ['#',' ']:
                    return self.currloc.real+row*1j
                elif self.maze[self.currloc.real+row*1j]=='#':
                    return self.currloc
        if self.direction == -1:
            for col in range(self.maxdims[1],int(self.currloc.real),-1):
                if self.maze[col +int(self.currloc.imag)*1j] not in ['#',' ']:
                    return col+int(self.currloc.imag)*1j
                elif self.maze[col +int(self.currloc.imag)*1j]=='#':
                    return self.currloc

    def blocked(self,nextloc):
        if self.maze[nextloc] == '#':
            return True
        elif self.maze[nextloc] == '.':
            return False

    def cubewrap(self):
        if 0 <= int(self.currloc.imag) <= 49 and int(self.currloc.real) == 149:
            gate=' D1 '
            newdir=self.direction*-1
            newloc= 99 + (149-int(self.currloc.imag))*1j
        elif 50 <= int(self.currloc.imag) <= 99 and int(self.currloc.real) == 99:
            gate=' C2 '
            newdir=self.direction*-1j
            newloc=  50+int(self.currloc.imag) +49j
        elif 100 <= int(self.currloc.imag) <= 149 and int(self.currloc.real) == 99:
            gate=' D2 '
            newdir=self.direction*-1
            newloc= 149+(149-int(self.currloc.imag))*1j
        elif 150 <= int(self.currloc.imag) <= 199 and int(self.currloc.real) == 49:
            gate=' A2 '
            newdir=self.direction*-1j
            newloc= int(self.currloc.imag)-100+149j
        elif 150 <= int(self.currloc.imag) <= 199 and int(self.currloc.real) == 0:
            gate=' F2 '
            newdir=self.direction*-1j
            newloc= int(self.currloc.imag)-100 + 0j
        elif 100 <= int(self.currloc.imag) <= 149 and int(self.currloc.real) == 0:
            gate=' G2 '
            newdir=self.direction*-1
            newloc= 50+(149-int(self.currloc.imag))*1j
        elif 50 <= int(self.currloc.imag) <= 99 and int(self.currloc.real) == 50:
            gate=' B1 '
            newdir=self.direction*-1j
            newloc= -50+int(self.currloc.imag)+100j
        elif 0 <= int(self.currloc.imag) <= 49 and int(self.currloc.real) == 50:
            gate=' G1 '
            newdir=self.direction*-1
            newloc= 0 + (149-int(self.currloc.imag))*1j
        elif int(self.currloc.imag) == 0 and 50 <= int(self.currloc.real) <= 99:
            gate=' F1 '
            newdir=self.direction*1j
            newloc= 0 + (int(self.currloc.real)+100)*1j
        elif int(self.currloc.imag) == 0 and 100 <= int(self.currloc.real) <= 149:
            gate=' E1 '
            newdir=self.direction*1
            newloc= int(self.currloc.real)-100+199j
        elif int(self.currloc.imag) == 49 and 100 <= int(self.currloc.real) <= 149:
            gate=' C1 '
            newdir=self.direction*1j
            newloc=  99 + (int(self.currloc.real)-50)*1j
        elif int(self.currloc.imag) == 149 and 50 <= int(self.currloc.real) <= 99:
            gate=' A1 '
            newdir=self.direction*1j
            newloc= 49+(100+self.currloc.real)*1j
        elif int(self.currloc.imag) == 199 and 0 <= int(self.currloc.real) <= 49:
            gate=' E2 '
            newdir=self.direction*1
            newloc= 100+int(self.currloc.real)+0j
        elif int(self.currloc.imag) == 100 and 0 <= int(self.currloc.real) <= 49:
            gate=' B2 '
            newdir=self.direction*1j
            newloc= 50+(50+int(self.currloc.real))*1j
        else:
            raise ValueError(self.currloc)

        return newloc,newdir

    def walkmaze(self):
        self.parse()
        self.parseinstr()
        self.start_walk()
        for i, instr in enumerate(self.dirs):
            self.stepnum=i
            self.walk(instr)

        answ=0
        answ+=(int(self.currloc.imag)+1)*1000
        answ+=(int(self.currloc.real)+1)*4
        if self.direction == 1:
            answ+=0
        if self.direction == 1j:
            answ+=1
        if self.direction == -1:
            answ+=2
        if self.direction == -1j:
            answ+=3
        return answ

    def __repr__(self):
        maze=[]
        for rownum in range(self.maxdims[0]):
            thisrow=''
            for colnum in range(self.maxdims[1]):
                if colnum+rownum*1j != self.currloc:
                    thisrow+= self.maze[colnum+rownum*1j]
                else:
                    thisrow+='C'
            maze.append(thisrow)
        maze.append('')
        maze.append(f'Current: {self.currloc}, Dir: {self.direction}')
        return "\n".join(maze)




def main1(input_data):
    mymaze=Maze(input_data[:-2],input_data[-1])
    mymaze.part1=True
    return mymaze.walkmaze()

def main2(input_data):
    mymaze=Maze(input_data[:-2],input_data[-1])
    mymaze.part2=False
    return mymaze.walkmaze()

def day22_01():
    """Run part 1 of Day 22's code"""
    path = "./input/input_22.txt"
    print("2201:",main1(get_bald_string_list_from_file(path)))

def day22_02():
    """Run part 2 of Day 22's code"""
    path = "./input/input_22.txt"
    print("2202:",main2(get_bald_string_list_from_file(path)))

if __name__ == "__main__":
    day22_01()
    day22_02()


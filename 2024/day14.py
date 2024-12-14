from lib.filehelper import file_to_str_array
from collections import defaultdict
from collections import deque
import re
# pylint: disable=missing-module-docstring

testdata='''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''



class Grid:
    def __init__(self,inputdata,numrows=103,numcols=101):
        self.inputdata=inputdata
        self.diag_neighbours=[up*1j+down for up in [-1,1] for down in [-1,1] ]
        self.direct_neighbours=[1,-1,1j,-1j]
        self.reset_grid()
        self.numrows=numrows
        self.numcols=numcols
        self.velocities={}
        self.positions={}
        linenum=0
        for line in inputdata:
            for section in line.split():
                vals=section.split('=')[1]
                values=vals.split(',')
                if 'p=' in section:
                    self.positions[linenum]=int(values[0])+int(values[1])*1j
                elif 'v=' in section:
                    self.velocities[linenum]=int(values[0])+int(values[1])*1j
                else:
                    raise
            linenum+=1

    def reset_grid(self):
        self.grid=defaultdict(str)
        for rownum,row in enumerate(self.inputdata):
            for colnum, char in enumerate(row):
                self.grid[colnum+rownum*1j]='.'

    def on_grid(self,point):
        return 0<= point.imag <= self.numrows and 0<= point.real <= self.numcols

    def step(self,steps):
        for k,p in self.positions.items():
            v=self.velocities[k]
            re = ( int(p.real) + (steps * int(v.real)) ) % self.numcols
            im = ( int(p.imag) + (steps * int(v.imag)) ) % self.numrows
            self.positions[k]=re+im*1j
            

    def run(self,n):
        for _ in range(n):
            self.step()


    def score(self):
        midcol=self.numcols//2 
        midrow=self.numrows//2 
        Q = {1: (0,midrow,0,midcol),
             2: (midrow+1,self.numrows,0,midcol),
             3: (0,midrow,midcol+1,self.numcols),
             4: (midrow+1,self.numrows,midcol+1,self.numcols)}
        output=1
        for minrow,maxrow,mincol,maxcol in Q.values():
            quadrant=0
            for row in range(minrow,maxrow):
                for col in range(mincol,maxcol):
                    quadrant+=sum(row*1j+col == i for i in self.positions.values())
            output*=quadrant
        return output

    def __len__(self):
        return self.numrows*self.numcols

    def __str__(self):
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                if re+im*1j in self.positions.values():
                    #output+=str(sum([ i == re+im*1j for i in self.positions.values() ]))
                    output+='#'
                else:
                    output+='.'
            output+='\n'
        return output

def part1(inputdata=testdata.split('\n')):
    g=Grid(inputdata)
    g.step(100)
    return g.score()

def part2(inputdata=testdata.split('\n')):
    ''' For part 2 there is a cycle in the output where everything lines up on step 51, then every 103 steps thereafter.
    by lookat at every 103th subsequent step I was able to see the tree'''
    g=Grid(inputdata)
    i=51
    g.step(51)
    g.step(68*103)
    print(g)
    print(g.score())
    return 51+(68*103)

def day14_01():
    """Run part 1 of Day 14's code"""
    path = "./input/14.txt"
    print("1401:", part1(file_to_str_array(path)))


def day14_02():
    """Run part 2 of Day 14's code"""
    path = "./input/14.txt"
    print("1402:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day14_01()
    day14_02()





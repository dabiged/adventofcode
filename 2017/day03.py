from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

import math

def cardinal_points(ringnum):
    i=ringnum
    north=(2*i+1)**2-(7*i)
    east=(2*i+1)**2-(5*i)
    south=(2*i+1)**2-(3*i)
    west=(2*i+1)**2-(i)

    return [south,east,north,west]

def gen_star(num):
    ## the optimal solution is to work to a cardinal point on the map.
    # then step in the number of rings from the centre.
    ring=math.ceil(((num**0.5)-1)/2)
    dists=[]
    for point in cardinal_points(ring):
        dists.append(abs(num-point))
    return min(dists)+ring




class board():
    def __init__(self):
        self.loc=0+0*1j
        self.squares={}
        self.squares[self.loc]=1
        self.up=0

    def next_val(self):
        val=0
        for neighbour in self.neighbours():
            if neighbour in self.squares.keys():
                val+=self.squares[neighbour]
        self.squares[self.loc]=val


    def iter(self):
        if (self.loc.real+self.loc.imag == 1 ) and self.loc.real>0 and self.loc.imag<=0:
            self.up=1j
        if abs(self.loc.imag)-abs(self.loc.real) == 0:
            if self.loc.imag >0 and self.loc.real > 0:
                self.up=-1
            elif self.loc.imag>0 and self.loc.real <0:
                self.up=-1j
            elif self.loc.imag<=0 and self.loc.real <=0:
                self.up=1
        self.loc+=self.up
        self.next_val()

    def neighbours(self):
        return [self.loc+1j-1,self.loc+1j,self.loc+1j+1,
                self.loc-1, self.loc+1,
                self.loc-1j-1,self.loc-1j,self.loc-1j+1]


def day03_01():
    """Run part 1 of Day 1's code"""
    print('0301:', gen_star(312051))



def day03_02():
    """Run part 2 of Day 1's code"""
    myboard=board()
    while max(myboard.squares.values()) <312051:
        myboard.iter()
    print('0301:', max(myboard.squares.values()))


if __name__ == "__main__":
    day03_01()
    day03_02()

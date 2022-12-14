from lib.filehelper import file_to_str_array
from collections import defaultdict
import cmath
import math
# pylint: disable=missing-module-docstring


test_input='''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''.split('\n')

class UnknownDirection(Exception):
    pass

def pair2cmp(csv):
    values=csv.split(',')
    return int(values[0])+int(values[1])*1j

class CaveSystem():
    def __init__(self,walldefs):
        self.walldefs=walldefs
        self.a=defaultdict(lambda: '.')
        self.a[500+0j]='+'

        self.printsteps=[1,2,5,22,24,25]
        self.makewalls()

    def run2(self):
        bottom=max([ int(i.imag) for i in self.a.keys()]) +2
        boundary=500+bottom+2
        for real in range(-boundary,boundary):
            self.a[real+bottom*1j]='#'
        step=self.run()
        return step+1

    def run(self):
        step=0
        while self.step():
            step+=1
        return step



    def step(self):
        currloc=500+0j
        while currloc.imag < 1000.0:
            if self.a[currloc+1j] == '.':
                # below is empty, move down
                currloc=currloc+1j
                continue
            elif self.a[currloc+1j] in ['#','o']:
                # below is wall or sand
                    # try diag left
                if self.a[currloc -1+1j] in ['#','o']:
                    if self.a[currloc+1+1j] in ['#','o']:
                        if currloc==500+0j:
                            return False
                        self.a[currloc]='o'
                        return True
                    else:
                        currloc+=1+1j
                else:
                    currloc+=-1+1j
            else:
                raise UnknownDirection

        return False


    def makewalls(self):
        for walldef in self.walldefs:
            points=walldef.split(' -> ')
            oldpoint=None
            for point in points:
                if not oldpoint:
                    oldpoint = pair2cmp(point)
                    continue
                newpoint = pair2cmp(point)

                if oldpoint.real == newpoint.real:
                    for i in range(min(int(oldpoint.imag),int(newpoint.imag)),max(int(oldpoint.imag),int(newpoint.imag))+1):
                        self.a[int(oldpoint.real)+i*1j] = '#'
                elif oldpoint.imag == newpoint.imag:
                    for i in range(min(int(oldpoint.real),int(newpoint.real)),max(int(oldpoint.real),int(newpoint.real))+1):
                        self.a[i+oldpoint.imag*1j] = '#'
                oldpoint=newpoint


    def __repr__(self):
        minreal=min([ int(i.real) for i in self.a.keys()])
        maxreal=max([ int(i.real) for i in self.a.keys()])
        minimag=0
        maximag=max([ int(i.imag) for i in self.a.keys()])

        wholecave=[]
        for im in range(minimag,maximag+1):
            thisrow=''
            for re in range(minreal,maxreal+1):
                thisrow+=self.a[re+im*1j]
            wholecave.append(thisrow)

        return '\n'.join(wholecave)

#print(CaveSystem(test_input).run())

def day14_01():
    """Run part 1 of Day 9's code"""
    path = "./input/input_14.txt"
    print("1401:",CaveSystem(file_to_str_array(path)).run())

def day14_02():
    """Run part 2 of Day 9's code"""
    path = "./input/input_14.txt"
    print("1402:",CaveSystem(file_to_str_array(path)).run2())

if __name__ == "__main__":
    day14_01()
    day14_02()

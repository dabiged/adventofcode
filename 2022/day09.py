from lib.filehelper import file_to_str_array
import cmath
import math
# pylint: disable=missing-module-docstring


test_input=''''''.split('\n')

class UnknownDirection(Exception):
    pass


class RopeBoard():
    def __init__(self,instrs):
        self.instrs=instrs
        self.head=0+0j
        self.tail=0+0j
        self.visited=set()

    def run(self):
        self.visited.add(self.tail)
        for instr in self.instrs:
            self.step(instr)

        return len(self.visited)

    def step(self,instr):
        ludr = instr.split()[0]
        count = int(instr.split()[1])
        for i in range(count):  
            self.movehead(ludr)
            self.movetail()
            self.visited.add(self.tail)

    def movehead(self,direction):
        if direction == 'U':
            self.head+= 1j
        elif direction == 'D':
            self.head+= -1j
        elif direction == 'L':
            self.head+= -1
        elif direction == 'R':
            self.head+= 1
        else:
            raise UnknownDirection

    def movetail(self):
        diff = self.head-self.tail
        if diff in [0,1,-1,1j,-1j, 1+1j, 1-1j, -1+1j, -1-1j]:
            pass
        elif diff in (2, -2, -2j, 2j):
            if diff == 2:
                self.tail+=1
            elif diff == -2:
                self.tail+= -1
            elif diff == -2j:
                self.tail+= -1j
            elif diff == 2j:
                self.tail+=1j
        else:
            direction=cmath.phase(diff)
            if -math.pi < direction < -math.pi/2:
                self.tail += -1-1j
            elif -math.pi/2 < direction < 0:
                self.tail +=1-1j
            elif 0 < direction < math.pi/2:
                self.tail += 1+1j
            elif math.pi/2 < direction < math.pi:
                self.tail += -1+1j







def main1(data):
    r=RopeBoard(data)
    return r.run()


def main2(data):
    pass

def day09_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_09.txt"
    print("0901:", main1(file_to_str_array(path)))

def day09_02():
    """Run part 2 of Day 1's code"""
    path = "./input/input_09.txt"
    print("0902:")

if __name__ == "__main__":
    day09_01()
    day09_02()

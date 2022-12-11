from lib.filehelper import file_to_str_array
import cmath
import math
# pylint: disable=missing-module-docstring


test_input=''''''.split('\n')

class UnknownDirection(Exception):
    pass


class RopeBoard():
    def __init__(self,instrs,length=2):
        self.instrs=instrs
        self.rope=[]
        for i in range(length):
            self.rope.append(0+0j)
        self.visited=set()

    def run(self):
        self.visited.add(self.rope[-1])
        for instr in self.instrs:
            self.step(instr)

        return len(self.visited)

    def step(self,instr):
        ludr = instr.split()[0]
        count = int(instr.split()[1])
        for i in range(count):
            self.movehead(ludr)
            self.moverope()
            self.visited.add(self.rope[-1])

    def movehead(self,direction):
        if direction == 'U':
            self.rope[0]+= 1j
        elif direction == 'D':
            self.rope[0]+= -1j
        elif direction == 'L':
            self.rope[0]+= -1
        elif direction == 'R':
            self.rope[0]+= 1
        else:
            raise UnknownDirection

    def moverope(self):
        for i, knotloc in enumerate(self.rope[1:],start=1):
            diff = self.rope[i-1]-self.rope[i]
            if diff in [0,1,-1,1j,-1j, 1+1j, 1-1j, -1+1j, -1-1j]:
                pass
            elif diff in (2, -2, -2j, 2j):
                if diff == 2:
                    self.rope[i]+=1
                elif diff == -2:
                    self.rope[i]+= -1
                elif diff == -2j:
                    self.rope[i]+= -1j
                elif diff == 2j:
                    self.rope[i]+=1j
            else:
                direction=cmath.phase(diff)
                if -math.pi < direction < -math.pi/2:
                    self.rope[i] += -1-1j
                elif -math.pi/2 < direction < 0:
                    self.rope[i] +=1-1j
                elif 0 < direction < math.pi/2:
                    self.rope[i] += 1+1j
                elif math.pi/2 < direction < math.pi:
                    self.rope[i] += -1+1j

def main1(data):
    r=RopeBoard(data)
    return r.run()


def main2(data):
    r=RopeBoard(data,10)
    return r.run()

def day09_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_09.txt"
    print("0901:", main1(file_to_str_array(path)))

def day09_02():
    """Run part 2 of Day 1's code"""
    path = "./input/input_09.txt"
    print("0902:", main2(file_to_str_array(path)))

if __name__ == "__main__":
    day09_01()
    day09_02()

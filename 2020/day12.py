"""
AOC day 12 2018
"""
from lib.filehelper import file_to_str_array
from itertools import cycle
# pylint: disable=missing-module-docstring

class NavComp:
    
    def __init__(self,listofinstr):
        '''
        We are going to keep track of the ship by recoring its direction
        and its position.
        '''
        self.dir2nums={'E':[1,0],'N':[0,1],'W':[-1,0],'S':[0,-1]}
        self.dir2angs={'E':90,'N':0,'W':270,'S':180}
        self.direction = 'E'
        self.position=[0,0]
        self.read_instr(listofinstr)

    def read_instr(self,listofinstr):
        for instr in listofinstr:
            #print(instr)
            self.update_position(instr)
        return self.dist_from_origin()

    def update_position(self,instr):
        '''Update the location of the boat'''
        action, value = instr[0],instr[1:]
        if action in ['E','S','N','W']:
            for coord in [0,1]:
                self.position[coord] += int(value)*self.dir2nums[action][coord]
        elif action in ['L','R']:
            self.turn(instr)
        elif action =='F':
            for coord in [0,1]:
                self.position[coord] += int(value)*self.dir2nums[self.direction][coord]
        else:
            print('Unknown Instr', instr)
        #print(self.direction, self.position)

    def turn(self,instr):
        turndir,value = instr[0],int(instr[1:])
        # Turndir in ['R','L'], value in [0,90,180,270]
        # Angle increases or decreases
        angsgn= 1 if turndir=='R' else -1
        # new compass heading
        compass_heading = (self.dir2angs[self.direction]+angsgn*value) % 360
        for direction,heading in self.dir2angs.items():
            if heading== compass_heading:
                self.direction=direction


#    def turn_left (self,angle):
#        while i != self.position:
#            cycle(self.turnleft)
#        for i in range(angle//90):
#            self.direction=cycle(self.turnleft)
#



    def dist_from_origin(self):
        return abs(self.position[0])+abs(self.position[1])


            

def day12_01():
    """Run part 1 of Day 12's code"""
    path = "./input/12/input.txt"
    testnavcomp = NavComp(file_to_str_array(path))
    result = testnavcomp.dist_from_origin()
    print(f'1201: {result}')

def day12_02():
    """Run part 2 of Day 12's code"""
    path = "./input/12/input.txt"
    result=""
    print(f'1202: {result}')

if __name__ == "__main__":
    day12_01()
    #day12_02()

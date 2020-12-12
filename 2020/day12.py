"""
AOC day 12 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class NavComp:
    ''' A computer that takes a  series of instructions and navigates a ship'''
    def __init__(self,listofinstr):
        '''
        We are going to keep track of the ship by recording its direction
        and its position.
        '''
        # Some helper dictionaries.
        # This one tells us how to move in cartesian space if we are facing a cardinal direction
        self.dir2nums={'E':[1,0],'N':[0,1],'W':[-1,0],'S':[0,-1]}
        # This one maps cardinal points to compass points.
        self.dir2angs={'E':90,'N':0,'W':270,'S':180}
        # These are the two state variables.
        self.direction = 'E'
        self.position=[0,0]
        # Read instructions and move ship.
        self.read_instr(listofinstr)

    def read_instr(self,listofinstr):
        '''
        Read a series of instructions and undertake a series of actions to move the ship'''
        for instr in listofinstr:
            self.update_position(instr)
        return self.dist_from_origin()

    def update_position(self,instr):
        '''Update the location of the boat'''
        action, value = instr[0],instr[1:]
        if action in ['E','S','N','W']:
            # Move in a cardinal direction without reorienting
            for coord in [0,1]:
                self.position[coord] += int(value)*self.dir2nums[action][coord]
        elif action in ['L','R']:
            # Turn the ship left or right in increments of 90 degrees
            self.turn(instr)
        elif action =='F':
            # move the ship forward along its current heading.
            for coord in [0,1]:
                self.position[coord] += int(value)*self.dir2nums[self.direction][coord]
        else:
            print('Unknown Instr', instr)

    def turn(self,instr):
        '''executes the turning of the ship.'''
        turndir,value = instr[0],int(instr[1:])
        # Turndir in ['R','L'], value in [0,90,180,270]
        # Angle increases or decreases
        angsgn= 1 if turndir=='R' else -1
        # new compass heading
        # 1.               convert the current direction
        #                  to a compass bearing.
        # 2.                                            Change the compass bearing
        compass_heading = (self.dir2angs[self.direction]+angsgn*value) % 360
        for direction,heading in self.dir2angs.items():
            # convert the compass bearing into a cardinal direction
            if heading== compass_heading:
                self.direction=direction

    def dist_from_origin(self):
        ''' Returns the manhattan distance of the boat from the origin'''
        return abs(self.position[0])+abs(self.position[1])

class NavCompPart2:
    '''Another nav computer for moving a ship.
    This one uses a waypoint to navigate instead of ships heading'''
    def __init__(self,listofinstr):
        '''
        We are going to keep track of the ship by tracking the waypoint location
        and the ships position position.
        '''
        self.dir2nums={'E':[1,0],'N':[0,1],'W':[-1,0],'S':[0,-1]}
        self.waypoint=[10,1]
        self.position=[0,0]
        self.read_instr(listofinstr)

    def read_instr(self,listofinstr):
        '''
        Read a series of instructions and undertake a series of actions to move the ship'''
        for instr in listofinstr:
            self.update_position(instr)
        return self.dist_from_origin()

    def update_position(self,instr):
        '''Update the location of the boat using the way point.'''
        action, value = instr[0],instr[1:]
        if action in ['E','S','N','W']:
            # move waypoint
            for coord in [0,1]:
                self.waypoint[coord] += int(value)*self.dir2nums[action][coord]
        elif action in ['L','R']:
            # Rotate waypoint
            self.turnwaypoint(instr)
        elif action =='F':
            # Drive towards waypoint
            for coord in [0,1]:
                self.position[coord] += int(value)*self.waypoint[coord]
        else:
            print('Unknown Instr', instr)

    def turnwaypoint(self,instr):
        '''Rotate the waypoint about the origin according to the instruction'''
        turndir,value = instr[0],int(instr[1:])
        # Turndir in ['R','L'], value in [0,90,180,270]
        # Angle increases or decreases
        for _ in range((value//90)):
            # perform a number of 90degree turns
            if turndir == 'L':
                self.turnleft()
            elif turndir == 'R':
                self.turnright()
            else:
                print("SOmething went wrong in turnwaypoiint for instr:",instr)

    def turnright(self):
        '''rotate the waypoint once about the origin 90 degrees clockwise'''
        self.waypoint[0], self.waypoint[1] = self.waypoint[1], -self.waypoint[0]

    def turnleft(self):
        '''rotate the waypoint once about the origin 90 degrees counter-clockwise'''
        self.waypoint[0], self.waypoint[1] = -self.waypoint[1], self.waypoint[0]

    def dist_from_origin(self):
        ''' Returns the manhattan distance of the boat from the origin'''
        return abs(self.position[0])+abs(self.position[1])

def day12_01():
    """Run part 1 of Day 12's code"""
    path = "./input/12/input.txt"
    testnavcomp = NavComp(file_to_str_array(path))
    result = testnavcomp.dist_from_origin()
    print(f'1201: Ship distance from origin: {result}')

def day12_02():
    """Run part 2 of Day 12's code"""
    path = "./input/12/input.txt"
    testnavcomp = NavCompPart2(file_to_str_array(path))
    result = testnavcomp.dist_from_origin()
    print(f'1202: Ship distance from origin using waypoints: {result}')

if __name__ == "__main__":
    day12_01()
    day12_02()

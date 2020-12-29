"""
AOC day 24 2018
"""
from collections import defaultdict
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class HexBoard:
    '''      
            /  \
           |    |  col +1
            \  /
       row+1     row+1,col+1



    '''
    def __init__(self, instr):
        '''Read in instructions and initialise the hex board'''
        self.board=defaultdict(int)
        self.instructions=[]
        with open(instr) as f:
            instructions = f.read()
        for instr in instructions.split('\n'):
            # instr is a str
            i=0
            if i == 0:
                print(instr)
            thisinstr=[]
            while i < len(instr):
                if instr[i] in ('n','s'):
                    thisinstr.append(instr[i:i+2])
                    i+=2
                elif instr[i] in ('e','w'):
                    thisinstr.append(instr[i])
                    i+=1
                else:
                    raise ValueError(f'Unknown Direction found in instruction\n{instr}\nAt location:{i}')
            self.instructions.append(thisinstr)



    def get_neighbours(self,rcloc):
        ''' given a tuple location rcloc, give all neighbours'''
        for loc in [self.west(rcloc),self.northwest(rcloc),self.northeast(rcloc),\
                    self.east(rcloc),self.southeast(rcloc),self.southwest(rcloc)]:
            yield loc

    def west(self,rcloc):
        row,col=rcloc
        return (row,col-1)

    def southwest(self,rcloc):
        row,col=rcloc
        return (row-1,col-1)

    def southeast(self,rcloc):
        row,col=rcloc
        return (row-1,col)

    def east(self,rcloc):
        row,col=rcloc
        return (row,col+1)

    def northeast(self,rcloc):
        row,col=rcloc
        return (row+1,col+1)

    def northwest(self,rcloc):
        row,col=rcloc
        return (row+1,col)



def day24_01():
    """Run part 1 of Day 24's code"""
    path = "./input/24/input.txt"
    result=""
    print(f'2401: {result}')

def day24_02():
    """Run part 2 of Day 24's code"""
    path = "./input/24/input.txt"
    result=""
    print(f'2402: {result}')

if __name__ == "__main__":
    day24_01()
    #day24_02()

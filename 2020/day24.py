"""
AOC day 24 2018
"""
from collections import defaultdict
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class HexBoard:
    '''Create a hexagon based board.
    Offset odd rows by 1/2 space.
    left and right sides of the hexagons are vertical.
    '''
    def __init__(self, instr):
        '''Read in instructions and initialise the hex board'''
        self.board={}
        self.instructions=[]
        with open(instr) as f:
            instructions = f.read()
        for instr in instructions.split('\n'):
            if instr == '':
                # Skip blank lines
                continue
            # instr is a str
            i=0
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
    def __repr__(self):
        alloutput=''
        minrow,maxrow,mincol,maxcol =0,0,0,0
        for row,col in self.board:
            minrow=min(minrow,row)
            maxrow=max(maxrow,row)
            mincol=min(mincol,col)
            maxcol=max(maxcol,col)
        alloutput+=f'Board Dimensions:\nRows: {minrow}-{maxrow}\nCols: {mincol}-{maxcol}\n'
        minrow,maxrow,mincol,maxcol =-10,10,-10,10
        for row in range(maxrow+1,minrow-2,-1):
            if row % 2 ==1:
                output=' '
            else:
                output=''
            for col in range(mincol-1,maxcol+2):
                output+=str(self.board.get((row,col),'.'))+' '
            alloutput+=output+'\n'
        alloutput+='Black Tiles: '+str(self.count_black_tiles())

        return alloutput



    def west(self,rcloc):
        row,col=rcloc
        return (row,col-1)

    def east(self,rcloc):
        row,col=rcloc
        return (row,col+1)

    def southwest(self,rcloc):
        row,col=rcloc
        if abs(row) % 2 == 1:
            return (row-1,col)
        return (row-1,col-1)

    def southeast(self,rcloc):
        row,col=rcloc
        if abs(row) % 2 == 1:
            return (row-1,col+1)
        return (row-1,col)

    def northeast(self,rcloc):
        row,col=rcloc
        if abs(row) % 2 == 1:
            return (row+1,col+1)
        return (row+1,col)

    def northwest(self,rcloc):
        row,col=rcloc
        if abs(row) % 2 == 1:
            return (row+1,col)
        return (row+1,col-1)

    def move(self,instr,loc):
        '''Given a single movement, change the location'''
        if   instr == 'e':
            return self.east(loc)
        elif instr == 'w':
            return self.west(loc)
        elif instr == 'nw':
            return self.northwest(loc)
        elif instr == 'ne':
            return self.northeast(loc)
        elif instr == 'sw':
            return self.southwest(loc)
        elif instr == 'se':
            return self.southeast(loc)
        raise ValueError(f'Unknown Instruction: {instr}')

    def locate_tile(self,instruction):
        ''' Read an instruction and return the location of the tile reached in that instruction'''
        location=(0,0)
        for instr in instruction:
            location=self.move(instr,location)
        return location


    def run_instr(self,instruction):
        '''Read an instruction and flip the tile at the location given'''
        location=self.locate_tile(instruction)
        current_value=self.board.get(location,0)
        if current_value == 0:
            self.board[location] =1
        elif current_value==1:
            del self.board[location] 

    def setup(self):
        ''' Run all instructions in the instruction list'''
        for instruction in self.instructions:
            self.run_instr(instruction)

    def count_black_tiles(self):
        blacktiles=0
        for location,numflips in self.board.items():
            if numflips==1:
                blacktiles+=1
        return blacktiles

    def count_occupied(self,loc):
        numoccupied=0
        for thispoint in self.get_neighbours(loc):
            if self.board.get(thispoint,0) ==1:
                numoccupied +=1
        return numoccupied

    def get_neighbours(self,rcloc):
        ''' given a tuple location rcloc, give all neighbours'''
        for loc in [self.west(rcloc),self.northwest(rcloc),self.northeast(rcloc),\
                    self.east(rcloc),self.southeast(rcloc),self.southwest(rcloc)]:
            yield loc

    def step(self):
        '''Step the tile floor 1 day'''
        # Count the number of neighbours of each hex.

        black_tile_num_neighbours={}
        # Note the use of a set comprehension here so we only count each one once.
        all_tiles_and_neighbours=set(self.board)
        all_tiles_and_neighbours|={neighbourhex for centrehex in self.board\
                    for neighbourhex in self.get_neighbours(centrehex)}

        for thishex in all_tiles_and_neighbours:
            black_tile_num_neighbours[thishex]=self.count_occupied(thishex)
        for thishex, numneighbours in black_tile_num_neighbours.items():
            if self.board.get(thishex,0) == 1 and ( numneighbours ==0 or numneighbours >2 ):
                del self.board[thishex] 
            elif self.board.get(thishex,0) == 0 and numneighbours == 2:
                self.board[thishex]=1

def day24_01():
    """Run part 1 of Day 24's code"""
    path = "./input/24/input.txt"
    myhex = HexBoard(path)
    myhex.setup()
    result = myhex.count_black_tiles()
    print(f'2401: Number of Black tiles: {result}')

def day24_02():
    """Run part 2 of Day 24's code"""
    path = "./input/24/input.txt"
    myhex = HexBoard(path)
    myhex.setup()
    for _ in range(100):
        myhex.step()
    result= myhex.count_black_tiles()
    print(f'2402: Number of black tiles after 100 days: {result}')

if __name__ == "__main__":
    day24_01()
    day24_02()

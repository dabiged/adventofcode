"""
AOC day 20 2018
"""
import math
from collections import deque
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Tile:
    ''' A tile object

    it consists of a 10x10 chars.

    storage is a dict with tuple keys, and char values.'''
    def __init__(self,tilenum: int, tile: list, verbose=False):
        '''Initialise a tile'''
        self.pairs=set()
        self.tilenum = tilenum
        self.borders=[]

        self.tile=[i for i in tile]
        #self.tile.append(i) for i in tile
        # top, bottom, left, right
        self.borders=[self.top(), self.bottom(), self.left(), self.right()]

        reversed_borders=[i[::-1] for i in self.borders]
        for revborder in reversed_borders:
            self.borders.append(revborder)

        if verbose:
            print('Tile Number')
            print(self.tilenum)
            print('Borders')
            print(self.borders)
            print('Pairs')
            print(self.pairs)
            print('tile')
            print(self.tile)

    def pair(self,other):
        '''Check to see if this tile shares a border with other tile'''
        for thistileborder in self.borders:
            for othertileborder in other.borders:
                if thistileborder == othertileborder:
                    if self.tilenum != other.tilenum:
                        self.pairs|={other.tilenum}
                        return True, thistileborder
        return False, None

    def trim_sides(self):
        ''' Remove all borders from tile
        result has 2 less cols and 2 less rows.'''
        return [ row[1:-1] for row in self.tile[1:-1]]
    def left(self):
        ''' return the left side of the tile'''
        return ''.join([row[0] for row in self.tile])
    def right(self):
        ''' return the right side of the tile'''
        return ''.join([row[-1] for row in self.tile])
    def top(self):
        ''' return the top side of the tile'''
        return self.tile[0]
    def bottom(self):
        ''' return the bottom side of the tile'''
        return self.tile[-1]

    def flip(self):
        ''' perform a horizontal flip '''
        return  [''.join(row[::-1]) for row in self.tile]

    def rotate(self):
        ''' rotate the tile '''
        return [''.join(s) for s in zip(*self.tile[::-1])]

    def orientations(self):
        '''A generator that return all 8 possible orientations of a tile'''
        for _ in range(0,4):
            yield Tile(self.tilenum,[''.join(row) for row in self.rotate()])
            self.tile=self.rotate()
            yield Tile(self.tilenum,[''.join(row) for row in map(list,zip(*self.tile))])

    def find_monsters(self):
        '''Search the tile for any signs of monsters'''
        monster=['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']
        monstercount=0
        # For each location in the tile (less the length/height of the monster)
        for rowloc in range(len(self.tile)-len(monster)+1):
            for colloc in range(len(self.tile[0])-len(monster[0])+1):
                is_monster=True
                for monsterrow in range(len(monster)):
                    for monstercol in range(len(monster[0])):
                        # if any location that is a # in the monster, 
                        # is not a # in the image, it cannot be a monster.
                        if monster[monsterrow][monstercol] == '#' and \
                          self.tile[rowloc+monsterrow][colloc+monstercol] != '#':
                            is_monster = is_monster and False
                if is_monster:
                    monstercount+=1
        return monstercount


    def __repr__(self):
        ''' Helper method for debugging. '''
        output='<Tile Object:\n'
        for row in self.tile:
            output+=row+'\n'
        return output+str(self.tilenum)+'>\n'

class ImageTiler:
    '''A board to arrange image tiles'''
    def __init__(self,inputdata):
        '''read in all tiles and create a dict of tiles'''
        self.ordering={} # key=2d-tuple, vale = tile num.
        self.common_borders=[]
        self.tiles={}
        thistile=[]
        for line in inputdata:
            if line.startswith('Tile'):
                tilenum=int(line.replace('Tile ','').replace(':',''))
            elif '#' in line or '.' in line:
                thistile.append(line)
            elif line == '':
                self.tiles[tilenum]=Tile(tilenum,thistile)
                thistile=[]
            else:
                print('Unknown input detected')


    def pair_tiles(self):
        '''Determine which tiles share a common border'''
        for tile1 in self.tiles.values():
            for tile2 in self.tiles.values():
                is_border, border = tile1.pair(tile2)
                if is_border and border not in self.common_borders \
                  and border[::-1] not in self.common_borders:
                    self.common_borders.append(border)

    def product_of_corners(self):
        '''Determine which pieces are the corners of the puzzle and return their product'''
        output=1
        for tile in self.tiles.values():
            if len(tile.pairs) == 2:
                output*= tile.tilenum
        return output

    def build_image(self):
        ''' let n = sqrt (len self.tiles)
        start with a corner piece, then build the puzzle row by row until len(row) == np.sqrt(n)
        once we have sqrt(n) x (1xsqrt n) tiles build rows in a larger tile.'''
        # This method is a HOT MESS! but it works.
        # Sort the pieces into 3 piles, corners, edges and middle pieces.
        twopiecequeue = deque([tile for tile in self.tiles.values() if len(tile.pairs) ==2])
        threepiecequeue = deque([tile for tile in self.tiles.values() if len(tile.pairs) ==3])
        fourpiecequeue = deque([tile for tile in self.tiles.values() if len(tile.pairs) ==4])
        # Take a piece with two corners, manipulate it until its bottom and right sides are matches.
        # This will be the top left corner piece of the puzzle.
        # Loop over each location in the puzzle.
        puz_side_len=int(math.sqrt(len(self.tiles)))
        for row in range(1,puz_side_len+1):
            for col in range(1,puz_side_len+1):
                # loop over the puzzle from left to right and top to bottom
                # Choose the next piecepile
                if row in [1,puz_side_len] and col in [1,puz_side_len]:
                    # Corners
                    nextpiecequeue = twopiecequeue
                elif row in [1,puz_side_len] or col in [1,puz_side_len]:
                    # edges
                    nextpiecequeue = threepiecequeue
                else:
                    # Middle bits
                    nextpiecequeue = fourpiecequeue
                # If this is the top left corner, rotate and flip the piece until the
                #  bottom and right have matching borders
                if row ==1 and col ==1:
                    thispiece=nextpiecequeue.pop()
                    done=False
                    while not done:
                        if thispiece.right() not in self.common_borders and \
                            thispiece.bottom() not in self.common_borders:
                            thispiece.tile=thispiece.rotate()
                        else:
                            done=True
                        if thispiece.right() not in self.common_borders and \
                            thispiece.bottom() not in self.common_borders:
                            thispiece.tile=thispiece.flip()
                        else:
                            done = True
                    # The tile is now correctly oriented for the top left corner.
                    self.ordering[(1,1)]=thispiece
                else:
                    if col ==1:
                        done=False
                        while not done:
                            thispiece=nextpiecequeue.pop()
                            # Match the first col to the row above
                            for orientation in thispiece.orientations():
                                if orientation.top() == self.ordering[(row-1,col)].bottom():
                                    self.ordering[(row,col)]=orientation
                                    done=True
                            if not done:
                                # If this piece doesn't fit, put it back in the pile.
                                nextpiecequeue.appendleft(thispiece)
                    else:
                        # Match to the piece to the left
                        done=False
                        while not done:
                            thispiece=nextpiecequeue.pop()
                            # Match the first col to the row above
                            for orientation in thispiece.orientations():
                                if orientation.left() == self.ordering[(row,col-1)].right():
                                    self.ordering[(row,col)]=orientation
                                    done=True
                                    break
                            if not done:
                                nextpiecequeue.appendleft(thispiece)

    def make_big_tile(self):
        '''Take all the pieces in order and build a large tile'''
        bigtile=[]
        for imgrow in range(1,13):
            for i in range(0,8):
                thisrow=''
                for imgcol in range(1,13):
                    # Note we trim the matching sides
                    thisrow+=self.ordering[imgrow,imgcol].trim_sides()[i]
                bigtile.append(thisrow)

        return Tile(1337,bigtile)

def day20_01():
    """Run part 1 of Day 20's code"""
    path = "./input/20/input.txt"
    mytiler = ImageTiler(file_to_str_array(path))
    mytiler.pair_tiles()
    result = mytiler.product_of_corners()
    print(f'2001: Product of corner piece numbers: {result}')

def day20_02():
    """Run part 2 of Day 20's code"""
    path = "./input/20/input.txt"
    #path ='tests/day20_testinput.txt'
    mytiler = ImageTiler(file_to_str_array(path))
    mytiler.pair_tiles()
    mytiler.build_image()
    bigtile=mytiler.make_big_tile()
    nummonsters=0
    for orientation in bigtile.orientations():
        nummonsters+=orientation.find_monsters()
    result=sum([bool(char=='#') for row in bigtile.tile for char in row ]) - nummonsters*15
    print(f'2002: Number of Monsters: {nummonsters}. Number of rough sea tiles:{result}')

if __name__ == "__main__":
    day20_01()
    day20_02()

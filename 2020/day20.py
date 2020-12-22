"""
AOC day 20 2018
"""
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

        self.tile=[]
        [self.tile.append(i) for i in tile]
        # top, bottom, left, right
        self.borders=[self.tile[0], \
            self.tile[-1], \
            ''.join([row[0] for row in self.tile]),\
            ''.join([row[-1] for row in self.tile])]

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
                    if self.tilenum == other.tilenum:
                        continue
                    else:
                        self.pairs|={other.tilenum}

    def trim_sides(self):
        return [ row[1:-1] for row in self.tile]

    def rotate(self):
        self.tile = [''.join(s) for s in zip(*self.tile[::-1])]

    def __repr__(self):
        output='<Tile Object:\n'
        for row in self.tile:
            output+=row+'\n'
        return output+'>\n'

class ImageTiler:
    def __init__(self,inputdata):
        '''read in all tiles and create a dict of tiles'''
        self.ordering={} # key=2d-tuple, vale = tile num.
        
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
        for tile1 in self.tiles.values():
            for tile2 in self.tiles.values():
                tile1.pair(tile2)

    def product_of_corners(self):
        output=1
        for tile in self.tiles.values():
            if len(tile.pairs) == 2:
                output*= tile.tilenum
        return output

    def build_image(self):
        ''' let n = sqrt (len self.tiles)
        start with a corner piece, then build the puzzle row by row until len(row) == np.sqrt(n)
        once we have sqrt(n) x (1xsqrt n) tiles build rows in a larger tile.'''
        twopiecequeue = deque([tile for tile in self.tiles if len(tile.pairs) ==2])
        threepiecequeue = deque([tile for tile in self.tiles if len(tile.pairs) ==2])
        fourpiecequeue = deque([tile for tile in self.tiles if len(tile.pairs) ==2])
        first_corner = twopiecequeue.pop()
        pass

def day20_01():
    """Run part 1 of Day 20's code"""
    path = "./input/20/input.txt"
    mytiler = ImageTiler(file_to_str_array(path))
    mytiler.pair_tiles()
    result = mytiler.product_of_corners()
    print(len(mytiler.tiles))
    print(f'2001: {result}')

def day20_02():
    """Run part 2 of Day 20's code"""
    path = "./input/20/input.txt"
    result=""
    print(f'2002: {result}')

if __name__ == "__main__":
    day20_01()
    #day20_02()

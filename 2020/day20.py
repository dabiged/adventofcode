"""
AOC day 20 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Tile:
    ''' A tile object 

    it consists of a 10x10 chars.

    storage is a dict with tuple keys, and char values.'''
    def __init__(self,tile: list):
        '''Initialise a tile'''
        self.tilegeom={}
        for rownum, row in enumerate(tile):
            for colnum, col in enumerate(row):
                self.tilegeom[complex(colnum-5,rownum-5)]=col


    def __repr__(self):
        output=''
        for im in range(-5,6):
            for re in range(-5,6):
                output+=self.tilegeom.get(complex(re,im),'')
            output+='\n'
        return output

    def flip(self,tile):
        ''' a generator that flips a tile  horizontally and vertically'''
        pass

    def rotate(self):
        ''' a generator that rotates a tile by 90 degs 3 times '''
        output={}
        for key,value in self.tilegeom.items():
            output[key*1j]=value
        self.tilegeom=output

    def permute(self,tile):
        ''' a generator that returns all possible tile rotations and flips'''
        pass


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
                self.tiles[tilenum]=Tile(thistile)
                thistile=[]
            elif line == '':
                pass
            else:
                print('Unknown input detected')


    def sort_tiles(self):
        raise NotImplementedError
        '''for tile1 in list of tiles:
            for tile2 in list of tiles:
                if tile1==tile2:
                    continue
                else:
                    for comb1 in tile1.permute():
                        for comb2 in tile2.permute():
                            if firstrow tile1 == last row tile2:
                                store tile geometry
        '''


def day20_01():
    """Run part 1 of Day 20's code"""
    path = "./input/20/input.txt"
    result=""
    print(f'2001: {result}')

def day20_02():
    """Run part 2 of Day 20's code"""
    path = "./input/20/input.txt"
    result=""
    print(f'2002: {result}')

if __name__ == "__main__":
    day20_01()
    #day20_02()

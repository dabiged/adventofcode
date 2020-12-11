"""
AOC day 06 2018
"""
from collections import defaultdict
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def man_dist(x1,y1, x2,y2):
    """Calculate the manhattan distance between two points"""
    return abs(x1-x2)+abs(y1-y2)

class Board:
    """
    A checker board like playing area of squares containing sources.
    Each source is allocated a letter pair and its location on the board is a capital.
    """
    def __init__(self,listofsource):
        """ build a list of lists to represent the playing area.
        halo specifies the number of blanks to the right and bottom
        outside of input area."""
        self.blankchar='..'
        # Build a dict that maps source num to a alpha-char
        self.alphabet = {num:char.upper() for num,char in enumerate([a+b for a in "abcdefghijklmnopqrstuvwxyz" for b in "abcdefghijklmnopqrstuvwxyz"])}
        # A dict to contain source positions.
        self.sources={}
        sourcenum=0
        for source in listofsource:
            self.sources[self.alphabet[sourcenum]]=tuple([int(i) for i in reversed(source.split(", "))])
            sourcenum+=1
        # The gridded board.
        self.board=[]
        #populate the board with empty values.
        self.board_size=max(self.source_row_max(),self.source_col_max())+1
        for row in range(0,self.board_size):
            thisrow = [self.blankchar for col in range(0,self.board_size)]
            self.board.append(thisrow)
        # Read source locations and place them on the board
        for key, location in self.sources.items():
            row, col = location
            self.board[row][col] = key.upper()

    def __repr__(self):
        """
        A helper method that allows us to run
        > print(mysquare)
        to return a human readable representation of the cuts.
        """
        gridplot=""
        for thisrow in self.board:
            gridplot+="".join(thisrow)+"\n"
        return gridplot

    def calc_influence(self):
        '''Calculate the area that each source influences.
        influence is determinied  by which source is closest.
        '''
        # for each location on the board
        for row in range(self.board_size):
            for col in range(self.board_size):
                # look at each source and work out which is closest.
                sourcedist={}
                for sourcename, sourceloc in self.sources.items():
                    sourcerow, sourcecol = sourceloc
                    sourcedist[sourcename]=man_dist(row,col,sourcerow,sourcecol)
                # make a list of all sources that are the shortest distance away.
                closestsources=[k for k, v in sourcedist.items() if v==min(sourcedist.values())]
                if (row,col) in self.sources.values():
                    # location is a source.
                    pass
                elif len(closestsources) > 1:
                    # location tied for multiple sources
                    self.board[row][col]=self.blankchar
                elif len(closestsources) == 1:
                    # Update board with closest source.
                    self.board[row][col] = closestsources[0].lower()
                else:
                    print("Something went wrong")

    def create_area(self,dist=10000):
        ''' Create and return the size of an area where all sources are
        within dist units, measured by manhattan distance'''
        size_area=0
        for row in range(self.board_size):
            for col in range(self.board_size):
                # look at each source and work out which is closest.
                sourcedist={}
                for sourcename, sourceloc in self.sources.items():
                    sourcerow, sourcecol = sourceloc
                    sourcedist[sourcename]=man_dist(row,col,sourcerow,sourcecol)
                # make a list of all sources that are the shortest distance away.
                totaldist=0
                for i in sourcedist.values():
                    totaldist+=i
                if totaldist<dist:
                    self.board[row][col]='#'
                    size_area+=1
        return size_area


    def count_highest_finite(self):
        """ Return the size of the source whose influenced area is the largest
        finite value and its name."""
        # Create a list of all lower case infinite source.
        # These will be excluded from all sources below.
        # inlcude the period as these will be dropped later.
        infinite_sources=set({self.blankchar})
        # Look for any source area on the edges of the board.
        for char in self.board[0][:]:
            # Top
            infinite_sources|=set({char.lower()})
        for char in self.board[self.board_size-1][:]:
            # bottom
            infinite_sources|=set({char.lower()})
        print(infinite_sources)
        for row in range(self.board_size):
            for col in [0, self.board_size-1]:
                infinite_sources|= set({self.board[row][col].lower()})
        print("Infinite sources:", infinite_sources)
        positions_influenced=defaultdict(int)
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col].lower() not in infinite_sources:
                    # Calc the number of positions influenced.
                    positions_influenced[self.board[row][col].lower()]+=1
        # get the name of the source with the largest finite area.
        largest_finite_source = max(positions_influenced, key=positions_influenced.get)
        # Return its size.
        return positions_influenced[largest_finite_source], largest_finite_source.upper()



    def source_col_max(self):
        return max([self.sources[source][0]  for source in self.sources])

    def source_row_max(self):
        return max([self.sources[source][1]  for source in self.sources])

    def source_col_min(self):
        return min([self.sources[source][0]  for source in self.sources])

    def source_row_min(self):
        return min([self.sources[source][1]  for source in self.sources])


def day06_01():
    """Run part 1 of Day 06's code"""
    path = "./input/06/input.txt"
    part1board = Board(file_to_str_array(path))
    part1board.calc_influence()
    result, source =part1board.count_highest_finite()
    print(f'0601: The largest finite area is: {result}')

def day06_02():
    """Run part 2 of Day 06's code"""
    path = "./input/06/input.txt"
    part1board = Board(file_to_str_array(path))
    result=part1board.create_area()
    print(f'0602: Number of spaces within 10000 units of all sources: {result}')

if __name__ == "__main__":
    day06_01()
    day06_02()

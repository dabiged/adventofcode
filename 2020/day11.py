"""
AOC day 11 2018
"""
import time
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class BoardingLounge:
    """
    A boarding lounge containing seats.
    L == Vacant
    # == Occupied
    . == floor

    """

    def __init__(self,strarray):
        self.grid=[]
        self.numneighbours=[]
        for row in strarray:
            self.grid.append(list(row))
            # This initialisation of numneighbours is a shitty hack.
            #  it should be initialised as all zeroes.
            self.numneighbours.append(list(row))
        self.numrows=len(self.grid)
        self.numcols=len(self.grid[0])

    def __repr__(self):
        """
        A helper method that allows us to run

        to return a human readable representation of the run
        """
        gridplot="\n"
        for thisrow in self.grid:
            gridplot+="".join(thisrow)+"\n"
        return gridplot

    def occupied(self,row,col):
        """ Return a bool if seat is occupied or not"""
        if self.grid[row][col] == '#':
            return True
        return False

    def get_neighbours(self,row,col):
        """ get the number of occupied neightbours surrounding this seat
        neighbours is defined as the surrounding seats only,
        i.e. for the seat at '@' there are 8 possible neighbours
        123
        4@5
        678

        returns an int between 0 and 8
        """
        if self.grid[row][col] == ".":
            return 0
        numneighbours=0
        for deltarow in [-1, 0, 1]:
            for deltacol in [-1, 0, 1]:
                if row+deltarow <0 or row+deltarow>self.numrows-1:
                    # out of bounds
                    pass
                elif col+deltacol <0 or col+deltacol >self.numcols-1:
                    # out of bounds
                    pass
                elif deltarow == 0 and deltacol == 0:
                    # don't count this seat
                    pass
                elif self.occupied(row+deltarow, col+deltacol):
                    numneighbours+=1
        return numneighbours

    def get_neighbours_part2(self,row,col):
        """ get the number of occupied seats along diagonals and lines.
        i.e.
        .#.#.
        ..L..
        .#.#.
        Sees no seats.
        returns an int between 0 and 8
        """

        if self.grid[row][col] == ".":
            # Floor space
            return 0
        numneighbours=0
        for deltarow, deltacol in [(x,y) for x in [-1,0,1] for y in [-1,0,1] if not y == x == 0]:
            done=False
            thisrow, thiscol = row, col
            while not done:
                thisrow+=deltarow
                thiscol+=deltacol
                if thisrow>self.numrows-1 or thisrow<0:
                    # Out of bounds
                    done=True
                elif thiscol>self.numcols-1 or thiscol<0:
                    # Out of bounds
                    done=True
                elif self.grid[thisrow][thiscol] == '#':
                    # Saw neighbour
                    numneighbours+=1
                    done=True
                elif self.grid[thisrow][thiscol] == 'L':
                    #saw empty seat
                    done=True
                elif self.grid[thisrow][thiscol] == '.':
                    pass
                else:
                    print(thisrow, thiscol, self.grid[thisrow][thiscol])
                   # raise ValueError("Something went wrong")

        return numneighbours

    def calc_neighbours(self,part=1):
        """ Update the class variable numneighbours with the number of
        neighbours seen by each location"""
        for row in range(0,self.numrows):
            for col in range(0,self.numcols):
                if part == 1:
                    self.numneighbours[row][col]=self.get_neighbours(row,col)
                elif part ==2 :
                    self.numneighbours[row][col]=self.get_neighbours_part2(row,col)


    def update(self,part=1):
        """Perform one update to the seating arrangement of the boarding lounge
        Updates class variable "grid" """

        if part==1:
            self.calc_neighbours()
            thres=4
        elif part==2:
            self.calc_neighbours(part=2)
            thres=5
        for row in range(0,self.numrows):
            for col in range(0,self.numcols):
                if self.grid[row][col] == "L" \
                and self.numneighbours[row][col] == 0:
                    self.grid[row][col] = '#'
                elif self.grid[row][col] == "#" \
                and self.numneighbours[row][col] >= thres:
                    self.grid[row][col]='L'

    def run(self,part=1, show=False):
        """Step the boarding pass until it ceases changing
        Updates class variables grid and numneighbours"""
        old_state=''
        count=0
        while str(self) != old_state:
            old_state=self.__repr__()
            self.update(part=part)
            count+=1
            if show and count%2 == 1:
                time.sleep(0.2)
                print(self)
                if count in (1, 85):
                    time.sleep(3)
        return count

    def count_occupied(self):
        """ count the number of occupied seats in the boarding lounge"""
        numoccupied=0
        for row in range(0,self.numrows):
            for col in range(0,self.numcols):
                if self.grid[row][col]=='#':
                    numoccupied+=1
        return numoccupied

def day11_01():
    """Run part 1 of Day 11's code"""
    path = "./input/11/input.txt"
    part11lounge=BoardingLounge(file_to_str_array(path))
    part11lounge.run(show=True)

    result=part11lounge.count_occupied()
    print(f'1101: Number of occupied seats: {result}')

def day11_02():
    """Run part 2 of Day 11's code"""
    path = "./input/11/input.txt"
    part11lounge=BoardingLounge(file_to_str_array(path))
    part11lounge.run(part=2,show=True)
    result=part11lounge.count_occupied()
    print(f'1102: Number of occupied seats {result}')

if __name__ == "__main__":
    #day11_01()
    day11_02()

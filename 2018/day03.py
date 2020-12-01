"""
AOC day 03 2018
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def read_cut(line):
    """
    Given a cut of form :
    #CutNum(int) @ Xloc(int),Yloc(int): Xsize(int)x(Ysize)
    return CutNum, Xloc, YLoc, XSize, YSize
    """
    # CutNum(int) @ Xloc(int),Yloc(int): Xsize(int)x(Ysize)
    CutName,     _, location,                 size = tuple(line.split())
    location=location.rstrip(":")
    CutNum=CutName.lstrip("#")
    (CutXloc,CutYloc) = tuple(location.split(","))
    (CutXsize, CutYsize ) = tuple(size.split("x"))
    return int(CutNum), int(CutXloc), int(CutYloc), int(CutXsize), int(CutYsize)

class fabric_square:
    """
    A 2d fabric square upon which cuts may be made.
    """

    def __init__(self, rows=1000, cols=1000) :
        """
        Initialises the size of the square.
        """
        self.summary={}
        self.grid=[]
        for row in range(0,rows):
            thisrow=[]
            for col in range(0,cols):
                thisrow.append(".")
            self.grid.append(thisrow)

    def __repr__(self):
        """
        A helper method that allows us to run 
        > print(mysquare)
        to return a human readable representation of the cuts.
        """
        gridplot=""
        for thisrow in self.grid:
            row=""
            for item in thisrow:
                row+=item
            gridplot+=(row+"\n")
        return gridplot


    def addcut(self, cut):
        """
        Given a claim to cut the fabric of form :
        #CutNum(int) @ Xloc(int),Yloc(int): Xsize(int)x(Ysize)
        Allocate part of the fabric square to that cut by replacing the period
        with the cutNum.
        If the location is already claimed place an X there.
        """
        CutNum, CutColStartloc, CutRowStartloc, CutColsize, CutRowsize = read_cut(cut)
        for column in range(CutColStartloc, CutColStartloc+CutColsize):
            for row in range(CutRowStartloc,CutRowStartloc+CutRowsize):
                if self.grid[row][column] == ".":
                    self.grid[row][column]=str(CutNum)
                else:
                    self.grid[row][column] = "X"

    def overlaps(self):
        """
        How many locations on the fabric sqaure overlap another claim.
        """
        count=0
        # Loop over each location in the fabric.
        for row in range(0,self.numrows()):
            for col in range(0,self.numcols()):
                if self.grid[row][col] == "X":
                    count+=1
        return count
    
    def summarise(self):
        """
        Count the number of inches of each claim.
        """
        for row in range(0,self.numrows()):
            for col in range(0,self.numcols()):
                if self.grid[row][col] not in self.summary.keys():
                    self.summary[self.grid[row][col]] = 1
                else:
                    self.summary[self.grid[row][col]] += 1

    def nooverlap(self,cut):
        """
        Does the current cut have no overlaps with others?
        """
        CutNum, _, _, CutColsize, CutRowsize = read_cut(cut)
        if str(CutNum) not in self.summary.keys():
            return False
        if self.summary[str(CutNum)] == CutColsize*CutRowsize:
           return True
        return False


    def numcols(self):
        """The Number of columns in the grid"""
        return len(self.grid[0])

    def numrows(self):
        """The Number of rows in the grid"""
        return len(self.grid)

    def shape(self):
        """A tuple of the grig size"""
        return self.numrows(), self.numcols()

    def getsummary(self):
        return self.summary

def day03_01():
    """Run part 1 of Day 3's code"""

    path = "./input/03/input.txt"
    mysquare=fabric_square()
    for cut in file_to_str_array(path):
        mysquare.addcut(cut)
    result = mysquare.overlaps()
    print(f'0301: Number of overlaps: {result}')

def day03_02():
    """Run part 2 of Day 3's code"""
    path = "./input/03/input.txt"
    mysquare=fabric_square()
    for cut in file_to_str_array(path):
        mysquare.addcut(cut)
    mysquare.summarise()
    for cut in file_to_str_array(path):
        if mysquare.nooverlap(cut):
            result= cut.split()[0]
    print(f'0302: Cut with no overlaps: {result}')
    pass

if __name__ == "__main__":
    day03_01()
    day03_02()

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
    cutname,     _, location,                 size = tuple(line.split())
    location=location.rstrip(":")
    cutnum=cutname.lstrip("#")
    (cutxloc,cutyloc) = tuple(location.split(","))
    (cutxsize, cutysize ) = tuple(size.split("x"))
    return int(cutnum), int(cutxloc), int(cutyloc), int(cutxsize), int(cutysize)

class FabricSquare:
    """
    A 2d fabric square upon which cuts may be made.
    """

    def __init__(self, rows=1000, cols=1000) :
        """
        Initialises the size of the square.
        """
        self.summary={}
        self.grid=[]
        for _ in range(0,rows):
            thisrow=[]
            for _ in range(0,cols):
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
            gridplot+="".join(thisrow)+"\n"
        return gridplot


    def addcut(self, cut):
        """
        Given a claim to cut the fabric of form :
        #CutNum(int) @ Xloc(int),Yloc(int): Xsize(int)x(Ysize)
        Allocate part of the fabric square to that cut by replacing the period
        with the cutNum.
        If the location is already claimed place an X there.
        """
        cutnum, cutcolstartloc, cutrowstartloc, cutcolsize, cutrowsize = read_cut(cut)
        for column in range(cutcolstartloc, cutcolstartloc+cutcolsize):
            for row in range(cutrowstartloc,cutrowstartloc+cutrowsize):
                if self.grid[row][column] == ".":
                    self.grid[row][column]=str(cutnum)
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
        cutnum, _, _, cutcolsize, cutrowsize = read_cut(cut)
        if str(cutnum) not in self.summary.keys():
            return False
        if self.summary[str(cutnum)] == cutcolsize*cutrowsize:
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
        """Show summary of claim name and sqin size"""
        return self.summary

def day03_01():
    """Run part 1 of Day 3's code"""

    path = "./input/03/input.txt"
    mysquare=FabricSquare()
    for cut in file_to_str_array(path):
        mysquare.addcut(cut)
    result = mysquare.overlaps()
    print(f'0301: Number of overlaps: {result}')

def day03_02():
    """Run part 2 of Day 3's code"""
    path = "./input/03/input.txt"
    mysquare=FabricSquare()
    for cut in file_to_str_array(path):
        mysquare.addcut(cut)
    mysquare.summarise()
    for cut in file_to_str_array(path):
        if mysquare.nooverlap(cut):
            result= cut.split()[0]
    print(f'0302: Cut with no overlaps: {result}')

if __name__ == "__main__":
    day03_01()
    day03_02()

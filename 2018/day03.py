"""
AOC day 03 2018
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def build_empty_grid(xsize=1000, ysize=1000)->list:
    """
    Returns a List of size xsize x ysize with all entries containing a 
    period character.
    """
    grid=[]
    for y in range(0,ysize):
        thisrow=[]
        for x in range(0,xsize):
            thisrow.append(".")
        grid.append(thisrow)
    return grid

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

def print_fabric(grid):
    for thisrow in grid:
        row=""
        for item in thisrow:
            row+=item
        print(row)

def build_grid(listofcuts, xsize=1000, ysize=1000)->list:
    """
    Given a list of cuts of form :
    #CutNum(int) @ Xloc(int),Yloc(int): Xsize(int)x(Ysize)

    returns list with spaces taken by the CutNum
    """
    grid=build_empty_grid(xsize,ysize)
    for line in listofcuts:
        CutNum, CutXloc, CutYloc, CutXsize, CutYsize = read_cut(line)
        print(CutNum, CutXloc, CutYloc, CutXsize, CutYsize)
        for y in range(CutXloc, CutXloc+CutXsize):
            for x in range(CutYloc,CutYloc+CutYsize):
                if grid[x][y] == ".":
                    grid[x][y]=str(CutNum)
                else:
                    grid[x][y] = "X"
    return grid

def day02_01():
    """Run part 1 of Day 2's code"""
    path = "./input/02/input.txt"
    pass

def day02_02():
    """Run part 2 of Day 1's code"""
    path = "./input/02/input.txt"
    pass

if __name__ == "__main__":
    day02_01()
    day02_02()

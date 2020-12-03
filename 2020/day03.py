"""
AOC day 03 2020
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class ToboganRun:
    """
    A 2d tobogan run grid
    """

    def __init__(self, listofrun, repeats=500):
        """
        Initialises the size of the square.
        """
        self.grid=[]
        for row in listofrun:
            thisrow=""
            for repeat in range(repeats):
                thisrow+=row
            self.grid.append(list(thisrow))

    def __repr__(self):
        """
        A helper method that allows us to run
        > print(mytobogan
        to return a human readable representation of the run
        """
        gridplot=""
        for thisrow in self.grid:
            gridplot+="".join(thisrow)+"\n"
        return gridplot

    def tree_count(self, right=3, down=1, startrow=0, startcol=0):
        """ 
        return the number of trees encounted starting at the startrow,startcol
        and moving down and right in steps specified until you hit the bottom.
        """
        treecount=0
        row=startrow
        col=startcol
        while row <= self.numrows()-1:
            if self.grid[row][col] == "#":
                treecount +=1
            row+=down
            col+=right
        return treecount

    def numcols(self):
        """The Number of columns in the grid"""
        return len(self.grid[0])

    def numrows(self):
        """The Number of rows in the grid"""
        return len(self.grid)

    def shape(self):
        """A tuple of the grig size"""
        return self.numrows(), self.numcols()


def day03_01():
    """Run part 1 of Day 3's code"""

    path = "./input/03/input.txt"
    myrun=ToboganRun(file_to_str_array(path))
    print(f'0301: Number of Trees Intercepted: {myrun.tree_count()}')

def day03_02():
    """Run part 2 of Day 3's code"""
    path = "./input/03/input.txt"
    myrun=ToboganRun(file_to_str_array(path))
    result= \
     myrun.tree_count()* \
     myrun.tree_count(right=1,down=1)* \
     myrun.tree_count(right=5,down=1)* \
     myrun.tree_count(right=7,down=1)* \
     myrun.tree_count(right=1,down=2) 
    print(f'0302: Number of Trees Intercepted on 5 runs:{result}')

if __name__ == "__main__":
    day03_01()
    day03_02()

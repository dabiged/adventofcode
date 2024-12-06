from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

testdata=['....#.....',
'.........#',
'..........',
'..#.......',
'.......#..',
'..........',
'.#..^.....',
'........#.',
'#.........',
'......#...']


class Grid:
    def __init__(self,inputdata):
        # Store the input data for later (part 2)
        self.inputdata=inputdata
        self.grid=defaultdict(str)
        self.visited=set()
        self.dir=-1j # up
        for rownum,row in enumerate(inputdata):
            for colnum, char in enumerate(row):
                if char == '^':
                    self.position=colnum+rownum*1j
                    self.visited.add((colnum+rownum*1j,self.dir))
                    self.grid[colnum+rownum*1j]='.'
                else:
                    self.grid[colnum+rownum*1j]=char

        self.numrows=max([int(i.imag) for i in self.grid.keys()])
        self.numcols=max([int(i.real) for i in self.grid.keys()])
        self.possibleblock=set() #part 2
        
    def __str__(self):
        # helper method to print the grid
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                if re+im*1j in [a[0] for a in self.visited]:
                    output+='X'
                else:
                    output+=self.grid[re+im*1j]
            output+='\n'
        return output

    def walk(self):
        # Walk to a new location or direction
        newloc=self.position+self.dir
        if self.grid[newloc] == '':
            # you are outside grid
            return False
        elif self.grid[newloc] == '#':
            # there is obstacle so turn right
            self.dir=self.dir*1j
            return True
        elif self.grid[newloc] == '.':
            # move to vacant position
            self.position=newloc
            self.visited.add((newloc,self.dir))
            return True
        else:
            # Shit when wrong yo!
            raise ValueError

    def walknew(self):
        newloc=self.position+self.dir
        if self.grid[newloc] == '':
            # outside grid
            return False
        elif self.grid[newloc] == '#':
            # obstacle so turn
            self.dir=self.dir*1j
            return True
        elif self.grid[newloc] == '.':
            # move
            self.position=newloc
            if (newloc,self.dir) not in self.visited:
                self.visited.add((newloc,self.dir))
            else:
                raise RecursionError
            return True
        else:
            raise ValueError


    def walk_grid(self,verbose=False) :
        while self.walknew():
            print(self)
        return len(self.visited)
        
    def find_loops(self):
        loop=0
        for row in range(self.numrows+1):
            for col in range(self.numcols+1):
                # for each possible location Add an obstacle and rerun simuation
                print(row,col)
                newgrid=Grid(self.inputdata)
                newgrid.grid[col+row*1j]='#'
                try:
                    newgrid.walk_grid(verbose=verbose)
                except RecursionError:
                    loop+=1
                except Exception as e:
                    print(e)
        return loop

def part1(inputdata=testdata):
    mygrid=Grid(inputdata)
    return mygrid.walk_grid()

def part2(inputdata=testdata):
    mygrid=Grid(inputdata)
    return mygrid.find_loops()


def day06_01():
    """Run part 1 of Day 4's code"""
    path = "./input/06.txt"
    print("0601:", part1(file_to_str_array(path)))


def day06_02():
    """Run part 2 of Day 4's code"""
    path = "./input/06.txt"
    print("0602:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day06_01()
    day06_02()

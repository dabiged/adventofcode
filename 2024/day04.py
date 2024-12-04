from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

testdata=['MMMSXXMASM',
'MSAMXMSMSA',
'AMXSXMAAMM',
'MSAMASMSMX',
'XMASAMXAMM',
'XXAMMXXAMA',
'SMSMSASXSS',
'SAXAMASAAA',
'MAMMMXMMMM',
'MXMXAXMASX']


class Grid:
    def __init__(self,grid):
        self.grid=defaultdict(str)
        for rownum,row in enumerate(grid):
            for colnum, char in enumerate(row):
                self.grid[colnum+rownum*1j]=char
        self.numrows=max([int(i.imag) for i in self.grid.keys()])
        self.numcols=max([int(i.real) for i in self.grid.keys()])
        self.dirs=[(up,down) for up in [-1,0,1] for down in [-1,0,1] ]
        self.dirs.remove((0,0))
        
    def __str__(self):
        output=''
        for im in range(self.numrows):
            for re in range(self.numcols):
                output+=self.grid[re+im*1j]
            output+='\n'
        return output

    def look1(self,point,direction):
        a,b=direction
        return "".join([self.grid[point+i*a+b*i*1j] for i in range(4)])

    def lookall1(self,point):
        words= [self.look1(point,(up,down)) for up,down in self.dirs ]
        output=[]
        for word in words:
            if len(word) == 4:
                output.append(word)
        return output

    def count_xmas(self):
        count=0
        for re in range(self.numcols+1):
            for im in range(self.numrows+1):
                point=(re+im*1j)
                for string in self.lookall1(point):
                    if string == 'XMAS' or string =='SAMX':
                        count+=1
        return count//2

    def look2(self,point):
        str1=self.grid[point-1-1j]+self.grid[point]+self.grid[point+1+1j]
        str2=self.grid[point-1+1j]+self.grid[point]+self.grid[point+1-1j]
        output=[]
        if len(str1) == 3:
            output.append(str1)
        else:
            output.append('')
        if len(str2) == 3:
            output.append(str2)
        else:
            output.append('')
        return output

    def count_tmas(self):
        count=0
        for re in range(self.numcols+1):
            for im in range(self.numrows+1):
                point=(re+im*1j)
                check=self.look2(point)
                if check[0] in ['SAM','MAS'] and check[1] in ['SAM','MAS']:
                    count+=1
        return count







def part1(inputdata=testdata):
    mygrid=Grid(inputdata)
    return mygrid.count_xmas()

def part2(inputdata=testdata):
    mygrid=Grid(inputdata)
    return mygrid.count_tmas()


def day04_01():
    """Run part 1 of Day 4's code"""
    path = "./input/04.txt"
    print("0401:", part1(file_to_str_array(path)))


def day04_02():
    """Run part 2 of Day 4's code"""
    path = "./input/04.txt"
    print("0402:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day04_01()
    day04_02()

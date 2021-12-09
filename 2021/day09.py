"""
AOC day 09 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Map():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.locations={}
        self.process_inputfile()
        self.count_low_points()

    def process_inputfile(self):
        data=file_to_str_array(self.inputfile)
        row,col = 0,0
        for line in data:
            for elem in line:
                self.locations[(row,col)]=int(elem)
                col+=1
            self.numcol=col
            col=0
            row+=1
        self.numrow=row


    def adjacent_points(self,point):
        row,col=point

        operations=[(-1,0),(1,0),(0,-1),(0,1)]

        if row == 0:
            operations.remove((-1,0))
        if row == self.numrow - 1:
            operations.remove((1,0))
        if col == 0:
            operations.remove((0,-1))
        if col == self.numcol - 1:
            operations.remove((0,1))

        adjacentpoints=[]
        for op in operations:
            adjacentpoints.append((row+op[0],col+op[1]))
        return adjacentpoints

    def is_low_point(self,point):
        row,col=point
        thisval=self.locations[(row,col)]
        adjacent_points=self.adjacent_points(point)

        lowest_near=10
        for point in adjacent_points:
            lowest_near=min(lowest_near,self.locations[point])
        if thisval < lowest_near:
            return True
        return False

    def count_low_points(self):
        self.lowpoints=[]
        for row in range(self.numrow):
            for col in range(self.numcol):
                if self.is_low_point((row,col)):
                    self.lowpoints.append( (row,col) )
        return self.lowpoints

    def explore_basin(self,point):
        if self.locations[point] == 9 or self.locations[point] == '#':
            return None
        else:
            self.locations[point]='#'
            for adjacent_point in self.adjacent_points(point):
                self.explore_basin(adjacent_point)

    def get_basin_size(self):
        count=0
        for val in self.locations.values():
            if val =='#':
                count+=1
        return count

    def explore_all_basins(self):
        self.basins_sizes=[]
        for lowpoint in self.lowpoints:
            self.explore_basin(lowpoint)
            basin_size=self.get_basin_size()
            self.process_inputfile()
            self.basins_sizes.append(basin_size)

    def part2(self):
        prod=1
        for i in sorted(self.basins_sizes)[-3:]:
            prod*=i
        return prod

    def get_risk(self):
        risk=0
        for location in self.count_low_points():
            risk+=1+self.locations[location]
        return risk

    def __repr__(self):
        outputstr=''
        for row in range(self.numrow):
            for col in range(self.numcol):
                outputstr+=str(self.locations[(row,col)])
            outputstr+='\n'
        return outputstr

def day09_01():
    """Run part 1 of Day 09's code"""
    inputfile = "./input/day09.txt"
    testmap=Map(inputfile)
    testmap.process_inputfile()
    result=testmap.get_risk()
    print(f'0901: {result} is the total risk')

def day09_02():
    """Run part 2 of Day 09's code"""
    inputfile = "./input/day09.txt"
    testmap=Map(inputfile)
    testmap.process_inputfile()
    result=testmap.explore_all_basins()
    result=testmap.part2()
    print(f'0902: {result} is the product of the size of the 3 largest basins')

if __name__ == "__main__":
    day09_01()
    day09_02()

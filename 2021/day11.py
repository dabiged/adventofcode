"""
AOC day 11 2018
"""
from lib.filehelper import file_to_str_array
from collections import deque
# pylint: disable=missing-module-docstring


class node():
    def __init__(self,row,col,score):
        ''' A bioluminent octopus'''
        self.score=score
        self.row=row
        self.col=col
        self.flashed=False

    def neighbours(self):
        ''' Return the locations of this Octopii's neighbours'''
        neighbours=[(self.row+i,self.col+j) for i in range(-1,2) for j in range(-1,2)]
        neighbours.remove((self.row,self.col))
        if self.row == 0:
            for outsidelocation in [(self.row-1,self.col+j) for j in range(-1,2)]:
                if outsidelocation in neighbours:
                    neighbours.remove(outsidelocation)
        if self.row == 9:
            for outsidelocation in [(self.row+1,self.col+j) for j in range(-1,2)]:
                if outsidelocation in neighbours:
                    neighbours.remove(outsidelocation)
        if self.col == 0:
            for outsidelocation in [(self.row+j,self.col-1) for j in range(-1,2)]:
                if outsidelocation in neighbours:
                    neighbours.remove(outsidelocation)
        if self.col == 9:
            for outsidelocation in [(self.row+j,self.col+1) for j in range(-1,2)]:
                if outsidelocation in neighbours:
                    neighbours.remove(outsidelocation)
        return neighbours


    def increment(self):
        ''' increment its energy by 1'''
        self.score+=1
        return self.score

    def flash(self):
        ''' Flash '''
        if self.flashed == False:
            self.flashed=True
            return 1
        else:
            return 0

    def __repr__(self):
        return str(self.score)

class Grid():
    def __init__(self,inputfile):
        self.numrows=10
        self.numcols=10
        self.inputfile=inputfile
        self.processinputfile()
        self.grid={}
        self.import_grid()
        self.totalflashes=0
        

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)

    def import_grid(self):
        for row,thisrow in enumerate(self.input):
            for col,val in enumerate(thisrow):
                self.grid[row,col]=node(row,col,int(val))
    def step(self):
        flash_queue=deque([])
        for location in self.grid.keys():
            flash_queue.append(location)
        while len(flash_queue) >0:
            location = flash_queue.pop()
            self.grid[(location)].score+=1
            if self.grid[location].score > 9 and self.grid[location].flashed == False:
                self.grid[location].flashed = True
                for neighbour in self.grid[location].neighbours():
                    flash_queue.append(neighbour)
            # flash
        for location,node in self.grid.items():
            if self.grid[location].flashed:
                self.grid[location].flashed=False
                self.totalflashes+=1
            if node.score > 9:
                node.score=0

    def part1(self):
        for step in range(100):
            self.step()
        return self.totalflashes

    def part2(self):
        done = False
        step =0
        while not done:
            prevnoflashes=self.totalflashes
            step+=1
            self.step()
            if prevnoflashes - self.totalflashes == -100:
                done=True
        return step


    def __repr__(self):
        output=''
        for row in range(self.numrows):
            thisrow=''
            for col in range(self.numcols):
                thisrow+=str(self.grid[row,col])
            output+=thisrow+'\n'
        return output



def day11_01():
    """Run part 1 of Day 11's code"""
    inputfile='input/day11.txt'
    testGrid=Grid(inputfile)
    result=testGrid.part1()
    print(f'1101: {result} is the number of flashes after 100 steps')

def day11_02():
    """Run part 2 of Day 11's code"""
    inputfile='input/day11.txt'
    testGrid=Grid(inputfile)
    result=testGrid.part2()
    print(f'1102: {result} is the first step where all octopii flash')

if __name__ == "__main__":
    day11_01()
    day11_02()

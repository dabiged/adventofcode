"""
AOC day 15 2018
"""
from lib.filehelper import file_to_str_array
from collections import deque, defaultdict
from queue import PriorityQueue
# pylint: disable=missing-module-docstring

class Node():
    def __init__(self,row,col,score,maxrows,maxcols):
        ''' '''
        self.score=score
        self.row=row
        self.col=col
        self.maxrows=maxrows
        self.maxcols=maxcols
        self.dist=0
        self.shortestpath=[]

    def neighbours(self):
        ''' Return the locations of this Octopii's neighbours'''
        r,c=self.row,self.col
        neighbours=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        if r == 0:
            neighbours.remove((r-1,c))
        if self.row == self.maxrows-1:
            neighbours.remove((r+1,c))
        if self.col == 0:
            neighbours.remove((r,c-1))
        if self.col == self.maxcols-1:
            neighbours.remove((r,c+1))
        return neighbours

    def __repr__(self):
        return str(self.score)


def increase(num,incrementer):
    output=num+incrementer
    if output > 9:
        output-=9
    return output

class Grid():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.numrows=-1
        self.numcols=-1
        self.grid={}


    def processinputfile2(self):
        self.input=file_to_str_array(self.inputfile)
        self.numrows=len(self.input)
        self.numcols=len(self.input[0])
        for tilex in range(0,5):
            for tiley in range(0,5):
                increaseby=tilex+tiley
                for row,line in enumerate(self.input):
                    for col,val in enumerate(line):
                        self.grid[tilex*self.numrows+row,tiley*self.numcols+col]=Node(tilex*self.numrows+row,tiley*self.numcols+col,increase(int(val),increaseby),self.numrows*5,self.numcols*5)
        self.numrows*=5
        self.numcols*=5

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)
        self.numrows=len(self.input)
        self.numcols=len(self.input[0])
        for row,line in enumerate(self.input):
            for col,val in enumerate(line):
                self.grid[row,col]=Node(row,col,int(val),self.numrows,self.numcols)

    def calc_paths(self,target,start=(0,0)):
        processed=set()
        proc_queue=PriorityQueue()
        proc_queue.put((self.grid[start].dist,start))
        self.grid[start].dist=0

        while not proc_queue.empty():
            dist,thisnode=proc_queue.get()
            if thisnode == target:
                print(f'{thisnode}:{self.grid[thisnode].dist}')
                break
            if thisnode not in processed:
                #print(f'{thisnode}:{self.grid[thisnode].dist}')
                processed.add(thisnode)
                for neighbour in self.grid[thisnode].neighbours():
                    if self.grid[neighbour].dist > dist+self.grid[neighbour].score:
                        self.grid[neighbour].dist=dist+self.grid[neighbour].score
                        proc_queue.put((self.grid[neighbour].dist,neighbour))
                    else:
                        self.grid[neighbour].dist=dist+self.grid[neighbour].score
                        self.grid[neighbour].shortestpath.append(self.grid[thisnode].shortestpath)
                        if neighbour not in processed:
                            proc_queue.put((self.grid[neighbour].dist,neighbour))
        return self.grid[target].dist


    def __repr__(self):
        output='   01234567890123456789012345678901234567890123456789\n\n'
        rowcounter=0
        for row in range(self.numrows):
            thisrow=str(rowcounter).zfill(2)+' '
            for col in range(self.numcols):
                thisrow+=str(self.grid[row,col])
            output+=thisrow+'\n'
            rowcounter+=1
        return output



def day15_01():
    """Run part 1 of Day 15's code"""
    path = "./input/day15.txt"
    testGrid=Grid(path)
    testGrid.processinputfile()
    result=testGrid.calc_paths((testGrid.numrows-1,testGrid.numcols-1))
    print(f'1501: {result}')

def day15_02():
    """Run part 2 of Day 15's code"""
    path = "./input/day15.txt"
    result=""
    print(f'1502: {result}')

if __name__ == "__main__":
    day15_01()
    #day15_02()

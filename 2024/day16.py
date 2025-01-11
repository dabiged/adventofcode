from lib.filehelper import file_to_str_array, get_file
import heapq
import math
import random
# pylint: disable=missing-module-docstring

from collections import defaultdict

testdata='''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''

testdata1='''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''

class Grid:
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.diag_neighbours=[up*1j+down for up in [-1,1] for down in [-1,1] ]
        self.direct_neighbours=[1,-1,1j,-1j]
        self.start=0
        self.end=0
        self.dir=1
        self.reset_grid()

    def reset_grid(self):
        self.grid=defaultdict(str)
        self.location=defaultdict(list)
        for rownum,row in enumerate(self.inputdata):
            for colnum, char in enumerate(row):
                if char == 'S':
                    self.start=colnum+rownum*1j
                    self.grid[colnum+rownum*1j]='.'
                elif char == 'E':
                    self.end=colnum+rownum*1j
                    self.grid[colnum+rownum*1j]='.'
                else:
                    self.grid[colnum+rownum*1j]=char
        self.numrows=max([int(i.imag) for i in self.grid.keys()])
        self.numcols=max([int(i.real) for i in self.grid.keys()])

    def on_grid(self,point):
        return 0<= point.imag <= self.numrows and 0<= point.real < self.numcols

    def look(self,point,direction):
        '''
        Return all locations along a line from the point in direction ordered nearest to furtherest

        point: complex: location on the grid
        direction: complex: direction to look
        '''
        a,b=direction
        this_point=point+direction
        output=[]
        while self.on_grid(thispoint):
            output.append(this_point)
            thispoint+=direction
        return output

    def get_neighbours(self,point,diags=False):
        ''' 
        Return the location of all neighbors of point (N,S,E,W).
        If diags = True, also return NE, SW, SE, NW

        point: complex: The point in question
        '''
        output=[]
        for delta in self.direct_neighbours:
            if self.on_grid(point+delta):
                output.append(point+delta)
        if diags:
            for delta in self.diag_neighbours:
                if self.on_grid(point+delta):
                    output.append(point+delta)
        return output

    def rotate(self,direction):
        '''
        Rotate the grid either Left or right
        '''
        if direction.lower() in [ 'l','ac','left', 'anticlockwise']:
            delta=-1j
            fixup=(self.numrows)*1j
        elif direction.lower() in ['r','c','right','clockwise']:
            delta=1j
            fixup=self.numcols
        newgrid={}
        for k,v in self.grid.items():
            newgrid[k*delta+fixup]=v
        self.grid=newgrid

    def flip(self,direction):
        '''
        Flip the grid either vertical or horizontal
        '''
        newgrid={}
        if direction.lower() in ['h','horz','horizontal']:
            for k,v in self.grid.items():
                newgrid[self.numcols-k.real+k.imag*1j]=v
        elif direction.lower() in ['v','vert','vertical']:
            for k,v in self.grid.items():
                newgrid[(self.numrows-k.imag)*1j+k.real]=v
        self.grid=newgrid

    def __len__(self):
        return self.numrows*self.numcols

    def __str__(self):
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                if re+im*1j == self.start:
                    output+='S'
                elif re+im*1j == self.end:
                    output+='E'
                else:
                    output+=self.grid[re+im*1j]
            output+='\n'
        return output
    
    def find_path(self,start,end,knowncost=None):
        ''' start is a tuple of location and direction
        end is a location on the grid.
        '''

        startloc,startdir=start
        #  cost, [path: (position,direction) ]
        a=[((0,0),[(startloc,startdir)])]
        heapq.heapify(a)
        count=0
        seen_locs=set()
        while True:
            try:
                elem=heapq.heappop(a)
            except:
                print([b[0] for b in a])
                raise
            cost,path=elem
            cost=math.floor(cost[0])
            curr_position=path[-1][0]
            curr_direction=path[-1][1]
            #if (curr_position,curr_direction) not in seen_locs:
            #    seen_locs.add((curr_position,curr_direction))
            if curr_position == self.end:
                if knowncost:
                    print(cost, path)
                    best_locs=set()
                    for loc,_ in path:
                        best_locs.add(loc)
                    while len(a) >0:
                        elem=heapq.heappop(a)
                        cost,path=elem
                        cost=cost[0]
                        print(cost, path)
                        if cost==knowncost:
                            for loc,_ in path:
                                best_locs.add(loc)
                        if cost>knowncost:
                            print(best_locs)
                            return len(best_locs),[]
                else:
                    return cost, path
            if self.grid[curr_position+curr_direction] == '.':
                count+=1
                heapq.heappush(a,((cost+1,count), path+[(curr_position+curr_direction,curr_direction)]))
            if self.grid[curr_position+(curr_direction*1j)] == '.':
                count+=1
                heapq.heappush(a,((cost+1001,count),path+[(curr_position+curr_direction*1j,curr_direction*1j)] ))
            if self.grid[curr_position+(curr_direction*-1j)] == '.':
                count+=1
                heapq.heappush(a,((cost+1001,count),path+[(curr_position+curr_direction*-1j,curr_direction*-1j)]))

def part1(inputdata=testdata1.split('\n')):
    grid=Grid(inputdata)
    cost, path =grid.find_path((grid.start,grid.dir),grid.end)
    return cost


def part2(inputdata=testdata1.split('\n')):
    grid=Grid(inputdata)
    cost, path =grid.find_path((grid.start,grid.dir),grid.end,knowncost=11048)
    return cost

def day16_01():
    """Run part 1 of Day 16's code"""
    path = "./input/16.txt"
    inputdata=get_file(path)
    print("1601:", part1(inputdata.split('\n')))


def day16_02():
    """Run part 2 of Day 16's code"""
    path = "./input/16.txt"
    inputdata=get_file(path)
    print("1602:", part2(inputdata.split('\n')))

if __name__ == "__main__":
    #day16_01()
    print(part1())
    print(part2())
    #day16_02()

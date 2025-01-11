from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from collections import defaultdict,deque

testdata='''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''

class Grid:
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.diag_neighbours=[up*1j+down for up in [-1,1] for down in [-1,1] ]
        self.direct_neighbours=[1,-1,1j,-1j]
        self.reset_grid()

    def reset_grid(self):
        self.grid=defaultdict(str)
        self.location=defaultdict(list)
        for rownum,row in enumerate(self.inputdata):
            for colnum, char in enumerate(row):
                self.grid[colnum+rownum*1j]=char
                if char == 'S':
                    self.start=colnum+rownum*1j
                    self.grid[colnum+rownum*1j]='.'
                if char == 'E':
                    self.end=colnum+rownum*1j
                    self.grid[colnum+rownum*1j]='.'
        self.numrows=max([int(i.imag) for i in self.grid.keys()])
        self.numcols=max([int(i.real) for i in self.grid.keys()])

    def on_grid(self,point):
        return 0<= point.imag <= self.numrows and 0<= point.real <= self.numcols

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


    def find_path(self,start,end):
        ''' Find shortest path between start and end using dijkstra's algorithm.
        Returns distance and path or None,[] if no path found.'''
        visited=dict()
        queue=deque()
        queue.append((start,1,[start]))
        visited[start]=0
        while queue:
            currloc, distance, path = queue.popleft()
            if currloc == end:
                return distance, path, visited
            for neighbour in self.get_neighbours(currloc):
                if self.grid[neighbour] != '#' and neighbour not in visited.keys():
                    queue.append((neighbour, distance+1, path+[neighbour]))
                    visited[neighbour] = distance
            #print(self.show(path=path))
        return None, [], dict()


    def __len__(self):
        return self.numrows*self.numcols

    def show(self,path=[]):
        ''' Similar to the __str__ method, but allows annotation with a list of locations.
        Very useful for path finding
        '''
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                if re+im*1j in path:
                    output+='O'
                elif re+im*1j == self.start:
                    output+='S'
                elif re+im*1j == self.end:
                    output+='E'
                elif self.grid[re+im*1j] != '#':
                    output+='.'
                else:
                    output+=self.grid[re+im*1j]
            output+='\n'
        return output

    def deltas(self,loc,dist):
        ''' return all possible cheats from loc'''
        deltas=[]
        for real_diff in range(-dist,dist+1):
            for imag_diff in range(-dist,dist+1):
                candidate = real_diff + imag_diff*1j + loc
                if abs(real_diff)+abs(imag_diff) <= dist and self.on_grid(candidate) and self.grid[candidate] != '#':
                    deltas.append(candidate)
        return deltas

    def __str__(self):
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                output+=self.grid[re+im*1j]
            output+='\n'
        return output

def part1(inputdata=testdata.split('\n'),size=100):
    grid=Grid(inputdata)
    dist,path,visited=grid.find_path(grid.start,grid.end)
    cheats=defaultdict(int)
    for location in visited.keys():
        deltas=[2, -2, 2*1j, -2*1j]
        for delta in deltas:
            if location + delta in visited.keys():
                diff = visited[location] - visited[location+delta] 
                if diff > size:
                    cheats[diff]+=1
    return sum([i for i in cheats.values()])


def part2(inputdata=testdata.split('\n'),size=100):
    grid=Grid(inputdata)
    dist,path,visited=grid.find_path(grid.start,grid.end)
    cheats=defaultdict(int)
    for endloc in range(len(path)):
        for startloc in range(endloc):
            secondloc= path[endloc]
            firstloc = path[startloc]
            distance=int(abs(firstloc.real - secondloc.real)+abs(firstloc.imag - secondloc.imag))
            if distance <=20 and endloc - startloc -distance >= size:
                cheats[distance]+=1
    return sum([i for i in cheats.values()])

def day20_01():
    """Run part 1 of Day 20's code"""
    path = "./input/20.txt"
    print("2001:", part1(file_to_str_array(path)))


def day20_02():
    """Run part 2 of Day 20's code"""
    path = "./input/20.txt"
    print("2002:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day20_01()
    day20_02()

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

from collections import defaultdict,deque

testdata='''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''

class Grid:
    def __init__(self,inputdata,steps=1024,testing=False):
        self.inputdata=inputdata
        self.testing=testing
        self.diag_neighbours=[up*1j+down for up in [-1,1] for down in [-1,1] ]
        self.direct_neighbours=[1,-1,1j,-1j]
        self.reset_grid(space=steps)

    def reset_grid(self,space=10000000):
        self.start=0
        self.end=70+70*1j
        self.numrows, self.numcols =70,70
        if self.testing:
            self.numrows,self.numcols = 6,6
            self.end=6+6*1j

        self.grid=defaultdict(str)
        self.lastbyte=self.inputdata[space]
        for coord in self.inputdata[:space]:
            re=int(coord.split(',')[0])
            im=int(coord.split(',')[1])
            self.grid[re+im*1j]='#'

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
        visited=set()
        queue=deque()
        queue.append((start,0,[start]))
        while queue:
            currloc, distance, path = queue.popleft()
            if currloc == end:
                return distance, path
            for neighbour in self.get_neighbours(currloc):
                if self.grid[neighbour] != '#' and neighbour not in visited:
                    queue.append((neighbour, distance+1, path+[neighbour]))
                    visited.add(neighbour)
        return None, []


    def __len__(self):
        return self.numrows*self.numcols

    def show(self,path=[]):
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                if re+im*1j in path:
                    output+='O'
                elif self.grid[re+im*1j] != '#':
                    output+='.'
                else:
                    output+=self.grid[re+im*1j]
            output+='\n'
        return output




def part1(inputdata=testdata.split('\n')):
    #grid=Grid(inputdata,steps=12,testing=True)
    grid=Grid(inputdata,steps=1024,testing=False)
    distance,path = grid.find_path(grid.start, grid.end)
    return distance



def part2(inputdata=testdata):
    steps=1024
    distance=280
    while distance:
        steps+=1
        grid=Grid(inputdata,steps=steps,testing=False)
        distance,path = grid.find_path(grid.start, grid.end)
    return inputdata[steps-1]


def day18_01():
    """Run part 1 of Day 18's code"""
    path = "./input/18.txt"
    print("1801:", part1(file_to_str_array(path)))


def day18_02():
    """Run part 2 of Day 18's code"""
    path = "./input/18.txt"
    print("1802:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day18_01()
    day18_02()

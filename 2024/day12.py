from lib.filehelper import file_to_str_array
from collections import defaultdict
from collections import deque
# pylint: disable=missing-module-docstring

testdata='''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''



class Region:
    '''
    A region is a shape of complex locations.
    '''
    def __init__(self,name):
        self.name=name
        self.locations=set()

    def add(self,loc):
        ''' Add a new location to the region'''
        self.locations.add(loc)

    def area(self):
        return len(self.locations)

    def side_length(self,vect):
        '''
        The number of cells with an empty cell next to it in one direction
        '''
        length=0
        for i in self.locations:
            if i+vect not in self.locations:
                length+=1
        return length

    def perimeter1(self):
        '''
        part 1 perimeter
        '''
        return sum([self.side_length(vect) for vect in [1, -1, 1j, -1j]])
    
    def is_in(self,location):
        if location in self.locations:
            return True
        return False

    def is_not_in(self,location):
        if location in self.locations:
            return False
        return True

    def concave_corners(self,loc):
        '''
        Rather than counting the number of sides, count the number of corners.

        There are two types of corners 
        Concave corners like this:
            ...     The check for this concave corner is:
         001111...  If the cell above and left are filled, but the above-left isn't filled:
         001111...       corners+=1
         111111...   Repeat for the other geometries.
         111111...
           ...

        '''

        return sum([self.is_in(loc-1j) and self.is_in(loc-1) and not self.is_in(loc-1j-1),
                    self.is_in(loc-1j) and self.is_in(loc+1) and not self.is_in(loc-1j+1),
                    self.is_in(loc+1j) and self.is_in(loc-1) and not self.is_in(loc+1j-1),
                    self.is_in(loc+1j) and self.is_in(loc+1) and not self.is_in(loc+1j+1)
            ])

    def convex_corners(self,loc):
        '''
        Convex corners like this:
            ...     The check for this concave corner is:
         000000...  If the cell above and left are empty:
         000000...       corners+=1
         001111...
         001111...
           ...

        '''
        return sum([self.is_not_in(loc-1j) and self.is_not_in(loc-1),
                    self.is_not_in(loc-1j) and self.is_not_in(loc+1),
                    self.is_not_in(loc+1j) and self.is_not_in(loc-1),
                    self.is_not_in(loc+1j) and self.is_not_in(loc+1)
            ])

    def perimeter2(self):
        corners=0
        for i in self.locations:
            corners+=self.convex_corners(i)
            corners+=self.concave_corners(i)
        sides=corners ## Geometry BITCHES!
        return sides

    def score1(self):
        return self.perimeter1()*self.area()

    def score2(self):
        return self.perimeter2()*self.area()
    
    def __str__(self):
        return f'<Region {self.name}: {self.locations}>'


class Grid:
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.diag_neighbours=[up*1j+down for up in [-1,1] for down in [-1,1] ]
        self.direct_neighbours=[1,-1,1j,-1j]
        self.reset_grid()
        self.find_regions()

    def reset_grid(self):
        self.regions=[]
        self.grid=defaultdict(str)
        self.location=defaultdict(list)

        for rownum,row in enumerate(self.inputdata):
            for colnum, char in enumerate(row):
                self.grid[colnum+rownum*1j]=char
        self.numrows=max([int(i.imag) for i in self.grid.keys()])
        self.numcols=max([int(i.real) for i in self.grid.keys()])

    def find_regions(self):
        seen_locations=set()
        for k,v in self.grid.items():
            if k in seen_locations:
                continue
            else:
                tocheck=deque()
                regionvalue=v
                curr_region=Region(regionvalue)
                tocheck.append(k)
                while len(tocheck):
                    currloc=tocheck.popleft()
                    if self.grid[currloc] == regionvalue:
                        curr_region.add(currloc)
                        seen_locations.add(currloc)
                        for loc in self.get_neighbours(currloc):
                            if loc not in seen_locations:
                                if loc not in tocheck:
                                    tocheck.append(loc)
                self.regions.append(curr_region)

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

    def score1(self):
        total=0
        for v in self.regions:
            total+=v.score1()
        return total

    def score2(self):
        total=0
        for v in self.regions:
            print(v.name, v.score2())
            total+=v.score2()
        return total

    def __len__(self):
        return self.numrows*self.numcols

    def __str__(self):
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                output+=self.grid[re+im*1j]
            output+='\n'
        return output

def part1(inputdata=testdata.split('\n')):
    g=Grid(inputdata)
    return g.score1()

def part2(inputdata=testdata.split('\n')):
    g=Grid(inputdata)
    return g.score2()

def day12_01():
    """Run part 1 of Day 12's code"""
    path = "./input/12.txt"
    print("1201:", part1(file_to_str_array(path)))


def day12_02():
    """Run part 2 of Day 12's code"""
    path = "./input/12.txt"
    print("1202:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day12_01()
    day12_02()





from collections import defaultdict,deque


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
                if char == '':
                    pass
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
        ''' Similar to the __str__ method, but allows annotation with a list of locations.
        Very useful for path finding
        '''
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

    def __str__(self):
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                output+=self.grid[re+im*1j]
            output+='\n'
        return output


testdata=['#......0',
          '......1.',
          '.....2..',
          '....3...',
          '...4....',
          '..5.....',
          '.6......',
          '7......*']


grid=Grid(testdata)
print(grid)
print(grid.get_neighbours(6,diags=True))

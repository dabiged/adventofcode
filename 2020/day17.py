"""
AOC day 17 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


class Conway3D:
    ''' A conway's game of life style game in 3 dimensions'''
    def __init__(self,inputdata):
        '''Read the initial state from a file'''
        self.board={}
        for row, rowdata in enumerate(inputdata):
            for col, char in enumerate(rowdata):
                if char == '#':
                    self.board[(row,col,0)] = '#'
                elif char == '.':
                    self.board[row,col,0] = '.'


    def __repr__(self):
        # pylint: disable-msg=too-many-locals
        '''print the board as a block for debugging'''
        minrow = maxrow= maxcol = mincol = minzplane = maxzplane = 0
        for point in self.board:
            minrow=min(minrow,point[0])
            maxrow=max(maxrow,point[0])
            mincol=min(mincol,point[1])
            maxcol=max(maxcol,point[1])
            minzplane=min(minzplane,point[2])
            maxzplane=max(maxzplane,point[2])
        output=''
        for zplane in range(minzplane,maxzplane+1):
            thiszplane='z='+str(zplane)+'\n'
            for row in range(minrow,maxrow+1):
                thisrow=''
                for col in range(mincol,maxcol+1):
                    if self.board[(row,col,zplane)] == '#':
                        thisrow+='#'
                    else:
                        thisrow+='.'
                thiszplane+=thisrow+'\n'
            output+=thiszplane+'\n'
        return output

    @staticmethod
    def get_all_neighbours(target):
        '''
        A generator method that gives all neighbours near a point in 3d space.
        '''
        for drow in range(-1,2):
            for dcol in range(-1,2):
                for dzplane in range(-1,2):
                    if drow == dcol == dzplane ==0:
                        pass
                    else:
                        yield (target[0]+drow, target[1]+dcol, target[2]+dzplane)

    def count_occupied(self,point):
        '''
        Count the number of occupied points near a point.
        '''
        numoccupied=0
        for thispoint in self.get_all_neighbours(point):
            if self.board.get(thispoint,False) == '#':
                numoccupied+=1
        return numoccupied

    def step(self):
        ''' Update the board according to the rules.'''
        occupied={}
        # Note the set comp below to only vist each point including neightbours once only
        for point in { point for centrecell in self.board \
                        for point in self.get_all_neighbours(centrecell)}:
            occupied[point] = self.count_occupied(point)
        for point, numneighbours in occupied.items():
            if self.board.get(point,False)== '#' and numneighbours in (2,3):
                self.board[point] = '#'
            elif self.board.get(point,False) != '#' and numneighbours == 3:
                self.board[point] = '#'
            else:
                self.board[point] ='.'

    def count_active(self):
        '''Returns the number of active points in the board'''
        return sum([val == '#' for val in self.board.values()])

    def run(self,numsteps):
        '''Run the game numsteps times'''
        for _ in range(numsteps):
            self.step()
        return self.count_active()

class Conway4D:
    ''' A conway's game of life style game in 4 dimensions'''
    def __init__(self,inputdata):
        '''initialise the board from a file'''
        self.board={}
        for row, rowdata in enumerate(inputdata):
            for col, char in enumerate(rowdata):
                if char == '#':
                    self.board[(row,col,0,0)] = '#'
                elif char == '.':
                    self.board[(row,col,0,0)] = '.'

    def __repr__(self):
        # pylint: disable-msg=too-many-locals
        '''print the board as a block for debugging'''
        minrow = maxrow= maxcol = mincol = minzplane = maxzplane=minw=maxw = 0
        for point in self.board:
            minrow=min(minrow,point[0])
            maxrow=max(maxrow,point[0])
            mincol=min(mincol,point[1])
            maxcol=max(maxcol,point[1])
            minzplane=min(minzplane,point[2])
            maxzplane=max(maxzplane,point[2])
            minw=min(minw,point[3])
            maxw=max(maxw,point[3])
        output=''
        for wplane in range(minw,maxw+1):
            for zplane in range(minzplane,maxzplane+1):
                thiszplane='z='+str(zplane)+', w='+str(wplane)+'\n'
                for row in range(minrow,maxrow+1):
                    thisrow=''
                    for col in range(mincol,maxcol+1):
                        if self.board[(row,col,zplane,wplane)] == '#':
                            thisrow+='#'
                        else:
                            thisrow+='.'
                    thiszplane+=thisrow+'\n'
                output+=thiszplane+'\n'
        return output

    @staticmethod
    def get_all_neighbours(target):
        '''
        A generator method that gives all neighbours near a point in 4d space.
        input: len(tuple) == 4
        output:len(tuple) == 4
        '''
        for drow in range(-1,2):
            for dcol in range(-1,2):
                for dzplane in range(-1,2):
                    for dwdim in range(-1,2):
                        if dwdim == drow == dcol == dzplane ==0:
                            # do not include current position
                            pass
                        else:
                            yield (target[0]+drow, \
                                   target[1]+dcol, \
                                   target[2]+dzplane, \
                                   target[3]+dwdim)

    def count_occupied(self,point):
        '''
        Count the number of occupied points near a point.
        '''
        numoccupied=0
        for thispoint in self.get_all_neighbours(point):
            if self.board.get(thispoint,False) == '#':
                numoccupied+=1
        return numoccupied

    def step(self):
        ''' Update the board'''
        occupied={}
        # Note the set comp below to only vist each point once
        for point in { point for centrecell in self.board \
                        for point in self.get_all_neighbours(centrecell)}:
            occupied[point] = self.count_occupied(point)
        for point, numneighbours in occupied.items():
            if self.board.get(point,False)== '#' and numneighbours in (2,3):
                self.board[point] = '#'
            elif self.board.get(point,False) != '#' and numneighbours == 3:
                self.board[point] = '#'
            else:
                self.board[point] ='.'

    def count_active(self):
        '''returns the number of active locations in the space'''
        return sum([val == '#' for val in self.board.values()])

    def run(self,numsteps):
        '''Run the simulation for numsteps'''
        for _ in range(numsteps):
            self.step()
        return self.count_active()



def day17_01():
    """Run part 1 of Day 17's code"""
    path = "./input/17/input.txt"
    mygame=Conway3D(file_to_str_array(path))
    result = mygame.run(6)
    print(f'1701: Number of active spaces after 6 steps (3D): {result}')

def day17_02():
    """Run part 2 of Day 17's code"""
    path = "./input/17/input.txt"
    mygame=Conway4D(file_to_str_array(path))
    result = mygame.run(6)
    print(f'1702: Number of active spaces after 6 steps (4D): {result}')

if __name__ == "__main__":
    day17_01()
    day17_02()

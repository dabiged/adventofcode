from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


test_input=''''''.split('\n')

class Forest():
    def __init__(self,heights):
        self.heights=heights
        self.visible={}
        self.heightmap={}
        self.scenicscore={}
        self.maxrow=-1
        self.maxcol=-1

    def parse(self):
        maxrow,maxcol=0,0
        for rownum,row in enumerate(self.heights):
            for colnum, height in enumerate(row):
                self.heightmap[(rownum,colnum)] = int(height)
                self.maxcol=max(colnum,self.maxcol)
            self.maxrow=max(rownum,self.maxrow)

    def calc_visible(self):
        for row in range(self.maxrow+1):
            for col in range(self.maxcol+1):
                point=(row,col)
                if row == self.maxrow or col == self.maxcol or col == 0 or row ==0:
                    self.visible[point]=True
                elif self.visible_left(point) or self.visible_right(point) or self.visible_up(point) or self.visible_down(point):
                    self.visible[point]=True
                else:
                    self.visible[point]=False

    def calc_scenic(self):
        for row in range(1,self.maxrow):
            for col in range(1,self.maxcol):
                point=(row,col)
                self.scenicscore[point]=self.count_up(point)*self.count_down(point)*self.count_left(point)*self.count_right(point)
        return max(self.scenicscore.values())

    def count_up(self,point):
        dist=1
        row,col=point
        for treerow in range(row-1,0,-1):
            if self.heightmap[treerow,col] < self.heightmap[point]:
                dist+=1
            else:
                return dist
        return dist

    def count_down(self,point):
        dist=1
        row,col=point
        for treerow in range(row+1,self.maxrow):
            if self.heightmap[treerow,col] < self.heightmap[point]:
                dist+=1
            else:
                return dist
        return dist

    def count_right(self,point):
        dist=1
        row,col=point
        for treecol in range(col+1,self.maxcol):
            if self.heightmap[row,treecol] < self.heightmap[point]:
                dist+=1
            else:
                return dist
        return dist



    def count_left(self,point):
        dist=1
        row,col=point
        for treecol in range(col-1,0,-1):
            if self.heightmap[row,treecol] < self.heightmap[point]:
                dist+=1
            else:
                return dist
        return dist

    def visible_left(self,point):
        row,col=point
        return self.heightmap[point] > max([self.heightmap[(i,col)] for i in range(0,row)])

    def visible_right(self,point):
        row,col=point
        return self.heightmap[point] > max([self.heightmap[(i,col)] for i in range(row+1,self.maxrow+1)])

    def visible_up(self,point):
        row,col=point
        return self.heightmap[point] > max([self.heightmap[(row,i)] for i in range(0,col)])

    def visible_down(self,point):
        row,col=point
        return self.heightmap[point] > max([self.heightmap[(row,i)] for i in range(col+1,self.maxcol+1)])

    def count_visible(self):
        return sum(self.visible.values())

def main1(data):
    f=Forest(data)
    f.parse()
    f.calc_visible()
    return f.count_visible()

def main2(data):
    f=Forest(data)
    f.parse()
    return f.calc_scenic()

def day08_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_08.txt"
    print("0801:",main1(file_to_str_array(path)))

def day08_02():
    """Run part 4 of Day 1's code"""
    path = "./input/input_08.txt"
    print("0802:",main2(file_to_str_array(path)))

if __name__ == "__main__":
    day08_01()
    day08_02()

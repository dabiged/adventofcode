"""
AOC day 17 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class TrickShot():
    def __init__(self,minx,maxx,miny,maxy):
        self.minx=minx
        self.maxx=maxx
        self.miny=miny
        self.maxy=maxy

    def shoot(self,velx,vely,startx=0,starty=0):
        x,y=startx,starty
        maxy=0
        done=False
        while not done:
            if self.minx <= x <= self.maxx and self.miny <= y <= self.maxy:
                return (True, maxy)
            if y < self.miny:
                return (False, 0)
            x+=velx
            y+=vely
            maxy=max(y,maxy)
            if velx == 0:
                pass
            elif abs(velx) == velx:
                #positive
                velx-=1
            elif abs(velx) == -velx:
                velx+=1
            else:
                raise ValueError
            vely-=1
            #print(x,y,velx,vely)


    def find_highest(self,maxxvel, maxyvel):
        maxys={}
        for xvel in range(0,maxxvel):
            for yvel in range(0,maxyvel):
                ans,maxy=self.shoot(xvel,yvel)
                if ans:
                    maxys[(xvel,yvel)]=maxy
        return max(maxys.values())

    def find_all(self):
        maxys={}
        for xvel in range(0,self.maxx+1):
            for yvel in range(self.miny,98):
                ans,maxy=self.shoot(xvel,yvel)
                if ans :
                    maxys[(xvel,yvel)]=maxy
        return len(maxys)




def day17_01():
    """Run part 1 of Day 17's code"""
    shooter=TrickShot(137,171,-98,-73)
    result=shooter.find_highest(18,100)
    print(f'1701: {result} ')

def day17_02():
    """Run part 2 of Day 17's code"""
    shooter=TrickShot(137,171,-98,-73)
    result=shooter.find_all()
    print(f'1702: {result}')

if __name__ == "__main__":
    day17_01()
    day17_02()

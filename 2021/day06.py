"""
AOC day 06 2018
"""
from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

class FishSpawn():
    def __init__(self,inputfile,numsteps=0):
        self.inputfile=inputfile
        self.numsteps=numsteps
        self.timer=0
        self.ages=defaultdict(int)
        self.inputdata=file_to_str_array(self.inputfile)
        for age in self.inputdata[0].split(','):
            self.ages[int(age)]+=1

    def step(self):
        newage=defaultdict(int)
        for age,count in self.ages.items():
            newage[age-1]=count
        newage[6]+=newage[-1]
        newage[8]+=newage[-1]
        del newage[-1]
        del self.ages
        self.ages=newage
    def stepp2(self):
        newage=defaultdict(int)
        for age,count in self.ages.items():
            newage[age-1]=count
        newage[6]+=newage[-1]
        newage[8]+=newage[-1]
        self.ages=newage

    def run(self):
        for self.timer in range(self.numsteps):
            self.step()

    def runp2(self):
        for self.timer in range(self.numsteps):
            self.step()

    def count(self):
        return sum(self.ages.values())



def day06_01():
    """Run part 1 of Day 06's code"""
    inputfile = "./input/day06.txt"
    testspawn=FishSpawn(inputfile,80)
    testspawn.run()
    result = testspawn.count()
    print(f'0601: {result} laternfish after 80 days')

def day06_02():
    """Run part 2 of Day 06's code"""
    inputfile = "./input/day06.txt"
    testspawn=FishSpawn(inputfile,256)
    testspawn.run()
    result = testspawn.count()
    print(f'0602: {result} lanternfish after 256 days.')

if __name__ == "__main__":
    day06_01()
    day06_02()

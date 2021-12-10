"""
AOC day 07 2018
"""
from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

class FuelCalc():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.importdata()
        self.positioncosts=defaultdict(int)

    def calc_two_move(self,currentposition,target):
        #movecost=0
        #for i in range(1,abs(currentposition-target)+1):
        #    movecost+=i
        n=abs(currentposition-target)
        return int(n*(n+1)/2)

    def calc_one_move(self,currentposition,target):
        return abs(currentposition-target)

    def importdata(self):
        with open(self.inputfile,'r') as f:
            datastr=f.readline()
        self.inputdata=[int(i) for i in datastr.split(',')]

    def run2(self):
        for testposition in range(min(self.inputdata),max(self.inputdata)+1):
            totalfuel=0
            for i in self.inputdata:
                totalfuel+=self.calc_two_move(i,testposition)
            self.positioncosts[testposition]=totalfuel

    def run(self):
        for testposition in range(min(self.inputdata),max(self.inputdata)+1):
            totalfuel=0
            for i in self.inputdata:
                totalfuel+=self.calc_one_move(i,testposition)
            self.positioncosts[testposition]=totalfuel

    def get_best_position(self):
        cheapestpositioncost=min(self.positioncosts.values())
        for key,value in self.positioncosts.items():
            if value == cheapestpositioncost:
                return key,value



def day07_01():
    """Run part 1 of Day 07's code"""
    inputfile = "./input/day07.txt"
    testfuelcalc=FuelCalc(inputfile)
    testfuelcalc.run()
    position,cost=testfuelcalc.get_best_position()

    result= cost
    print(f'0701: {result} Fuel required')

def day07_02():
    """Run part 2 of Day 07's code"""
    inputfile = "./input/day07.txt"
    testfuelcalc=FuelCalc(inputfile)
    testfuelcalc.run2()
    position,cost=testfuelcalc.get_best_position()

    result= cost
    print(f'0702: {result} fuel required')

if __name__ == "__main__":
    day07_01()
    day07_02()

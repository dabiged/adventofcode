"""
AOC day XX 2018
"""
from lib.filehelper import file_to_str_array
from collections import deque, defaultdict
# pylint: disable=missing-module-docstring

class dayXX():
    def __init__(self,inputfile):
        self.inputfile=inputfile



        self.processinputfile()

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)

    def part1(self):
        pass

    def part2(self):
        pass



def dayXX_01():
    """Run part 1 of Day XX's code"""
    path = "./input/dayXX.txt"
    result=""
    print(f'XX01: {result}')

def dayXX_02():
    """Run part 2 of Day XX's code"""
    path = "./input/dayXX.txt"
    result=""
    print(f'XX02: {result}')

if __name__ == "__main__":
    dayXX_01()
    #dayXX_02()

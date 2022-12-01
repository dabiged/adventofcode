"""
AOC day 18 2018
"""
from lib.filehelper import file_to_str_array
from collections import deque, defaultdict
# pylint: disable=missing-module-docstring

class day18():
    def __init__(self,inputfile):
        self.inputfile=inputfile



        self.processinputfile()

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)

    def part1(self):
        pass

    def part2(self):
        pass



def day18_01():
    """Run part 1 of Day 18's code"""
    path = "./input/day18.txt"
    result=""
    print(f'1801: {result}')

def day18_02():
    """Run part 2 of Day 18's code"""
    path = "./input/day18.txt"
    result=""
    print(f'1802: {result}')

if __name__ == "__main__":
    day18_01()
    #day18_02()

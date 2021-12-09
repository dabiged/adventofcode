"""
AOC day 08 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class SevenSegDecoder():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.data=self.process_inputfile()
        actuals={0:set('abcefg'),1:set('cf'),2:set('acdeg'),3:set('acdfg'),4:set('bcdf'),
                       5:set('abdfg'),6:set('abdefg'),7:set('acf'),8:set('abcdefg'),9:set('abcdfg')}
    def process_inputfile(self):
        data=file_to_str_array(self.inputfile)
        self.digits=[]
        self.measurements=[]
        for line in data:
            digits, measurements = tuple(line.split('|'))
            print(digits.split())
            self.digits.append(list(map(set, digits.split())))
            self.measurements.append(list(map(set, measurements.split())))

    def part1(self):
        count=0
        for line in self.measurements:
            for val in line:
                if len(val) in (2,3,4,7):
                    count+=1
        return count

def day08_01():
    """Run part 1 of Day 08's code"""
    path = "./input/day08.txt"
    testdecode=SevenSegDecoder(path)
    result=testdecode.part1()
    print(f'0801: {result}')

def day08_02():
    """Run part 2 of Day 08's code"""
    path = "./input/08/input.txt"
    result=""
    print(f'0802: {result}')

if __name__ == "__main__":
    day08_01()
    #day08_02()

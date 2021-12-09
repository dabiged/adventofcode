"""
AOC day 08 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class digits():
    def __init__(self,digits):
        self.digits=digits # list of str
        self.digits=["".join(sorted(i)) for i in self.digits]
        self.fourminus1=''
        self.todigit={} # key str of element lit, value: digit

    def set2str(self,myset):
        return "".join([i for i in myset])

    def digit2str(self,digit):
        ''' given a digit return the mangled string '''
        for key,value in self.todigit.items():
            if value==digit:
                return key

    def solve(self):
        self.solve1()
        self.solve4()
        self.solve7()
        self.solve8()
        self.solve9()
        self.solve3()
        self.fourminus1=self.get4minus1()
        self.solve6()
        self.solve0()
        self.solve5()
        self.solve2()
        return self.todigit

    def get4minus1(self):
        return self.set2str(set(self.digit2str(4))-(set(self.digit2str(1))))

    def solve5(self):
        for char in self.digits:
            if len( char) == 5:
                if len(char) == len(set(char).union(set(self.fourminus1))):
                    self.todigit[self.set2str(char)] = 5
                    self.digits.remove(char)
                    return None

    def solve2(self):
        for char in self.digits:
            if len( char) == 5:
                self.todigit[self.set2str(char)] = 2
                self.digits.remove(char)
                return None


    def solve0(self):
        for char in self.digits:
            if len( char) == 6:
                self.todigit[self.set2str(char)] = 0
                self.digits.remove(char)
                return None

    def solve6(self):
        for char in self.digits:
            if len( char) == 6:
                if len(char) == len(set(char).union(set(self.fourminus1))):
                    self.todigit[char] = 6
                    self.digits.remove(char)
                    return None

    def solve3(self):
        for char in self.digits:
            if len( char) == 5:
                if len(char) == len(set(char).union(set(self.digit2str(1)))):
                    self.todigit[self.set2str(char)] = 3
                    self.digits.remove(char)
                    return None

    def solve9(self):
        for char in self.digits:
            if len( char) == 6:
                if len(char) == len(set(char).union(set(self.digit2str(4)))):
                    self.todigit[char] = 9
                    self.digits.remove(char)
                    return None


    def solve1(self):
        for chars in self.digits:
            if len(chars) == 2:
                self.todigit[chars]=1
                self.digits.remove(chars)
                return None

    def solve7(self):
        for chars in self.digits:
            if len(chars) == 3:
                self.todigit[chars]=7
                self.digits.remove(chars)
                return None

    def solve4(self):
        for chars in self.digits:
            if len(chars) == 4:
                self.todigit[chars]=4
                self.digits.remove(chars)
                return None

    def solve8(self):
        for chars in self.digits:
            if len(chars) == 7:
                self.todigit[chars]=8
                self.digits.remove(chars)
                return None

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
            self.digits.append(digits.split())
            self.measurements.append(measurements.split())

    def part1(self):
        count=0
        for line in self.measurements:
            for val in line:
                if len(val) in (2,3,4,7):
                    count+=1
        return count


    def part2(self):
        total=0
        for measurement,thesedigits in zip(self.measurements,self.digits):
            solution=digits(thesedigits)
            lookup=solution.solve()
            val=""
            for measure in measurement:
                val+=str(lookup["".join(sorted(measure))])
            total+=int(val)
        return total

def day08_01():
    """Run part 1 of Day 08's code"""
    path = "./input/day08.txt"
    testdecode=SevenSegDecoder(path)
    result=testdecode.part1()
    print(f'0801: {result} appearances of 1, 4, 7 or 8.')

def day08_02():
    """Run part 2 of Day 08's code"""
    inputfile = "./input/day08.txt"
    testdecode=SevenSegDecoder(inputfile)
    result=testdecode.part2()
    print(f'0802: {result} is the product of all readings')

if __name__ == "__main__":
    day08_01()
    day08_02()

from lib.filehelper import file_to_str_array
import re
# pylint: disable=missing-module-docstring

testdata='''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
testdata1='''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
regex='''mul\\([0-9]{1,3},[0-9]{1,3}\\)'''
regex1='do\\(\\).*?don\'t\\(\\)'

def multiply(inputstr):
    a=re.findall('\\([0-9]{1,3},',inputstr)[0][1:-1]
    b=re.findall(',[0-9]{1,3}\\)',inputstr)[0][1:-1]
    return int(a)*int(b)

def part1(inputdata=testdata):
    x=re.findall(regex,inputdata)
    total=0
    for mult in x:
        total+=multiply(mult)
    return total

def part2(inputdata=testdata1):
    inputdata='do()'+inputdata+"don't()"
    x=re.findall(regex1,inputdata)

    total=0
    for goodstr in x:
        total+=part1(goodstr)
    return total

def day03_01():
    """Run part 1 of Day 3's code"""
    path = "./input/03.txt"
    print("0301:", part1(file_to_str_array(path)[0]))


def day03_02():
    """Run part 2 of Day 3's code"""
    path = "./input/03.txt"
    print("0302:", part2(file_to_str_array(path)[0]))

if __name__ == "__main__":
    day03_01()
    day03_02()


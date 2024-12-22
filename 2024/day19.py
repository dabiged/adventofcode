from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from functools import cache

testdata='''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''

@cache
def number_of_ways_to_make_design(design):
    ans=0
    if len(design) == 0:
        return 1
    for towel in towel_list:
        if design.startswith(towel):
            ans+=number_of_ways_to_make_design(design[len(towel):])
    return ans

def part1(inputdata=testdata.split('\n')):
    global towel_list
    towel_list=inputdata[0].split(', ')
    designs=inputdata[2:]
    ans=0
    for design in designs:
        if number_of_ways_to_make_design(design)>0:
            ans+=1
    return ans

def part2(inputdata=testdata):
    global towel_list
    towel_list=inputdata[0].split(', ')
    designs=inputdata[2:]
    ans=0
    for design in designs:
        ans+=number_of_ways_to_make_design(design)
    return ans

def day19_01():
    """Run part 1 of Day 19's code"""
    path = "./input/19.txt"
    print("1901:", part1(file_to_str_array(path)))


def day19_02():
    """Run part 2 of Day 19's code"""
    path = "./input/19.txt"
    print("1902:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day19_01()
    day19_02()

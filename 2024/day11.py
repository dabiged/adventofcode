from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

testdata='''125 17'''

def parse(inputdata):
    stones=defaultdict(int)
    for i in inputdata.split():
        stones[int(i)]+=1
    return stones

def blink(stones):
    # don't store the order, just the number of times each stone value occurs.
    # new stones: key = number on the stone, value = number of occurances.
    new_stones=defaultdict(int)
    for stone in stones:
        if stones[stone] >0:
            if stone == 0:
                new_stones[1]+=stones[0]
            elif len(str(stone)) % 2 == 0:
                s=str(stone)
                new_stones[int(s[:len(s)//2])] += stones[stone]
                new_stones[int(s[len(s)//2:])] += stones[stone]
            else:
                new_stones[stone*2024]+=stones[stone]
    return new_stones

def run(starting_stones,ntimes):
    for i in range(ntimes):
        starting_stones = blink(starting_stones)
    return sum(starting_stones.values())

def part1(inputdata=testdata):
    a=parse(inputdata)
    return run(parse(inputdata),25)

def part2(inputdata=testdata):
    a=parse(inputdata)
    return run(parse(inputdata),75)


def day11_01():
    """Run part 1 of Day 11's code"""
    path = "./input/11.txt"
    print("1101:", part1(file_to_str_array(path)[0]))


def day11_02():
    """Run part 2 of Day 11's code"""
    path = "./input/11.txt"
    print("1102:", part2(file_to_str_array(path)[0]))

if __name__ == "__main__":
    day11_01()
    day11_02()

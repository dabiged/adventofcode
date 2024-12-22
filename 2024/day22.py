from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from functools import cache
from collections import defaultdict
import math

testdata='''1
2
3
2024'''

@cache
def next_number(num):
    num = ( num ^ ( num * 64 ) ) % 16777216 
    num = ( num ^ math.floor(num / 32 ) ) % 16777216
    num = ( num ^ ( num * 2048 ) ) % 16777216
    return num

def part1(inputdata=testdata.split('\n')):
    ans=0
    for i in inputdata:
        num=int(i)
        for _ in range(2000):
            num=next_number(num)
        ans+=num
    return ans

def part2(inputdata=testdata.split('\n')):
    # k = the last 4 changes, (as a tuple, since lists are unhashable)
    # v = total number of bananas I get for this combo
    sequence_values=defaultdict(int)
    for i,initial_number in enumerate(inputdata):
        print(i)
        number=int(initial_number)
        # All the sequences I have seen for this number (list of 4 ints)
        sequences=[]
        # the last 4 differences for this number, most recent last
        differences=[]
        for _ in range(2000):
            new_number=next_number(number)
            delta = (new_number % 10) - (number % 10)
            if len(differences) == 4:
                _ = differences.pop(0)
            differences.append(delta)
            #                                 Cannot reuse sequences.
            if len(differences) == 4 and not ( tuple(differences) in sequences):
                sequence_values[tuple(differences)] += new_number % 10
                sequences.append(tuple(differences))
            number=new_number

    return max(sequence_values.values())

def day22_01():
    """Run part 1 of Day 22's code"""
    path = "./input/22.txt"
    print("2201:", part1(file_to_str_array(path)))

def day22_02():
    """Run part 2 of Day 22's code"""
    path = "./input/22.txt"
    print("2202:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day22_01()
    day22_02()

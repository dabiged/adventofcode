"""
Advent of Code Day 02 2021
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def day02_01(inputlist):
    """Run part 1 of Day 2's code"""
    vert=0
    horz=0
    for command in inputlist:
        direction,num = tuple(command.split(" "))
        num=int(num)
        if direction == 'up':
            vert-=num
        if direction == 'down':
            vert+=num
        if  direction == 'forward':
            horz+=num
    print(f'0201: {horz*vert} is the product of the final depth and horizontal position.')
    return horz*vert


def day02_02(inputlist):
    """Run part 2 of Day 2's code"""
    vert=0
    horz=0
    aim=0
    for command in inputlist:
        direction,num = tuple(command.split(" "))
        num=int(num)
        if direction == 'up':
            aim-=num
        if direction == 'down':
            aim+=num
        if  direction == 'forward':
            horz+=num
            vert+=aim*num
    print(f'0202: {horz*vert} is the product of the final depth and horizontal position.')
    return horz*vert

if __name__ == "__main__":
    PATH = "./input/day02.txt"
    inputdata=file_to_str_array(PATH)
    day02_01(inputdata)
    day02_02(inputdata)

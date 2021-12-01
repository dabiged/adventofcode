"""
Advent of Code Day 01 2021
"""
from lib.filehelper import file_to_array
# pylint: disable=missing-module-docstring

def day01_01(inputlist):
    """Run part 1 of Day 1's code"""
    count=0
    old=9999
    for i in inputlist:
        if i >old:
            count+=1
        old=i

    print(f"0101: {count}")
    return count


def day01_02(inputlist):
    """Run part 2 of Day 1's code"""
    count=0
    old=9999
    for i,_ in enumerate(inputlist):
        if i not in (0,1):
            sumof3=sum(inputlist[i-2:i+1])
            if sumof3>old:
                count+=1
            old=sumof3

    print(f"0103: {count}")
    return count


if __name__ == "__main__":
    PATH = "./input/day01.txt"
    inputdata=file_to_array(PATH)
    day01_01(inputdata)
    day01_02(inputdata)

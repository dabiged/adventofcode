"""
Advent of Code Day 01 2021
"""
from lib.filehelper import file_to_array
# pylint: disable=missing-module-docstring

def gt_previous(inputlist):
    """Run part 1 of Day 1's code"""
    count=0
    old=9999
    for i in inputlist:
        if i >old:
            count+=1
        old=i

    return count


def gt_previous_smoothed(inputlist):
    """Run part 2 of Day 1's code"""
    count=0
    old=9999
    for i,_ in enumerate(inputlist):
        if i not in (0,1):
            sumof3=sum(inputlist[i-2:i+1])
            if sumof3>old:
                count+=1
            old=sumof3
    return count


def day01_01():
    PATH = "./input/day01.txt"
    inputlist=file_to_array(PATH)
    result=gt_previous(inputlist)
    print(f"0101: {result} Measurements larger than the previous measurement.")

def day01_02():
    PATH = "./input/day01.txt"
    inputlist=file_to_array(PATH)
    result=gt_previous_smoothed(inputlist)
    print(f"0102: {result} sums larger than the previous sum.")

if __name__ == "__main__":
    day01_01()
    day01_02()

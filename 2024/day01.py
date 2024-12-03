from lib.filehelper import file_to_str_array
import re
# pylint: disable=missing-module-docstring


testdata=["3   4",
"4   3",
"2   5",
"1   3",
"3   9",
"3   3"]

def part1(data=testdata):
    collect=0
    a,b = [],[]
    for i in data:
        i,j=i.split()
        a.append(int(i))
        b.append(int(j))
    a.sort()
    b.sort()
    for a,b in zip(a,b):
        collect=abs(a-b)+collect
    return collect

def part2(data=testdata):
    collect=0
    a,b = [],[]
    a,b = [],[]
    for i in data:
        i,j=i.split()
        a.append(int(i))
        b.append(int(j))
    a.sort()
    b.sort()
    for i in a:
        cnt=0
        for j in b:
            if i==j:
                cnt+=1
        collect+=cnt*i
    return collect

def day01_01():
    """Run part 1 of Day 1's code"""
    path = "./input/01.txt"
    print("0101:", part1(file_to_str_array(path)))


def day01_02():
    """Run part 2 of Day 1's code"""
    path = "./input/01.txt"
    print("0102:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day01_01()
    day01_02()

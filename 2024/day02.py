from lib.filehelper import file_to_str_array
import copy
# pylint: disable=missing-module-docstring

test_input=[
"7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9"
        ]

def issafe(i):
    return  ( sorted(i) == i or sorted(i,reverse=True) == i) and \
            max([abs(a - b) for a, b in zip(i[1:],i[:-1])]) <=3 and \
            min([abs(a - b) for a, b in zip(i[1:],i[:-1])])  >0 

def part1(inputdata=test_input):
    cnt=0
    for row in inputdata:
        i=[int(val) for val in row.split()]
        if issafe(i):
            cnt+=1
    return cnt


def part2(inputdata=test_input):
    cnt=0
    for row in inputdata:
        ints=[int(val) for val in row.split()]
        for i in range(len(ints)):
            a=copy.deepcopy(ints)
            del(a[i])
            if issafe(a):
                cnt+=1
                break
    return cnt

def day02_01():
    """Run part 1 of Day 1's code"""
    path = "./input/02.txt"
    print("0201:", part1(file_to_str_array(path)))


def day02_02():
    """Run part 2 of Day 1's code"""
    path = "./input/02.txt"
    print("0202:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day02_01()
    day02_02()

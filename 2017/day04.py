from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from collections import Counter


def count_valid2(line):
    seen_pws=[]
    for pw in line.split():
        letters=Counter(list(pw))
        if letters in seen_pws:
            return 0
        seen_pws.append(letters)
    return 1

def count_valid(line):
    seen_pws=[]
    for pw in line.split():
        if pw in seen_pws:
            return 0
        seen_pws.append(pw)
    return 1



def day04_01():
    """Run part 1 of Day 1's code"""
    path = "./input/04/input.txt"
    print("0401:",sum(map(count_valid,file_to_str_array(path))))



def day04_02():
    """Run part 2 of Day 4's code"""
    path = "./input/04/input.txt"
    print("0402:",sum(map(count_valid2,file_to_str_array(path))))


if __name__ == "__main__":
    day04_01()
    day04_02()

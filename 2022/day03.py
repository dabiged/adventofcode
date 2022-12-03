from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

test_data='''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split('\n')

score={}
for i, val in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', start =1 ):
    score[val] = i


def main(inputlist):
    totalscore=0
    for entry in inputlist:
        bag1,bag2 = entry[:len(entry)//2],entry[len(entry)//2:]
        overlap=set()
        for i in bag1:
            if i in bag2:
                overlap.add(i)
        if overlap :
            for symbol in overlap:
                totalscore += score[symbol]

    return totalscore



def get_3(inputlist):
    for i in range(0,len(inputlist),3):
        yield inputlist[i], inputlist[i+1], inputlist[i+2]

def main2(data):
    totalscore=0
    for bag1,bag2,bag3 in get_3(data):
        common=set(bag1).intersection(set(bag2)).intersection(set(bag3))
        for val in common:
            totalscore+=score[val]
    return totalscore

def day03_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_03.txt"
    print("0301:", main(file_to_str_array(path)))


def day03_02():
    """Run part 3 of Day 1's code"""
    path = "./input/input_03.txt"
    print("0302:", main2(file_to_str_array(path)))

if __name__ == "__main__":
    day03_01()
    day03_02()

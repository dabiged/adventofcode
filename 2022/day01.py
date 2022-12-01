from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


def calc_most_cal(inputlist):
    elves=[]
    thiself=0
    for entry in inputlist:
        if entry == "":
            elves.append(thiself)
            thiself=0
        else:
            thiself+=int(entry)
    return max(elves)

def calc_top3_cal(inputlist):
    elves=[]
    thiself=0
    for entry in inputlist:
        if entry == "":
            elves.append(thiself)
            thiself=0
        else:
            thiself+=int(entry)
    top3=0
    top3+=elves.pop(elves.index(max(elves)))
    top3+=elves.pop(elves.index(max(elves)))
    top3+=elves.pop(elves.index(max(elves)))

    return top3



def day01_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_01.txt"
    print("0101:", calc_most_cal(file_to_str_array(path)))


def day01_02():
    """Run part 2 of Day 1's code"""
    path = "./input/input_01.txt"
    print("0102:", calc_top3_cal(file_to_str_array(path)))

if __name__ == "__main__":
    day01_01()
    day01_02()

from lib.filehelper import file_to_str_array, get_bald_string_list_from_file, file_to_array
# pylint: disable=missing-module-docstring


test_input=['0 3 6 9 12 15',
'1 3 6 10 15 21',
'10 13 16 21 30 45']

def get_next(inputlist):
    differences=[]
    for i,j in zip(inputlist[0:-1],inputlist[1:]):
        differences.append(j-i)
    if all([a==0 for a in differences]):
        return inputlist[-1]
    else:
        return inputlist[-1]+get_next(differences)


def get_prev(inputlist):
    differences=[]
    for i,j in zip(inputlist[0:-1],inputlist[1:]):
        differences.append(j-i)
    if all([a==0 for a in differences]):
        return inputlist[0]
    else:
        return inputlist[0]-get_prev(differences)


def part1(inputdata=test_input):
    counter=0

    for row in inputdata:
        data=[i for i in map(int,row.split())]
        counter+=get_next(data)
    return counter

def part2(inputdata=test_input):
    counter=0
    for row in inputdata:
        data=[i for i in map(int,row.split())]
        counter+=get_prev(data)
    return counter



def day09_01():
    """Run part 1 of Day 7's code"""
    path = "./input/09.txt"
    print("0901:", part1(file_to_str_array(path)))


def day09_02():
    """Run part 2 of Day 1's code"""
    path = "./input/09.txt"
    print("0902:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day09_01()
    day09_02()

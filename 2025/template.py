from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


def part1(inputdata=testdata):
    pass

def part2(inputdata=testdata):
    pass


def dayXXXX_01():
    """Run part 1 of Day XXXX's code"""
    path = "./input/XXXX.txt"
    print("XXXX01:", part1(file_to_str_array(path)))


def dayXXXX_02():
    """Run part 2 of Day XXXX's code"""
    path = "./input/XXXX.txt"
    print("XXXX02:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    dayXXXX_01()
    dayXXXX_02()

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def calc_checksum(inputlist):
    checksum=0
    for line in inputlist:
        input_vals=line.split()
        vals=list(map(int,input_vals))

        checksum+=max(vals)-min(vals)
    return checksum


def calc_checksum2(inputlist):
    checksum=0
    for line in inputlist:
        input_vals=line.split()
        vals=list(map(int,input_vals))

        for i,x in enumerate(vals):
            for j,y in enumerate(vals):
                if i == j:
                    continue
                if x % y == 0:
                    checksum+= int(x)//int(y)
                elif y % x == 0:
                    checksum+=y//x
                else:
                    pass

    return checksum//2

def day01_01():
    """Run part 1 of Day 1's code"""
    path = "./input/02/input.txt"
    print("0201:",calc_checksum(file_to_str_array(path)))



def day01_02():
    """Run part 2 of Day 1's code"""
    path = "./input/02/input.txt"
    print("0202:",calc_checksum2(file_to_str_array(path)))


if __name__ == "__main__":
    day01_01()
    day01_02()

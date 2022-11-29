from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


def calc_captcha(inputstr):
    output=0
    for i,char in enumerate(inputstr):
        if i == 0:
            lastnum=char
            continue
        if char==lastnum:
            output+=int(char)
        lastnum=char
    if inputstr[0] == inputstr[-1]:
        output+=int(inputstr[0])
    return output

def calc_match(pos,inputstr):
    size=len(inputstr)
    print(size)
    output = ((pos+(size//2)) % size )
    if output==size:
        output=0
    return output

def calc_recaptcha(inputstr):
    output=0

    for i,char in enumerate(inputstr):
        if inputstr[i] == inputstr[calc_match(i,inputstr)]:
            print(i,char)

            output+=int(char)

    return output

def day01_01():
    """Run part 1 of Day 1's code"""
    path = "./input/01/input.txt"
    print("0101:",calc_captcha(file_to_str_array(path)[0]))



def day01_02():
    """Run part 2 of Day 1's code"""
    path = "./input/01/input.txt"
    print("0102:",calc_recaptcha(file_to_str_array(path)[0]))


if __name__ == "__main__":
    day01_01()
    day01_02()

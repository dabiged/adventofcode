from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


test_input='''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122'''.split('\n')

def toint(mystr):
    base=5
    answer=0
    for exponent,item in enumerate(mystr[::-1]):
        if item == '=':
            item=-2
        if item == '-':
            item =-1
        answer+=int(item)*base**exponent
    return answer


def tosnafu(myint):
    result=[]
    while myint > 0:
        result.append("012=-"[ myint % 5 ])
        myint=(2+myint)//5
    return "".join(result[::-1])


def main1(input_data):
    answer=0
    for snafu in input_data:
        answer+=toint(snafu)
    return tosnafu(answer)


def day25_01():
    """Run part 1 of Day 25's code"""
    path = "./input/input_25.txt"
    print("2501:",main1(file_to_str_array(path)))


if __name__ == "__main__":
    day25_01()


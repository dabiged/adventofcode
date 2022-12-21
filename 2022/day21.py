from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

import json

test_data='''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''.split('\n')

def parse(inputtext):
    inputdata={}
    for row in inputtext:
        k=row.split(':')[0]
        v=row.split(':')[1]
        inputdata[k]=v
    return inputdata

def calculate1(data,node):

    assert node in data.keys()

    line=data[node].split()

    if len(line) == 1 and line[0].isnumeric():
        return int(line[0])
    else:
        operator=line[1]
        if operator == '*':
            return calculate(data,line[0]) * calculate(data,line[2])
        if operator == '+':
            return calculate(data,line[0]) + calculate(data,line[2])
        if operator == '-':
            return calculate(data,line[0]) - calculate(data,line[2])
        if operator == '/':
            return int(calculate(data,line[0]) / calculate(data,line[2]))



def main1(input_data):
    return calculate1(parse(input_data),'root')


def main2(data):
    pass

def day21_01():
    """Run part 1 of Day 21's code"""
    path = "./input/input_21.txt"
    print("2101:",main1(file_to_str_array(path)))

def day21_02():
    """Run part 2 of Day 21's code"""
    path = "./input/input_21.txt"
    print("2102:")

if __name__ == "__main__":
    day21_01()
    day21_02()


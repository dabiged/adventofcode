from lib.filehelper import file_to_str_array
import re
# pylint: disable=missing-module-docstring

testdata=['1abc2',
'pqr3stu8vwx',
'a1b2c3d4e5f',
'treb7uchet']

moretestdata=['two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen']


def extract_numbers(input_str):
    numchars=''
    for char in input_str:
        if char.isnumeric():
            numchars+=char
    return int(numchars[0]+numchars[-1])

def extract_words(input_str):
    input_str=re.sub('one','o1e',input_str)
    input_str=re.sub('two','t2o',input_str)
    input_str=re.sub('three','t3e',input_str)
    input_str=re.sub('four','f4r',input_str)
    input_str=re.sub('five','f5e',input_str)
    input_str=re.sub('six','s6x',input_str)
    input_str=re.sub('seven','s7n',input_str)
    input_str=re.sub('eight','e8t',input_str)
    input_str=re.sub('nine','n9e',input_str)
    return input_str

def part1(data=testdata):
    calib_sum=0
    for test_str in data:
        calib_sum+=int(extract_numbers(test_str))
    return calib_sum

def part2(data=moretestdata):
    calib_sum=0
    for test_str in data:
        calib_sum+=int(extract_numbers(extract_words(test_str)))
    return calib_sum

def day01_01():
    """Run part 1 of Day 1's code"""
    path = "./input/01.txt"
    print("0101:", part1(file_to_str_array(path)))


def day01_02():
    """Run part 2 of Day 1's code"""
    path = "./input/01.txt"
    print("0102:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day01_01()
    day01_02()

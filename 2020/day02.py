"""
Advent of Code Day 02 2020
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def isvalidpw(inputline):
    """
    Tests if a password conforms to a given set of rules.
    input is of the form:
    Num range letter: password

    For example:
    15-16 l: ksadfsadfsadfsadfll

    Which means:
    15-16:                  min-max number of times the requested letter must be in the password
    l                       letter that must be in the password
    ksadfsadfsadfsadfll:    the password to be checked.

    Returns a bool.
    """
    num, letter_with_colon, password = inputline.split()
    letter = letter_with_colon.rstrip(":")
    minnum=num.split("-")[0]
    maxnum=num.split("-")[1]

    num_occurances = password.count(letter)
    if int(minnum) <= num_occurances <= int(maxnum):
        return True
    return False

def ismorevalidpw(inputline):
    """
    Tests if a password conforms to a given set of rules.
    input is of the form:

    15-16 l: ksadfsadfsadfsadfll

    Which means:
    15-16:                  location 15 or 16 must contain the letter
                            in the password, but not both.
    l                       letter that must be in the password
    ksadfsadfsadfsadfll:    the password to be checked.

    Returns a bool.
    """
    num, letter_with_colon, password = inputline.split()
    letter = letter_with_colon.rstrip(":")
    minnum=num.split("-")[0]
    maxnum=num.split("-")[1]

    if password[int(minnum)-1] == letter and password[int(maxnum)-1] == letter:
        return False
    if letter in (password[int(minnum) - 1], password[int(maxnum) - 1]):
        return True
    return False


def day02_01():
    """Run part 1 of Day 2's code"""
    path = "./input/02/input.txt"
    result=0
    for line in file_to_str_array(path):
        if isvalidpw(line):
            result+=1
    print(f'0201: Number of Valid Passwords: {result}')


def day02_02():
    """Run part 2 of Day 2's code"""
    path = "./input/02/input.txt"
    result=0
    for line in file_to_str_array(path):
        if ismorevalidpw(line):
            result+=1
    print(f'0202: Number of Valid Passwords: {result}')


if __name__ == "__main__":
    day02_01()
    day02_02()

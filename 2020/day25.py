"""
AOC day 25 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def transform(subject_num: int, loop_size=1, value=1)-> int:
    '''
    Perform the card/door transform loop_size times
    '''
    # A number of times called the loop_size:
    for _ in range(loop_size):
        # Set the value to itself multiplied by the subject number
        value = value * subject_num
        # Set the value to the remainder after dividing by 20201227
        value = value % 20201227
    return  value

def find_loop_size(subject_num, public_key):
    '''
    Determine the loopsize given a public_key and a subject num
    '''
    value=1
    loop=0
    while value != public_key:
        loop+=1
        # perform one loop of the transform and check the value.
        value = transform(subject_num, loop_size=1, value=value)
    return loop

def day25_01():
    """Run part 1 of Day 25's code"""
    card_public_key=1965712
    door_public_key=19072108
    card_loop_size=find_loop_size(7,card_public_key)
    result=transform(door_public_key,loop_size=card_loop_size)

    print(f'2501: Encryption key is: {result}')

def day25_02():
    """Run part 2 of Day 25's code"""
    path = "./input/25/input.txt"
    result=""
    print(f'2502: {result}')

if __name__ == "__main__":
    day25_01()
    #day25_02()

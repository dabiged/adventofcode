"""
AOC day 10 2018
"""
from collections import defaultdict, deque
from itertools import combinations
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def jolt_diff_dist(adapterjolts):
    '''
    Get the distribution of the difference in jolts.
    Return the product of the number of differences of
    1 and the number of differences by 3.
    '''
    # initialise the list with the charging outlet value
    sortedjolts=[0]
    # Read in the jolts and sort them
    for jolt in adapterjolts:
        sortedjolts.append(int(jolt))
    sortedjolts.sort()

    jolt_diffs=defaultdict(int)
    for num, adapter_val in enumerate(sortedjolts):
        if num ==0 :
            # Skip the charging port to avoid OutOfBounds exception
            pass
        jolt_diffs[adapter_val - sortedjolts[num-1]] +=1
    # the last difference between the last adaptor and our laptop is always 3.
    jolt_diffs[3]+=1
    return jolt_diffs[1]*jolt_diffs[3]

def number_combinations(adapterjolts):
    '''Find the number of different ways we can use out collection of adapters
    to bridge from the charging port to our laptop '''
    # initialise the list with the charging outlet value
    sortedjolts=[0]
    for jolt in adapterjolts:
        sortedjolts.append(int(jolt))
    sortedjolts.sort()
    # Add the laptop jolt value.
    sortedjolts.append(sortedjolts[-1]+3)

    # This next bit is a bit complicated.
    # 1. Read in the list of all adapters.
    # 2. look for any consequetive adapters that differ by exactly 3.
    # 3. then split the task into chunks.
    # i.e.:
    # [0, 1, 2, 3, 6, 7, 8, 9]
    # becomes:
    # [0, 1, 2, 3] and [6,7,8,9]
    # 4. Then calculate the number of combinations of each sublist and multiply them.
    queue = deque()
    thissequence=[]
    for i, _ in enumerate(sortedjolts):
        if i == 0:
            #skip the first entry (difference of charger is invalid)
            pass
        if (sortedjolts[i] - sortedjolts[i-1]) < 3:
            # add sequence to the queue.
            thissequence.append(sortedjolts[i])
        elif (sortedjolts[i] - sortedjolts[i-1]) == 3:
            thissequence.append(sortedjolts[i])
            queue.append(thissequence)
            # Note, this jolt goes at the beginning of the next sequence.
            thissequence=[sortedjolts[i]]
        else:
            print("Something went wrong")

    numbercombs=1
    while len(queue)>0:
        sequence = queue.pop()
        # The default number of ways this sequence of adapters can bridge the divide.
        this_seq_comb=1
        for comb_length in range(2,len(sequence)):
            for comb in combinations(sequence,comb_length):
                if sequence[0] == min(comb) and sequence[-1] == max(comb):
                    diff_list = []
                    for jolt_at_n, jolt_at_n_plus_1 in zip(comb[0::], comb[1::]):
                        # Create a list of all the difference of adjacent
                        #   adaptors in this sequence.
                        diff_list.append(jolt_at_n_plus_1-jolt_at_n)
                    if max(diff_list)<=3:
                        # If this combinations adacent difference are less than 3
                        # it is a valid combination
                        this_seq_comb+=1
        # Update the total number of combinations by multiplying by the number
        # of combinations in this sequence.
        numbercombs*=this_seq_comb
    return numbercombs


def day10_01():
    """Run part 1 of Day 10's code"""
    path = "./input/10/input.txt"
    result = jolt_diff_dist(file_to_str_array(path))
    print(f'1001: The product of 1 and 3 adapter differences is: {result}')

def day10_02():
    """Run part 2 of Day 10's code"""
    path = "./input/10/input.txt"
    result = number_combinations(file_to_str_array(path))
    print(f'1002: The number of different ways we can power our laptop is: {result}')

if __name__ == "__main__":
    day10_01()
    day10_02()

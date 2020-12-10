"""
AOC day 10 2018
"""
from collections import defaultdict
from itertools import combinations
from collections import deque
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def jolt_diff_dist(adapterjolts):
    # initialise the list with the charding outlet value
    sortedjolts=[0]
    for jolt in adapterjolts:
        sortedjolts.append(int(jolt))
    sortedjolts.sort()
    print(sortedjolts)


    jolt_diffs=defaultdict(int)
    for num, adapter_val in enumerate(sortedjolts):
        if num ==0 :
            pass
        jolt_diffs[adapter_val - sortedjolts[num-1]] +=1
    
    # the last difference between the last adaptor and out laptop
    jolt_diffs[3]+=1

    return jolt_diffs[1]*jolt_diffs[3]

def number_combinations(adapterjolts):
    # initialise the list with the charding outlet value
    sortedjolts=[0]
    for jolt in adapterjolts:
        sortedjolts.append(int(jolt))
    sortedjolts.sort()
    # Add the difference to the laptop
    sortedjolts.append(sortedjolts[-1]+3)
    print(sortedjolts)

    # Read in the list of all adapters.
    # look for any consequetive adapters that differ by exactly 3.
    # then split the task into chunks.
    # i.e.:
    # [0, 1, 2, 3, 6, 7, 8, 9]
    # becomes:
    # [0, 1, 2, 3] and [6,7,8,9]
    # Then calculate the number of combinations of each sublist and multiply them.
    queue = deque()
    thissequence=[]
    for i, jolts in enumerate(sortedjolts):
        if i == 0:
            #skip the first entry
            pass
        if (sortedjolts[i] - sortedjolts[i-1]) < 3:
            thissequence.append(sortedjolts[i])
        elif (sortedjolts[i] - sortedjolts[i-1]) == 3:
            thissequence.append(sortedjolts[i])
            queue.append(thissequence)
            thissequence=[sortedjolts[i]]
        else:
           print("Something went wrong")

    numbercombs=1
    while len(queue)>0:
        sequence = queue.pop()
        this_seq_comb=1
        for comb_length in range(2,len(sequence)):
            for comb in combinations(sequence,comb_length):
                if sequence[0] == min(comb) and sequence[-1] == max(comb):
                    diff_list = [] 
                    for x, y in zip(comb[0::], comb[1::]): 
                        diff_list.append(y-x)  
                    if max(diff_list)<=3:
                        this_seq_comb+=1
        numbercombs*=this_seq_comb
    return numbercombs


def day10_01():
    """Run part 1 of Day 10's code"""
    path = "./input/10/input.txt"
    result = jolt_diff_dist(file_to_str_array(path))
    print(f'1001: {result}')

def day10_02():
    """Run part 2 of Day 10's code"""
    path = "./input/10/input.txt"
    result = number_combinations(file_to_str_array(path))
    print(f'1002: {result}')

if __name__ == "__main__":
    day10_01()
    day10_02()

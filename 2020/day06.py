"""
AOC day 06 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def count_uniq_questions(inputdata):
    """
    returns the sum of all uniq questions answered by anyone in each group.
    """
    size=0
    thisq=set()
    for questions in inputdata:
        if questions == '':
            size+=len(set(thisq))
            thisq=set()
        for char in questions:
            thisq.add(char)
    return size

def count_all_answered_questions(inputdata):
    '''
    Returns the sum of all unique questions answered by everyone in each group

    Info:
    1. buil a dict of each persons answered question (a dict of sets)
    2. Calculate all questions answered by this group (union of all individual answers)
    3. count the number of questions answered by everyone in the group
    4. return the sum of these.
    '''

    count_of_all_answered=0
    qs_answered_in_this_group={}
    personid=0
    # loop through the questions answered.
    for questions in inputdata:
        if questions == '':
            # when we get to a blank line find all the questioned asnwered.
            all_groups_qs=set()
            for individual_qs in qs_answered_in_this_group.values():
                # All questions answered by all members of this group
                all_groups_qs= all_groups_qs.union(individual_qs)
            for char in all_groups_qs:
                # for the charaters answer by all persons in this group
                # if all the individuals answered this question
                if all([char in indiv for indiv in qs_answered_in_this_group.values()]):
                    # increase count by one.
                    count_of_all_answered+=1
            personid=0
            qs_answered_in_this_group={}

        # For each character in each line record the questions on this line.
        else:
            if personid not in qs_answered_in_this_group.keys():
                qs_answered_in_this_group[personid]=set()
            for char in questions:
                qs_answered_in_this_group[personid].add(char)
            personid+=1
    return count_of_all_answered

def day06_01():
    """Run part 1 of Day 06's code"""
    path = "./input/06/input.txt"
    result = count_uniq_questions(file_to_str_array(path))
    print(f'0601: the Sum of questions answer is: {result}')

def day06_02():
    """Run part 2 of Day 06's code"""
    path = "./input/06/input.txt"
    result = count_all_answered_questions(file_to_str_array(path))
    print(f'0602: Sum of questions answered by all in the group:{result}')

if __name__ == "__main__":
    day06_01()
    day06_02()

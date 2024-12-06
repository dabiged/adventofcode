from lib.filehelper import file_to_str_array
from collections import defaultdict
from functools import cmp_to_key
# pylint: disable=missing-module-docstring

testdata='''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

global allrules
allrules=defaultdict(list)

def parse(ipt):
    rules=[]
    updates=[]
    for row in ipt:
        if '|' in row:
            rules.append(row)
        elif ',' in row:
            updates.append(row)
        elif row == '':
            pass
        else:
            raise ValueError
    return rules, updates

def cmp_updates(a,b):
    # A custom sort function:
    # return 1 if a goes before b
    # return 0 if you dont care about the order
    # return -1 if b goes before a
    if b in allrules[a]:
        return -1
    elif a in allrules[b]:
        return 1
    else:
        return 0

def run(inputdata=testdata.split('\n')):
    rules, updates = parse(inputdata)
    # build rules
    for rule in rules:
        a=int(rule.split('|')[0])
        b=int(rule.split('|')[1])
        allrules[a].append(b)

    score1,score2=0,0
    for update in updates:
        nums=list(map(int,update.split(',')))
        # Sort the list using our custom function
        sorted_nums=sorted(nums,key=cmp_to_key(cmp_updates))
        if nums == sorted_nums:
            score1+=int(nums[len(nums)//2])
        else:
            score2+=int(sorted_nums[len(sorted_nums)//2])

    return score1,score2

def day05_01():
    """Run part 1 of Day 05's code"""
    path = "./input/05.txt"
    a,b=run(file_to_str_array(path))
    print("0501:", a)
    print("0502:", b)

if __name__ == "__main__":
    day05_01()

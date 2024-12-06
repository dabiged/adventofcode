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

global postrules
global prerules
prerules=defaultdict(set)
postrules=defaultdict(set)

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

def str_2_strarray(string):
    return string.split('\n')

def isValid(update,prerules,postrules):
    for i, num in enumerate(update):
        #print(update, num)
        if len(postrules[num]) >0:
            for notallowedafter in postrules[num]:
                if notallowedafter in update[i:]:
                    #print(notallowedafter, 'occurs after', num,' inviolation of',prerules[num])
                    return False
        if len(prerules[num]) >0:
            for notallowedbefore in prerules[num]:
                if notallowedbefore in update[:i]:
                    #print(notallowedafter, 'occurs after', num,' inviolation of',prerules[num])
                    return False

    return True


def part1(inputdata=str_2_strarray(testdata)):
    rules, updates = parse(inputdata)
    prerules=defaultdict(set)
    postrules=defaultdict(set)
    for rule in rules:
        a=rule.split('|')[0]
        b=rule.split('|')[1]
        prerules[a].add(b)
        postrules[b].add(a)
    score=0
    for update in updates:
        update=update.split(',')
        if isValid(update,prerules,postrules):
            score+=int(update[len(update)//2])
    return score


def cmp_updates(a,b):
    # A custom sort function:
    # return 1 if a goes before b
    # return 0 if you dont care about the order
    # return -1 if b goes before a
    if b in prerules[a]:
        return -1
    elif b in postrules[a]:
        return 1
    else:
        return 0

def part2(inputdata=str_2_strarray(testdata)):
    rules, updates = parse(inputdata)
    for rule in rules:
        a=rule.split('|')[0]
        b=rule.split('|')[1]
        prerules[a].add(b)
        postrules[b].add(a)
    score=0
    for update in updates:
        update=update.split(',')
        if not isValid(update,prerules,postrules):
            print(update)
            update.sort(key=cmp_to_key(cmp_updates))
            print(update)
            score+=int(update[len(update)//2])
    return score



def day05_01():
    """Run part 1 of Day 05's code"""
    path = "./input/05.txt"
    print("0501:", part1(file_to_str_array(path)))


def day05_02():
    """Run part 2 of Day 05's code"""
    path = "./input/05.txt"
    print("0502:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    #print(part1())
    day05_01()
    print(part2())
    day05_02()

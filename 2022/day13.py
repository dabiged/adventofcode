from lib.filehelper import get_bald_string_list_from_file
# pylint: disable=missing-module-docstring

import json

test_data='''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

def parse(inputtext):
    print(inputtext)
    for group in inputtext.split('\n\n'):
        a,b = group.splitlines()
        a = json.loads(a)
        b = json.loads(b)
        yield a,b

def compare(a,b):
    alen=len(a)
    blen=len(b)

    for i in range(min(alen,blen)):
        aitem=a[i]
        bitem=b[i]
        if isinstance(aitem,int) and isinstance(bitem,int):
            if aitem < bitem:
                return True
            if aitem > bitem:
                return False
            continue
        if isinstance(aitem,list) and isinstance(bitem,list):
            subanswer = compare(aitem,bitem)
            if subanswer is not None:
                return subanswer
            continue
        if isinstance(aitem,int):
            aitem=[aitem]
        elif isinstance(bitem,int):
            bitem=[bitem]
        else:
            raise ValueError
        subanswer=compare(aitem,bitem)
        if subanswer is not None:
            return subanswer

    if alen<blen:
        return True

    if alen>blen:
        return False


def main1(input_data):
    data = list(parse(input_data))
    count=0
    for i,(a,b) in enumerate(data,start=1):
        if compare(a,b):
            count+=i
    return count


class Chain():
    def __init__(self,item):
        self.item = item
    def __lt__ (self,other):
        return compare(self.item,other.item)
    def __repr__(self):
        return str(self.item)


def main2(data):
    chains=[]
    for a,b in parse(data):
        chains.append(Chain(a))
        chains.append(Chain(b))
    chains.append(Chain([[6]]))
    chains.append(Chain([[2]]))

    chains=sorted(chains)
    ans=1
    for i,chain in enumerate(chains,start=1):
        if chain.item == [[6]] or chain.item == [[2]]:
            ans*=i

    return ans


def day13_01():
    """Run part 1 of Day 13's code"""
    path = "./input/input_13.txt"
    #print("1301:",main1("".join(get_bald_string_list_from_file(path))))

def day13_02():
    """Run part 2 of Day 13's code"""
    path = "./input/input_13.txt"
    print("1302:",main2("".join(get_bald_string_list_from_file(path))))

if __name__ == "__main__":
    day13_01()
    day13_02()


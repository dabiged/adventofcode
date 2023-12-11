from lib.filehelper import file_to_str_array, get_bald_string_list_from_file
# pylint: disable=missing-module-docstring
import itertools
from collections import defaultdict
import functools 

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
def lcm(a,b):
    return a*b // gcd(a,b)



test_input='''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

test_input1='''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

test_input2='''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''


class Node():
    def __init__(self,data):
        self.data=data
        self.parse()

    def parse(self):
        tmp=self.data.split(' = ')
        self.name=tmp[0]
        self.L=tmp[1][1:-1].split(', ')[0]
        self.R=tmp[1][1:-1].split(', ')[1]

class Network():
    def __init__(self,data):
        self.data=data
        self.steps=self.data.split('\n\n')[0]
        self.nodes=self.data.split('\n\n')[1]
        self.map={}
        self.parse_nodes()
        self.num_steps=0

    def parse_nodes(self):
        for node in self.nodes.split('\n'):
            thisnode=Node(node)
            self.map[thisnode.name]=thisnode

    def walk(self):
        loc='AAA'
        for step in itertools.cycle(self.steps):
            if loc == 'ZZZ':
                break
            self.num_steps+=1
            if step == 'L':
                newloc=self.map[loc].L
            elif step == 'R':
                newloc=self.map[loc].R
            #print('Step:',num_steps,'At', loc, 'Instr:',step,'moving to:',newloc)
            loc=newloc
        return self.num_steps

    def walk_one(self,loc,step):
        self.num_steps+=1
        if step == 'L':
            newloc=self.map[loc].L
        elif step == 'R':
            newloc=self.map[loc].R
        loc=newloc
        return newloc


def part1(inputdata=test_input1):
    mynet=Network(inputdata)
    return mynet.walk()

def part2(inputdata=test_input2):
    num_step=0
    mynet=Network(inputdata)
    currlocs=[loc for loc in mynet.map.keys() if loc[-1] == 'A']

    startstep={}
    for step in itertools.cycle(mynet.steps):
        if any([a[-1] == 'Z' for a in currlocs]):
            print(num_step,startstep)
            print(len(startstep.keys()))
            for i,loc in enumerate(currlocs):
                if 'Z' in loc:
                    startstep[num_step]=loc

                    if len(startstep.keys()) == len(currlocs):
                        print(startstep)
                        return functools.reduce(lambda x, y: lcm(x, y),startstep.keys())
        newlocs=[]
        if all([A[-1]=='Z' for A in currlocs]):
            break
        num_step +=1
        for loc in currlocs:
            newlocs.append(mynet.walk_one(loc,step))
        currlocs=newlocs

    return num_step


def day08_01():
    """Run part 1 of Day 7's code"""
    path = "./input/08.txt"
    #print("0801:", part1('\n'.join(get_bald_string_list_from_file(path))))


def day08_02():
    """Run part 2 of Day 1's code"""
    #print(part2())
    path = "./input/08.txt"
    print("0802:", part2('\n'.join(get_bald_string_list_from_file(path))))

if __name__ == "__main__":
    #day08_01()
    day08_02()

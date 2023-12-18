from lib.filehelper import get_string_lists_from_file, get_map_from_file, file_to_str_array
# pylint: disable=missing-module-docstring
import itertools
from collections import defaultdict
import re

test_input=['rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7']



def ascii_hash(inputstr):
    output=0
    for char in inputstr:
        output+=ord(char)
        output*=17
        output%=256
    return output

class Box():
    def __init__(self,num):
        self.contents=[]
        self.num=num

    def instruction(self,instruction):
        if '-' not in instruction:
            location,value=instruction.split('=')[0],instruction.split('=')[1]
            for i, item in enumerate(self.contents):
                loc,val=item
                if loc == location:
                    removed_ = self.contents.pop(i)
                    self.contents.insert(i,(location,value))
                    return
            self.contents.append((location,value))
        else:
            location=instruction.split('-')[0]
            for i,item in enumerate(self.contents):
                loc,val=item
                if loc == location:
                    removed_ = self.contents.pop(i)

    def __str__(self):
        return 'Box '+str(self.num)+': '+" ".join([str(i) for i in self.contents])


class Boxes():
    def __init__(self,instructions):
        self.instructions=instructions
        self.map={}

    def run(self):
        for instr in self.instructions:
            location=re.split('[-=]',instr)[0]
            if ascii_hash(location) not in self.map.keys():
                self.map[ascii_hash(location)]=Box(ascii_hash(location))
            self.map[ascii_hash(location)].instruction(instr)

    def score(self):
        total=0
        for k,v in self.map.items():
            multiplier=k+1
            for i,item in enumerate(v.contents):
                total+=multiplier*((i+1)*int(item[1]))
        return total

    def __str__(self):
        output=''
        for loc in self.map.keys():
            output+=str(self.map[loc])+'\n'
        return output

def part1(inputdata=test_input):
    total=0
    for inputstr in inputdata:
        for sentence in inputstr.split(','):
            total+=ascii_hash(sentence)

    return total

def part2(inputdata=test_input):
    instructions=inputdata[0].split(',')

    boxes=Boxes(instructions)
    boxes.run()
    return boxes.score()



def day15_01():
    """Run part 1 of Day 7's code"""
    path = "./input/15.txt"
    print("1501:", part1(file_to_str_array(path)))


def day15_02():
    """Run part 2 of Day 1's code"""
    path = "./input/15.txt"
    #print(part2())
    print("1502:", part2(file_to_str_array(path)))


if __name__ == "__main__":
    day15_01()
    day15_02()

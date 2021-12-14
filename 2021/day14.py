"""
AOC day 14 2018
"""
from lib.filehelper import file_to_str_array
from collections import Counter, defaultdict
from copy import deepcopy
# pylint: disable=missing-module-docstring

class Polymer():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.rules=defaultdict(str)
        self.polymer=[]
        # A count of the number of each pair
        self.pairs=defaultdict(int)
        # a count of the individual letters
        self.count=defaultdict(int)

        self.processinputfile()

        for B,A in zip(self.polymer[1:],self.polymer[:-1]):
            self.pairs[A+B]+=1

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)
        for i,line in enumerate(self.input):
            if i ==0 :
                self.polymer=[i for i in line]
            elif i ==1:
                pass
            else:
                rule=line.split(' -> ')
                self.rules[rule[0]]=rule[1]

    def step(self):
        oldpairs=deepcopy(self.pairs)
        for pair,insert in self.rules.items():
            newpair1=pair[0]+insert
            newpair2=insert+pair[1]
            count=oldpairs[pair]
            self.pairs[pair]-=count
            self.pairs[newpair1]+=count
            self.pairs[newpair2]+=count

    def process(self,steps=1):
        for i in range(steps):
            self.step()
        return None

    def countletters(self):
        self.count[self.polymer[0]]+=1
        self.count[self.polymer[-1]]+=1
        for pair,count in self.pairs.items():
            self.count[pair[0]]+=count
            self.count[pair[1]]+=count
        return {k:int(v/2) for k,v in self.count.items()}


    def part1(self):
        self.process(10)
        data=Counter(self.countletters())
        return data.most_common()[0][1]-data.most_common()[-1][1]

    def part2(self):
        self.process(40)
        data=Counter(self.countletters())
        return data.most_common()[0][1]-data.most_common()[-1][1]



def day14_01():
    """Run part 1 of Day 14's code"""
    inputfile='input/day14.txt'
    testPolymer=Polymer(inputfile)
    result=testPolymer.part1()
    print(f'1401: {result} ')

def day14_02():
    """Run part 2 of Day 14's code"""
    inputfile='input/day14.txt'
    testPolymer=Polymer(inputfile)
    result=testPolymer.part2()
    print(f'1402: {result}')

if __name__ == "__main__":
    day14_01()
    day14_02()

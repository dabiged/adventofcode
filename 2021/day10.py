"""
AOC day 10 2018
"""
from lib.filehelper import file_to_str_array
from copy import deepcopy
# pylint: disable=missing-module-docstring

class FixLine():
    def __init__(self,inputstr):
        self.inputstr=inputstr
        self.activest=deepcopy(self.inputstr)
        self.score={')':3, ']':57,'}':1197,'>':25137}

    def run_part1(self):
        self.process()
        if not self.isIncomplete():
            for i,char in enumerate(self.activest):
                if char in (')','}',']','>'):
                    return self.score[self.activest[i]]
        return 0

    def run_part2(self):
        self.process()
        if self.isIncomplete():
            return self.activest


    def process(self):
        changed=True
        while changed:
            oldval=deepcopy(self.activest)
            self.activest=self.activest.replace('()','')
            self.activest=self.activest.replace('{}','')
            self.activest=self.activest.replace('[]','')
            self.activest=self.activest.replace('<>','')
            if len(self.activest) == len(oldval):
                changed=False
        return None

    def count(self):
        self.starters=0
        self.enders=0
        for char in self.activest:
            if char in ('(','{','[','<'):
                self.starters+=1
            if char in (')','}',']','>'):
                self.enders+=1
        return None

    def isIncomplete(self):
        self.count()
        if self.starters == 0 or self.enders ==0:
            return True
        return False


class SyntaxFixer():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.processinputfile()
        self.part2score={'(':1,'[':2,'{':3,'<':4}

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)

    def part1(self):
        score=0
        for line in self.input:
            thisline=FixLine(line)
            score+=thisline.run_part1()
        return score
    def part2(self):
        scores=[]
        for line in self.input:
            thisline=FixLine(line)
            unmatched=thisline.run_part2()
            if unmatched:
                thisscore=0
                for i in unmatched[::-1]:
                    thisscore*=5
                    thisscore+=self.part2score[i]
                scores.append(thisscore)
        scores=sorted(scores)
        return scores[len(scores)//2 ]




def day10_01():
    """Run part 1 of Day 10's code"""
    inputfile='./input/day10.txt'
    testfixer=SyntaxFixer(inputfile)
    result=testfixer.part1()
    print(f'1001: {result} is the total syntax score')

def day10_02():
    """Run part 2 of Day 10's code"""
    inputfile='./input/day10.txt'
    testfixer=SyntaxFixer(inputfile)
    result=testfixer.part2()
    print(f'1002: {result} is the middle score')

if __name__ == "__main__":
    day10_01()
    day10_02()

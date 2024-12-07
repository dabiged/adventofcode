from lib.filehelper import file_to_str_array
import itertools
from collections import deque
# pylint: disable=missing-module-docstring

testdata='''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

def SUB(a,b):
    return a-b

def ADD(a,b):
    return a+b

def MULT(a,b):
    return a*b

def CONCAT(a,b):
    return int(str(a)+str(b))


class Equation:
    def __init__(self,equation_text,operations):
        self.operations=operations
        self.targetvalue = int(equation_text.split(':')[0])
        self.numbers=list(map(int,equation_text.split()[1:]))
        self.combos=[]

    def make_combinations(self,length,operations):
        # return all possible combinations of operations
        a=deque()
        a.append(())
        while a:
            base=a.pop()
            for op in operations:
                if len(base) == length:
                    self.combos.append(base)
                else:
                    a.append(base+(op,))

    def short_check(self):
        for ops in [self.operations[:-1],self.operations]:
            num=self.total(ops)
            if num >0:
                return num
        return 0


    def total(self,operations):
        #determine if some combination of operations equals the total
        self.make_combinations(len(self.numbers),operations)
        for sequence in  self.combos:
            total=self.numbers[0]
            for op,number in zip(sequence,self.numbers[1:]):
                total=op(total,number)
            if total == self.targetvalue:
                return total
        return 0



def part1(inputdata=testdata.split('\n')):
    total=0
    for line in inputdata:
        myeq=Equation(line,[MULT,ADD])
        total+=myeq.total()
    return total

def part2(inputdata=testdata.split('\n')):
    total=0
    for line in inputdata:
        myeq=Equation(line,[MULT,ADD,CONCAT])
        total+=myeq.total(myeq.operations)
        print(total)
    return total

def part3(inputdata=testdata.split('\n')):
    total=0
    for line in inputdata:
        myeq=Equation(line,[MULT,ADD,CONCAT])
        total+=myeq.short_check()
        print(total)
    return total




def day07_01():
    """Run part 1 of Day 07's code"""
    path = "./input/07.txt"
    print("0701:", part1(file_to_str_array(path)))


def day07_02():
    """Run part 2 of Day 07's code"""
    path = "./input/07.txt"
    print("0702:", part3(file_to_str_array(path)))

if __name__ == "__main__":
    day07_01()
    day07_02()

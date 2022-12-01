"""
AOC day 02 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class IntCodeComputer():
    def __init__(self,inputfile,debug=False):
        self.program=self.readinputfile(inputfile)
        self.position=0
        self.finished=False
        self.debug=debug
        self.restore()
        self.run()

    def restore(self):
        self.program[1]=12
        self.program[2]=2

    def readinputfile(self,inputfile):
        with open(inputfile) as f:
            program=f.readline()
        return [int(i) for i in program.split(',')]

    def add(self):
        adder1=self.program[self.program[self.position]]
        self.position+=1
        adder2=self.program[self.program[self.position]]
        self.position+=1
        outputlocation=self.program[self.position]
        self.position+=1
        self.program[outputlocation]=adder1+adder2

    def multiply(self):
        mult1=self.program[self.program[self.position]]
        self.position+=1
        mult2=self.program[self.program[self.position]]
        self.position+=1
        outputlocation=self.program[self.position]
        self.position+=1
        self.program[outputlocation]=mult1*mult2

    def save(self,value):
        saveposition=self.program[self.position]
        self.position+=1
        self.program[saveposition]=value

    def output(self):
        outputval=self.program[self.position]
        self.position+=1
        print(outputval)

    def halt(self):
        self.finished=True

    def step(self):
        print(self.position)
        action=self.program[self.position]
        self.position+=1
        if action==1:
            self.add()
        elif action ==2:
            self.multiply()
        elif action == 99:
            self.halt()

    def result(self):
        return self.program[0]

    def run(self):
        if self.debug:
            print(self.program)
        while not self.finished:
            if self.debug:
                print(self.program)
            self.step()



def day02_01():
    """Run part 1 of Day 02's code"""
    inputfile = "./input/day02_input.txt"
    myIntcode=IntCodeComputer(inputfile,debug=True)
    result=myIntcode.result()
    print(f'0201: {result}')

def day02_02():
    """Run part 2 of Day 02's code"""
    path = "./input/02/input.txt"
    result=""
    print(f'0202: {result}')

if __name__ == "__main__":
    day02_01()
    #day02_02()

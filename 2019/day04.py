"""
AOC day 02 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class IntCodeComputer():
    numparams={1:3,2:3,3:1,4:1,99:0}
    def __init__(self,inputfile,debug=False):
        self.program=self.readinputfile(inputfile)
        self.position=0
        self.finished=False
        self.debug=debug

    def readinputfile(self,inputfile):
        with open(inputfile) as f:
            program=f.readline()
        return [int(i) for i in program.split(',')]

    def add(self,instructions):
        ''' mode is a zero padded str of len 3 '''
        mode=str(instructions).zfill(5)
        if mode[0] == '0':
            adder1=self.program[self.program[instructions[1]]]
        elif mode[0] == '1':
            adder1=self.program[instructions[1]]
        if mode[1] == '0':
            adder2=self.program[self.program[instructions[2]]]
        elif mode[1] == '1':
            adder2=self.program[instructions[2]]
        if mode[2] == '0':
            outputlocation=self.program[self.program[instructions[3]]]
        elif mode[2] == '1':
            outputlocation=self.program[instructions[3]]
        self.program[outputlocation]=adder1+adder2

    def multiply(self,instructions):
        mode=str(instructions[0]).zfill(5)
        if mode[0] == '0':
            mult1=self.program[instructions[1]]
        elif mode[0] == '1':
            mult1=instructions[1]
        if mode[1] == '0':
            mult2=self.program[instructions[2]]
        elif mode[1] == '1':
            mult2=instructions[2]
        if mode[2] == '0':
            outputlocation=instructions[3]
        elif mode[2] == '1':
            raise Exception('Parameters that an instruction writes will never be in immediate mode')
        self.program[outputlocation]=mult1*mult2

    def save(self):
        saveposition=self.program[self.position]
        self.position+=1
        value=input("input value:")
        self.program[saveposition]=value

    def output(self):
        outputval=self.program[self.position]
        self.position+=1
        print(outputval)

    def halt(self,action):
        self.finished=True

    def step(self):
        print(self.position)
        opcode=self.program[self.position]
        # tens and ones column of opcode
        baseopcode=opcode%100
        action=self.program[self.position:self.position+self.numparams[baseopcode]+1]
        if baseopcode==1:
            self.add(action)
        elif baseopcode==2:
            self.multiply(action)
        elif baseopcode== 3:
            self.save(action)
        elif baseopcode== 99:
            self.halt(action)
        self.position+=self.numparams[baseopcode]

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

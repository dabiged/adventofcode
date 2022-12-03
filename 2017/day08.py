from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from collections import defaultdict

class UnknownOperatorError(Exception):
    pass
class UnknownRegisterAlter(Exception):
    pass

class Computer():
    def __init__(self,program):
        self.program=program
        self.registers=defaultdict(int)

    def evaluate_conditional(self,register,operator,value):
        if   operator == '>':
            return self.registers[register] > value
        elif operator == '<':
            return self.registers[register] < value
        elif operator == '==':
            return self.registers[register] == value
        elif operator == '!=':
            return self.registers[register] != value
        elif operator == '>=':
            return self.registers[register] >= value
        elif operator == '<=':
            return self.registers[register] <= value
        else:
            raise UnknownOperatorError(operator)


    def change_register(self,register, incdec, value):
        if incdec == 'inc':
            self.registers[register] += value
        elif incdec == 'dec':
            self.registers[register] += -value
        else:
            raise UnknownRegisterAlter(incdec)

    def step(self,instr):
        register_change, conditional = instr.split(' if ')
        reg=register_change.split()
        cond=conditional.split()
        register, incdec, regchange = reg[0], reg[1], reg[2]
        checkreg, operator, value = cond[0], cond[1], cond[2]

        if self.evaluate_conditional(checkreg,operator,int(value)):
            self.change_register(register,incdec,int(regchange))

    def run(self):
        currmax=-9999999999
        for instr in self.program:
            self.step(instr)
            if max(self.registers.values()) > currmax:
                currmax=max(self.registers.values())
        return max(self.registers.values()), currmax




def day08_01():
    """Run part 1 of Day 8's code"""
    path = "./input/input_08.txt"
    myProgram=Computer(file_to_str_array(path))
    print('0801:', myProgram.run()[0])



def day08_02():
    """Run part 2 of Day 8's code"""
    path = "./input/input_08.txt"
    myProgram=Computer(file_to_str_array(path))
    print('0802:', myProgram.run()[1])


if __name__ == "__main__":
    day08_01()
    day08_02()

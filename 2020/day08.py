"""
AOC day 08 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class VMInstrNotFound(Exception):
    """Exception in case bootcode instruction is not found"""

class VMPositionOutOfBounds(Exception):
    """Exception for position going out of bound of program"""

class BootCode:
    """An assembler like computer for executing small programs"""
    def __init__(self,inputbootcode, accumulator=0, position=0):
        """ initialise the boot code, by reading the program line by line
        We store the program in a dict, with:
        key = position in the program  from 0 to len(self.bootcode)
        value = list of str. """
        # The global accumulator value.
        self.accumulator=accumulator
        # The current position in the program
        self.position=position
        # The program to run.
        self.bootcode={}
        # A history of all instructions run.
        # useful for debugging
        self.history=[]

        for counter, line in enumerate(inputbootcode):
            self.bootcode[counter]=line.split()

    def step(self, verbose=False):
        """ Step the bootcode once, by reading the instruction at the current position
        and changing the accumulator or position"""
        self.history.append(self.bootcode[self.position])
        if verbose:
            print("Position:",self.position,"Accumulator:",self.accumulator)
            print("Current Instr:", self.bootcode[self.position])
        if   self.bootcode[self.position][0] == 'nop':
            # nop = No Operation and ignore the value given.
            self.position +=1
        elif self.bootcode[self.position][0] == 'acc':
            # acc = Add to the global accumulator value by the value given.
            self.accumulator+=int(self.bootcode[self.position][1])
            self.position +=1
        elif self.bootcode[self.position][0] == 'jmp':
            # jmp = change the position up/down by the number given
            self.position +=int(self.bootcode[self.position][1])

        else:
            # A catchall Exception raised if the instruction is not recognised.
            raise VMInstrNotFound("The Instruction", self.bootcode[self.position][0], \
            "at location", self.position, "is not Valid")

        if  self.position < 0  or self.position > len(self.bootcode):
            # Another exception to check if the position has moved outside the program.
            raise VMPositionOutOfBounds("Position", self.position," is out of bounds")

        return self.accumulator, self.position

    def run(self, accumulator=0, position=0, verbose=False):
        """Loop over the program calling the step method repeatedly to run it"""
        self.accumulator=accumulator
        self.position=position
        # A list of past positions.
        positions_seen = []
        finished=False
        while not finished:
            # Add current position to list of positions visited.
            positions_seen.append(self.position)
            # Step the program
            accum, position = self.step(verbose=verbose)
            if verbose:
                print(position, positions_seen)
            # Check to see if the program has finished.
            if self.position in positions_seen:
                if verbose:
                    print("cyclical behaviour detected")
                finished=True
            if self.position==len(self.bootcode):
                finished=True

        return accum
def day08_01():
    """Run part 1 of Day 08's code"""
    path = "./input/08/input.txt"
    mybootcode=BootCode(file_to_str_array(path))
    result=mybootcode.run()
    print(f'0801: Accumulator value on looping: {result}')

def day08_02():
    """Run part 2 of Day 08's code"""
    path = "./input/08/input.txt"
    mybootcode=BootCode(file_to_str_array(path))
    for position, instr in mybootcode.bootcode.items():
        # Pretty sure tehre is a way to merge these two if statements???
        if instr[0] == 'nop':
            # Make a copy of the old program entry
            oldline = mybootcode.bootcode[position].copy()
            # Change the current instruction
            mybootcode.bootcode[position][0]='jmp'
            # Run it!
            result=mybootcode.run()
            if mybootcode.position==len(mybootcode.bootcode):
                # if we reached the end of program we have a result.
                print(f'0802: Accumulator value at end of run: {result}')
            mybootcode.bootcode[position]=oldline
        if instr[0] == 'jmp':
            oldline = mybootcode.bootcode[position].copy()
            mybootcode.bootcode[position][0]='nop'
            result=mybootcode.run()
            if mybootcode.position==len(mybootcode.bootcode):
                print(f'0802: Accumulator value at end of run: {result}')
            mybootcode.bootcode[position]=oldline

if __name__ == "__main__":
    day08_01()
    day08_02()

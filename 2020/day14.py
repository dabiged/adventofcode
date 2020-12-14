"""
AOC day 14 2018
"""
from collections import defaultdict, deque
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Computer:
    ''' A computer for interfacing between the port computer and the ships computer'''
    def __init__(self,inputdata):
        ''' Initialise the computer and read in the instructions'''
        self.mask=''
        self.mem=defaultdict(int)
        self.inputdata=file_to_str_array(inputdata)
        self.intsize=36

    @staticmethod
    def bin2int(binarynum):
        ''' convert a 36 bit binary string to a int'''
        output=0
        for bit, multiplier in  zip([2**i for i in reversed(range(0,36))],binarynum):
            output+=bit*int(multiplier)
        return output

    @staticmethod
    def int2bin(integer):
        '''convert an integer to a 36 bit binary string'''
        binary=""
        for bitname in reversed(range(0,36)):
            if integer - 2**bitname >= 0 :
                binary+='1'
                integer -= 2**bitname
            else:
                binary+='0'
        return binary

    def apply_mask(self, mask,number):
        ''' apply a binary mask to an integer and return the masked int
        a bit mask of:
        0 or 1: overwrites the corresponding bit i,
        X:      leaves the bit in the value unchanged.
        >>> apply_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1',2)
        3
        >>> apply_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',11)
        73
        >>> apply_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',101)
        101
        '''
        assert len(mask) == 36
        number_binary = self.int2bin(number)
        assert len(number_binary) == 36

        output=""
        for maskchar, binchar in zip(mask,number_binary):
            if maskchar == 'X':
                output+=binchar
            else:
                output+=maskchar
        return self.bin2int(output)

    def run(self):
        '''process all input updating memory locations as we go'''
        for instr in self.inputdata:
            partinstr=instr.split('=')
            maskmem, value = partinstr[0].strip(), partinstr[1].strip()
            if maskmem[1] == 'a':
                self.mask = value
            elif maskmem[1] == 'e':
                memloc = int(maskmem.replace('mem[','').replace(']',''))
                self.mem[memloc] = self.apply_mask(self.mask,int(value))
            else:
                print('Unknown instruction found', instr)

        return sum(self.mem.values())

class ComputerVer2:
    ''' A computer for interfacing between the port computer and the ships computer

    The behaviour of the mask in this version is different as it acts as a memory address decoder'''
    def __init__(self,inputdata):
        ''' Initialise the computer and read in the instructions'''
        self.mask=''
        self.mem=defaultdict(int)
        self.inputdata=file_to_str_array(inputdata)
        self.intsize=36

    @staticmethod
    def bin2int(binarynum):
        ''' convert a 36 bit binary string to a int'''
        output=0
        for bit, multiplier in  zip([2**i for i in reversed(range(0,36))],binarynum):
            output+=bit*int(multiplier)
        return output

    @staticmethod
    def int2bin(integer):
        '''convert an integer to a 36 bit binary string'''
        binary=""
        for bitname in reversed(range(0,36)):
            if integer - 2**bitname >= 0 :
                binary+='1'
                integer -= 2**bitname
            else:
                binary+='0'
        return binary

    def apply_mask2memloc(self, mask,mastermemloc):
        '''
        Apply the mask to the memory location.

        return a list of ints of locations to write to
        each bit in the bitmask modifies the corresponding bit of the destination memory address:

        If the bitmask bit is 0, the corresponding memory address bit is unchanged.
        If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
        If the bitmask bit is X, the corresponding memory address bit is floating.

        floating bits will take on all possible values
        '''
        output=[]
        assert len(mask) == 36
        mastermemloc_binary = self.int2bin(mastermemloc)
        assert len(mastermemloc_binary) == 36

        # We are going to use a queue to deal with the growth in values.
        # Initialise it with a zero length string.
        queue = deque([''])
        while len(queue)>0:
            thismem=queue.pop()
            i=len(thismem)
            if len(thismem) == 36:
                # If memory address is built, add integer version to output list.
                output.append(self.bin2int(thismem))
            elif mask[i] == '0':
                # If the bitmask bit is 0, the corresponding memory address bit is unchanged.
                queue.append(thismem+mastermemloc_binary[i])
            elif mask[i] == '1':
                # If the bitmask bit is 1, the corresponding memory address bit is set to 1.
                queue.append(thismem+'1')
            elif mask[i] == 'X':
                # If the bitmask bit is X, the corresponding memory address bit is floating.
                # floating bits will take on all possible values
                queue.append(thismem+'1')
                queue.append(thismem+'0')
            else:
                print("Something went wrong in apply masked2memloc")
        return output

    def run(self):
        '''process all input updating memory locations as we go'''
        for instr in self.inputdata:
            partinstr=instr.split('=')
            maskmem, value = partinstr[0].strip(), partinstr[1].strip()
            if maskmem[1] == 'a':
                # A mask line
                self.mask = value
            elif maskmem[1] == 'e':
                # A mem line.
                # Get the memloc in the program
                mastermemloc = int(maskmem.replace('mem[','').replace(']',''))
                for memloc in self.apply_mask2memloc(self.mask,mastermemloc):
                    # Write to EACH memloc specified by masking the memloc.
                    self.mem[memloc] = int(value)
            else:
                print('Unknown instruction found', instr)

        return sum(self.mem.values())

def day14_01():
    """Run part 1 of Day 14's code"""
    path = "./input/14/input.txt"
    mycomp=Computer(path)
    result=mycomp.run()
    print(f'1401: Sum of memory values in computer: {result}')

def day14_02():
    """Run part 2 of Day 14's code"""
    path = "./input/14/input.txt"
    mycomp=ComputerVer2(path)
    result=mycomp.run()
    print(f'1402: Sum of memory value in version 2 of computer: {result}')

if __name__ == "__main__":
    day14_01()
    day14_02()

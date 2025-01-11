from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

testdata=''

class Computer():
    def __init__(self,A,B,C,program):
        self.program=[int(i) for i in program.split(',')]
        self.pointer=0
        self.RegisterA=int(A)
        self.RegisterB=int(B)
        self.RegisterC=int(C)
        self.output=[]

    def combo(self,val):
        if 0<=val<= 3:
            return val
        elif val == 4:
            return self.RegisterA
        elif val == 5:
            return self.RegisterB
        elif val == 6:
            return self.RegisterC
        elif val == 7:
            raise NotImplementedError
        else:
            print(f'combo: got value {val}.')
            raise ValueError

    def adv(self,operand):
        # division
        self.RegisterA = self.RegisterA // (2 ** self.combo(operand))
        self.pointer+=2

    def bxl(self,operand):
        # Bitwise XOR
        self.RegisterB = self.RegisterB ^ operand
        self.pointer+=2

    def bst(self,operand):
        # mod 8
        self.RegisterB = self.combo(operand) % 8
        self.pointer+=2

    def jnz(self,operand):
        if self.RegisterA == 0:
            self.pointer +=2
        else:
            self.pointer = operand

    def bxc(self,operand):
        _ = operand
        self.RegisterB = self.RegisterB ^ self.RegisterC
        self.pointer+=2

    def out(self,operand):
        self.output.append(self.combo(operand) % 8)
        self.pointer+=2

    def bdv(self,operand):
        self.RegisterB = self.RegisterA // (2 ** self.combo(operand))
        self.pointer+=2

    def cdv(self,operand):
        self.RegisterC = self.RegisterA // (2 ** self.combo(operand))
        self.pointer+=2

    def lookup(self,digit):
        if digit == 0:
            return self.adv
        elif digit == 1:
            return self.bxl
        elif digit == 2:
            return self.bst
        elif digit == 3:
            return self.jnz
        elif digit == 4:
            return self.bxc
        elif digit == 5:
            return self.out
        elif digit == 6:
            return self.bdv
        elif digit == 7:
            return self.cdv
        else:
            print(f'lookup: Asked to lookup {digit} at {self.pointer}')
            raise ValueError

    def run(self):
        while self.pointer < len(self.program):
            operation=self.lookup(self.program[self.pointer])
            operand=self.program[self.pointer+1]
            operation(operand)
        return ','.join([str(i) for i in self.output])

            


def part1(inputdata=testdata):
    m=Computer(25358015,0,0,'2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0')
    return m.run()

def part2(inputdata=testdata):
    def find_quine(init_a):
        program='2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0'
        output = []
        matched = program[-1:] 
        init_a = 8 ** 15 
        power = 14 

        while output != program:
            print(init_a)
            init_a += 8 ** power
            m=Computer(init_a,0,0,program)

            output = m.run()
            if output[-len(matched):] == matched:
                power = max(0, power - 1)
                matched = program[-(len(matched)+1):]
        return init_a
    print(find_quine(1))


def day17_01():
    """Run part 1 of Day 17's code"""
    path = "./input/17.txt"
    print("1701:", part1(file_to_str_array(path)))


def day17_02():
    """Run part 2 of Day 17's code"""
    path = "./input/17.txt"
    print("1702:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    #print(part1())
    print(part2())

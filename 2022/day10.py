from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

test_input='''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''.split('\n')

class CPU():
    def __init__(self, instrs):
        self.instrs=instrs
        self.instrs.reverse()
        self.registers={}
        self.screen=[]
        self.registers['x']=1
        self.score=0
        self.run()

    def run(self):
        self.count=1
        instr_done=True
        program_done=False
        while not program_done:
            if instr_done:
                if len(self.instrs):
                    instr=self.instrs.pop()
                elif instr_done:
                    program_done=True
                    return self.score
                operation=instr.split()[0]
                instr_done=False
                addx_seen=False

            if operation == 'noop':
                instr_done=True
            elif operation == 'addx' and not addx_seen:
                addx_seen=True
                instr_done=False
            elif operation == 'addx' and addx_seen:
                self.registers['x']+= int(instr.split()[1])
                instr_done=True

            self.count+=1

            self.check()
            self.draw()


    def check(self):
        if self.count % 40 == 20:
            self.score +=self.count*self.registers['x']

    def score(self):
        return self.score

    def draw(self):
        checker=self.count % 40
        if checker == self.registers['x'] or checker == self.registers['x']+1 or checker == self.registers['x']+2:
            self.screen.append('#')
        else:
            self.screen.append('.')

    def show(self):
        return "\n".join(["".join(self.screen[0:39]),"".join(self.screen[40:79]),"".join(self.screen[80:119]),"".join(self.screen[120:159]),"".join(self.screen[160:199]),"".join(self.screen[200:]),])

def main1(data):
    mycpu=CPU(data)
    return mycpu.score

def main2(data):
    mycpu=CPU(data)
    mycpu.run()
    print(mycpu.show())

def day10_01():
    """Run part 1 of Day 10's code"""
    path = "./input/input_10.txt"
    print("1001:", main1(file_to_str_array(path)))

def day10_02():
    """Run part 2 of Day 10's code"""
    path = "./input/input_10.txt"
    print("1002:")
    main2(file_to_str_array(path))

if __name__ == "__main__":
    day10_01()
    day10_02()

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Computer():
    def __init__(self,program):
        self.program=list(map(int,program))
        self.position=0
        self.visited={}
        self.steps=0

    def run(self):
        while True:
            try:
                self.step()
            except:
                return self.steps-1
    def newrun(self):
        while True:
            try:
                self.newstep()
            except:
                return self.steps-1

    def step(self):
        self.steps+=1
        instr=self.program[self.position]

        self.program[self.position]+=1
        self.position=self.position+instr


    def newstep(self):
        self.steps+=1
        instr=self.program[self.position]

        if instr >= 3:
            self.program[self.position]-=1
        else:
            self.program[self.position]+=1

        self.position=self.position+instr


    def __repr__(self):
        return f'Computer(Pos={self.position}, Step={self.steps}, Program={self.program})'


def day05_01():
    """Run part 1 of Day 5's code"""
    path = "./input/05/input.txt"

    mycomputer=Computer(file_to_str_array(path))
    print('0501:', mycomputer.run())



def day05_02():
    """Run part 2 of Day 5's code"""
    path = "./input/05/input.txt"
    mycomputer=Computer(file_to_str_array(path))
    print('0502:',mycomputer.newrun())


if __name__ == "__main__":
    day05_01()
    day05_02()

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

testdata='''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''


class Dial():
    def __init__(self,instructions,start=50):
        self.instructions=instructions
        self.position=start
        self.size=100
        self.password=0

    def step(self,instruction):
        direction = 1 if instruction[0] == 'R' else -1
        size=int(instruction[1:])

        self.position= (self.position + direction*size ) % self.size
        if self.position ==0:
            self.password+=1

    def step2(self,instruction):
        direction = 1 if instruction[0] == 'R' else -1
        size=int(instruction[1:])

        oldposition=self.position
        self.position= (self.position + direction*size ) % self.size

        while size > 99:
            # Handle more than 1 entire turn
            size-=100
            self.password+=1

        if self.position ==0:
            self.password+=1
        elif direction == -1 and oldposition < self.position and oldposition != 0:
            self.password+=1
        elif direction == 1 and oldposition > self.position and oldposition != 0:
            self.password+=1


    def process(self,part=1):
        if part ==1:
            for instruction in self.instructions:
               self.step(instruction)
        else:
            for instruction in self.instructions:
               self.step2(instruction)
        return self.password

def part1(inputdata=testdata):
    myDial=Dial(inputdata)
    return myDial.process()

def part2(inputdata=testdata):
    myDial=Dial(inputdata)
    return myDial.process(part=2)


def day01_01():
    """Run part 1 of Day 01's code"""
    path = "./input/01.txt"
    print("0101:", part1(file_to_str_array(path)))


def day01_02():
    """Run part 2 of Day 01's code"""
    path = "./input/01.txt"
    print("0102:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day01_01()
    day01_02()

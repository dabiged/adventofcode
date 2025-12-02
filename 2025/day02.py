from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
testdata='''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

testdata=testdata.split('\n')

class IntRange():
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.invalid=0
        self.suminvalid=0
        self.check()


    def check(self):
        for i in range(self.start,self.end+1):
            #print(i)
            if len(str(i)) % 2 == 1:
                continue
            length = len(str(i))//2
            #print(length)
            #print(str(i)[0:length])
            #print(str(i)[length:])
            if str(i)[0:length] == str(i)[length:]:
                #print(f'{i} is invalid')
                self.invalid+=1
                self.suminvalid+=i

    def __repr__(self):
        return f'{self.start=}, {self.end=}'


def part1(inputdata=testdata):
    total_invalid=0
    for line in inputdata:
        for inrange in line.split(','):
            if inrange == '':
                continue
            a=inrange.split('-')
            my=IntRange(int(a[0]),int(a[1]))
            total_invalid +=my.suminvalid
    print(total_invalid)

def part2(inputdata=testdata):
    pass


def day02_01():
    """Run part 1 of Day 02's code"""
    #part1(testdata)
    path = "./input/02.txt"
    print("0201:", part1(file_to_str_array(path)))


def day02_02():
    """Run part 2 of Day 02's code"""
    path = "./input/02.txt"
    print("0202:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day02_01()
    #day02_02()

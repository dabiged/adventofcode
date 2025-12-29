from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
testdata='''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

testdata=testdata.split('\n')

def all_same(items:list):
    if not items:
        return True
    first_element = items[0]
    return all(x == first_element for x in items)


def is_invalid(num,inc=2):
    candidates=[]
    position=0
    while position < len(num):
        candidates.append(int(num[position:position+inc]))
        position+=inc
    return all_same(candidates)

class IntRange():
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.invalid=0
        self.suminvalid=0


    def check_pt1(self):
        for i in range(self.start,self.end+1):
            if len(str(i)) % 2 == 1:
                continue
            length = len(str(i))//2
            if str(i)[0:length] == str(i)[length:]:
                self.invalid+=1
                self.suminvalid+=i

    def check_pt2(self):
        # check all numbers
        invalid=set()
        for i in range(self.start,self.end+1):
            # check if invalid
            length = len(str(i))//2
            for inc in range(1,length+1):
                if is_invalid(str(i),inc):
                    invalid.add(i)
        self.suminvalid=sum(list(invalid))

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
            my.check_pt1()
            total_invalid +=my.suminvalid
    print(total_invalid)

def part2(inputdata=testdata):
    total_invalid=0
    for line in inputdata:
        for inrange in line.split(','):
            if inrange == '':
                continue
            a=inrange.split('-')
            my=IntRange(int(a[0]),int(a[1]))
            my.check_pt2()
            total_invalid +=my.suminvalid

    return total_invalid



def day02_01():
    """Run part 1 of Day 02's code"""
    #part1(testdata)
    path = "./input/02.txt"
    print("0201:", part1(file_to_str_array(path)))


def day02_02():
    """Run part 2 of Day 02's code"""
    #part2(testdata)
    path = "./input/02.txt"
    print("0202:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    #day02_01()
    day02_02()

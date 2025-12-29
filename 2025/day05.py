from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

testdata='''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

testdata=testdata.split('\n')

def format(inputdata):
    ranges=[]
    ings=[]
    rangesection=True
    for line in inputdata:
        if line == '':
            rangesection=False
            continue
        if rangesection:
            ranges.append(line)
        else:
            ings.append(line)
    return ings,ranges


def part1(inputdata=testdata):
    ings,ranges=format(inputdata)

    count=0
    for ing in ings:
        ing=int(ing)
        for this_range in ranges:
            a=this_range.split('-')
            if ing in range(int(a[0]),int(a[1])+1):
                count+=1
                break
    return count

class IntRange():
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def within(self,val):
        return val in range(self.start,self.end+1)

    def is_combinable(self,intrange):
        if self.end < intrange.start or self.start > intrange.end:
            return False
        return True

    def combine(self,intrange):
        if self.within(intrange.start) and self.within(intrange.end):
            return self
        elif self.within(intrange.start):
            return IntRange(self.start, intrange.end)
        elif self.within(intrange.end):
            return IntRange(intrange.start,self.end)
        else:
            return self, intrange

    def __lt__(self,other):
        return self.start < other.start

    def __len__(self):
        return self.end-self.start+1

    def __repr__(self):
        return f'IntRange: {self.start} - {self.end}'


def coalesce(inputlist):
    merged=[]
    intrange1=inputlist[0]
    for intrange2 in inputlist[1:]:
        if intrange2.start <= intrange1.end+1:
            intrange1=IntRange(intrange1.start,max(intrange2.end,intrange1.end))
        else:
            merged.append(intrange1)
            intrange1=intrange2
    merged.append(intrange1)
    return merged

def part2(inputdata=testdata):
    ings,ranges=format(inputdata)
    intranges=[]
    for this_range in ranges:
        a=this_range.split('-')
        intranges.append(IntRange(int(a[0]),int(a[1])))
    intranges.sort()

    merged=coalesce(intranges)

    totalsize=0
    for intrange in merged:
        totalsize+=len(intrange)
    return totalsize
        



def day05_01():
    """Run part 1 of Day 05's code"""
    path = "./input/05.txt"
    print("0501:", part1(file_to_str_array(path)))


def day05_02():
    """Run part 2 of Day 05's code"""
    path = "./input/05.txt"
    print("0502:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day05_01()
    day05_02()

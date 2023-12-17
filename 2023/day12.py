from lib.filehelper import file_to_str_array, get_bald_string_list_from_file, file_to_array
# pylint: disable=missing-module-docstring
import itertools
from collections import deque

test_input=['???.### 1,1,3',
'.??..??...?##. 1,1,3',
'?#?#?#?#?#?#?#? 1,3,1,6',
'????.#...#... 4,1,1',
'????.######..#####. 1,6,5',
'?###???????? 3,2,1']

def replace_unknowns(inputlist):
    output=[]
    processing_q=deque()
    processing_q.append(inputlist)
    while len(processing_q) > 0:
        thisinput=processing_q.pop()
        if '?' not in thisinput:
            output.append(thisinput)
        else:
            processing_q.append(thisinput.replace('?','.',1))
            processing_q.append(thisinput.replace('?','#',1))
    return output


class Map():
    def __init__(self,springs,inputmap):
        self.springs=springs
        self.inputmap=inputmap
        self.numunknown=sum([i=='?' for i in self.springs])


    def test(self,inputstr):
        output=[]
        inspring=False
        lenspring=0
        for i,char in enumerate(inputstr):
            if char == '.' :
                if inspring:
                    output.append(lenspring)
                    lenspring=0
                inspring=False
            elif char == '#' :
                lenspring+=1
                if not inspring:
                    inspring=True
        if char == '#':
            output.append(lenspring)
        return output

    def generate_possible(self):
        return replace_unknowns(self.springs)

    def count_valid(self):
        count=0
        for possible in self.generate_possible():
            if self.test(possible) == self.inputmap:
                count+=1
        return count

    def parse(self):
        pass


def part1(inputdata=test_input):
    total_valid=0
    for row in inputdata:
        print(row)
        springs=row.split()[0]
        definition=row.split()[1]

        m=Map(springs,[int(i) for i in definition.split(',')])
        total_valid+=m.count_valid()
    return total_valid


def part2(inputdata=test_input):
    total_valid=0
    for row in inputdata:
        springs=row.split()[0]
        definition=row.split()[1]
        fivesprings='?'.join([springs]*5)
        fivedefinitions=','.join([definition]*5)

    return total_valid

def day12_01():
    """Run part 1 of Day 7's code"""
    path = "./input/12.txt"
    print("1201:", part1(file_to_str_array(path)))


def day12_02():
    """Run part 2 of Day 1's code"""
    path = "./input/12.txt"
    print("1202:", part2(file_to_str_array(path)))


if __name__ == "__main__":
    day12_01()
    day12_02()

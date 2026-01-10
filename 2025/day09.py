from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring
testdata='''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''


testdata=testdata.split('\n')

class Rectangle():
    def __init__(self,pt1,pt2):
        self.x1=int(pt1[0])
        self.y1=int(pt1[1])
        self.x2=int(pt2[0])
        self.y2=int(pt2[1])
        
    def area(self):
        return (max(self.x1,self.x2)-min(self.x1,self.x2)+1) * ( max(self.y1,self.y2)-min(self.y1,self.y2)+1)


def part1(inputdata=testdata):
    maxarea=-1
    for a,coord1 in enumerate(inputdata):
        for coord2 in inputdata[a:]:
            maxarea=max(Rectangle(coord1.split(','),coord2.split(',')).area(),maxarea)
            print(coord1,coord2,maxarea)
    return maxarea


def part2(inputdata=testdata):
    return None

def day09_01():
    """Run part 1 of Day 09's code"""
    part1()
    path = "./input/09.txt"
    print("0901:", part1(file_to_str_array(path)))


def day09_02():
    """Run part 2 of Day 09's code"""
    #part2(testdata)
    path = "./input/09.txt"
    print("0902:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day09_01()
    #day09_02()

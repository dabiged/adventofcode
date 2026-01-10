from lib.filehelper import file_to_str_array
from collections import defaultdict, OrderedDict
import math
# pylint: disable=missing-module-docstring
testdata='''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''
testdata=testdata.split('\n')


class Connection():
    def __init__(self,box1,box2):
        pass

class Box():
    def __init__(self,x,y,z):
        self.x=int(x)
        self.y=int(y)
        self.z=int(z)

    def dist(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)

    def __repr__(self):
        return f'Box: ({self.x},{self.y},{self.z})'

    def __hash__(self):
        return hash((self.x,self.y,self.z))


def add_connection(connectionlist,box1,box2):
    ''' Connectionlist is a list of sets
    box1 and box2 need to be added.'''
    #      get box1's index
    for i,connection in enumerate(connectionlist):
        for box in connection:
            if box1 == box:
                box1.index=i
    for i,connection in enumerate

def part1(inputdata=testdata):
    boxes=[]
    #    intialise box objects
    for line in inputdata:
        a=line.split(',')
        boxes.append(Box(a[0],a[1],a[2]))
    connections=[]
    dists={}
    # get the list of the closest boxes
    for i,box1 in enumerate(boxes):
        connections.append=set(box1)
        for box2 in boxes[i+1:]:
            dists[box1.dist(box2)]=[box1,box2]
    ordereddists=OrderedDict(sorted(dists.items()))        
    # loop over the closest distances
    count=0
    for k,v in ordereddists.items():
        box1,box2 = v
        add_connection(connections,box1,box2)
        count+=1
        if count == 2:
            break

    for k,v in connections.items():
        print(k,len(v))







def part2(inputdata=testdata):
    pass

def day08_01():
    """Run part 1 of Day 08's code"""
    part1(testdata)
    #path = "./input/08.txt"
    #print("0802:", part1(file_to_str_array(path)))


def day08_02():
    """Run part 2 of Day 08's code"""
    #part2(testdata)
    path = "./input/08.txt"
    print("0802:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day08_01()
    #day08_02()

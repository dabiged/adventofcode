from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

import time

test_input='''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''.split('\n')

class Node():
    def __init__(self,position,height,distance,parent):
        self.position=position
        self.height=height
        self.distance=distance
        self.parent=parent

    def neighbours(self,allplaces):
        neighbours=[]
        r,c=self.position
        if (r-1,c) in allplaces:
            neighbours.append((r-1,c))
        if (r+1,c) in allplaces:
            neighbours.append((r+1,c))
        if (r,c+1) in allplaces:
            neighbours.append((r,c+1))
        if (r,c-1) in allplaces:
            neighbours.append((r,c-1))
        return neighbours

    def __repr__(self):
        return f'Node({self.position}, H:{self.height} D:{self.distance})'



def run1(definition):
    heights={v:k for k,v in enumerate('abcdefghijklmnopqrstuvwxyz')}

    height_map={}
    for row,rowdata in enumerate(definition):
        for col, char in enumerate(rowdata):
            if char=='S':
                start=(row,col)
                char='a'
            if char=='E':
                end=(row,col)
                char='z'
            height_map[(row,col)]=heights[char]

    nodes={}

    nodes[end]=Node(end,0,0,None)
    visited=[]
    toprocess=[(end)]

    while toprocess:
        currloc=toprocess.pop(0)
        if currloc in visited:
            continue
        currnode=nodes[currloc]
        visited.append(currloc)



        for neighbour in currnode.neighbours(height_map.keys()):
            if neighbour in visited:
                continue
            if height_map[neighbour]+ 1  >= height_map[currloc]:
                nodes[neighbour]=Node(neighbour,height_map[neighbour],currnode.distance+1,currnode)
                toprocess.append(neighbour)

        if start in nodes.keys():
            currnode=nodes[start]
            path=[]
            while currnode != None:
                path.append(currnode.position)
                currnode=currnode.parent
            total=[]
            path.reverse()

            return nodes[start].distance

def run2(definition):
    heights={v:k for k,v in enumerate('abcdefghijklmnopqrstuvwxyz')}

    height_map={}
    all_as=[]
    for row,rowdata in enumerate(definition):
        for col, char in enumerate(rowdata):
            if char=='S':
                start=(row,col)
                char='a'
            if char=='E':
                end=(row,col)
                char='z'
            if char=='a':
                all_as.append((row,col))
            height_map[(row,col)]=heights[char]

    nodes={}

    nodes[end]=Node(end,0,0,None)
    visited=[]
    toprocess=[(end)]

    while toprocess:
        currloc=toprocess.pop(0)
        if currloc in visited:
            continue
        currnode=nodes[currloc]
        visited.append(currloc)



        for neighbour in currnode.neighbours(height_map.keys()):
            if neighbour in visited:
                continue
            if height_map[neighbour]+ 1  >= height_map[currloc]:
                nodes[neighbour]=Node(neighbour,height_map[neighbour],currnode.distance+1,currnode)
                toprocess.append(neighbour)

        if len(set(all_as).intersection(set(nodes.keys()))) > 1:
            #print(set(all_as).intersection(set(nodes.keys())))
            start=(11,0)
            currnode=nodes[start]
            path=[]
            while currnode != None:
                path.append(currnode.position)
                currnode=currnode.parent
            total=[]
            path.reverse()

            return nodes[start].distance

def main1(data):
    return run1(data)


def main2(data):
    return run2(data)

def day12_01():
    """Run part 1 of Day 12's code"""
    path = "./input/input_12.txt"
    print("1201:",main1(file_to_str_array(path)))

def day12_02():
    """Run part 2 of Day 12's code"""
    path = "./input/input_12.txt"
    print("1202:",main2(file_to_str_array(path)))

if __name__ == "__main__":
    day12_01()
    day12_02()


from lib.filehelper import file_to_str_array, get_bald_string_list_from_file, file_to_array
# pylint: disable=missing-module-docstring
from collections import deque, defaultdict
import re

replaceLJ = re.compile(r"L-*J", re.IGNORECASE)
replaceF7 = re.compile(r"F-*7", re.IGNORECASE)
replaceL7 = re.compile(r"L-*7", re.IGNORECASE)
replaceFJ = re.compile(r"F-*J", re.IGNORECASE)


test_input=['.....',
'.S-7.',
'.|.|.',
'.L-J.',
'.....']

test_input1=['..F7.',
'.FJ|.',
'SJ.L7',
'|F--J',
'LJ...']

test_input2=['...........',
'.S-------7.',
'.|F-----7|.',
'.||.....||.',
'.||.....||.',
'.|L-7.F-J|.',
'.|..|.|..|.',
'.L--J.L--J.',
'...........']


class Node():
    def __init__(self,loc,char):
        self.char=char
        self.loc=loc

    def neighbours(self):
        neighbours=[]
        if self.char=='|':
            neighbours.append(1j)
            neighbours.append(-1j)
        elif self.char=='-':
            neighbours.append(1)
            neighbours.append(-1)
        elif self.char=='.':
            return []
        elif self.char=='L':
            neighbours.append(-1j)
            neighbours.append(1)
        elif self.char=='J':
            neighbours.append(-1j)
            neighbours.append(-1)
        elif self.char=='7':
            neighbours.append(1j)
            neighbours.append(-1)
        elif self.char=='F':
            neighbours.append(1j)
            neighbours.append(1)
        else:
            raise RuntimeError
        output=[]
        for i in neighbours:
            output.append(i+self.loc)
        return output





class Map():
    def __init__(self,nodes):
        self.dist={}
        self.nodes=nodes
        self.map={}
        self.start=None
        self.starting_neighbours=[]
        self.numrows=-1
        self.numcols=-1
        self.parse()
        self.visited=set()
        self.toprocess=deque()

    def parse(self):
        for row,rowchars in enumerate(self.nodes):
            for col,char in enumerate(rowchars):
                self.map[col+row*1j]=Node(col+row*1j,char)
                if char == 'S':
                    self.map[col+row*1j]=Node(col+row*1j,'|')
                    self.start=col+row*1j
        self.numrows=row
        self.numcols=col
        self.get_start_neighbours()

    def get_start_neighbours(self):
        dirs=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j ==0:
                    pass
                else:
                    loc=self.start + i+j*1j
                    if self.start in self.map[loc].neighbours():
                        dirs.append(i+j*1j)
                        self.starting_neighbours.append(loc)

    def walk(self):
        max_dist=-1
        currloc=self.start
        self.visited.add(self.start)
        for loc in self.starting_neighbours:
            self.toprocess.append((1,loc))
        while len(self.toprocess) >0:
            dist,loc=self.toprocess.popleft()
            if loc not in self.visited:
                self.dist[loc]=dist
                max_dist=max(dist,max_dist)
                self.visited.add(loc)
                for neighbour in self.map[loc].neighbours():
                    self.toprocess.append((dist+1,neighbour))
        return max_dist


    def inside_or_out(self,loc):
        ''' determine if a location is within the polygon'''
        row=int(loc.imag)
        leftstr=''
        for col in range(int(loc.real)+1):
            currloc=col+row*1j
            if currloc in self.visited:
                leftstr+=self.map[currloc].char
            else:
                leftstr+='.'
        output=leftstr
        output=replaceF7.sub('',output)
        output=replaceL7.sub('|',output)
        output=replaceFJ.sub('|',output)
        output=replaceLJ.sub('',output)

        parity=0
        for char in output:
            if char == '|':
                parity+=1
        return parity %2

    def ins_and_outs(self):
        '''return a string representation of the ins and outs locations and the loop'''
        output=''
        for row in range(self.numrows+1):
            thisrow=''
            for col in range(self.numcols+1):
                currloc=col+row*1j
                if currloc in self.visited:
                    thisrow+=self.map[currloc].char
                else:
                    if self.inside_or_out(currloc) == 1:
                        thisrow+='I'
                    elif self.inside_or_out(currloc) ==0:
                        thisrow+='O'
                    else:
                        raise
            output+=thisrow+'\n'
        return output+'\n'

    def count_ins(self):
        ''' return the number of locations inside the polygon'''
        count=0
        inputs=self.ins_and_outs()
        for row in inputs.split():
            for char in row:
                if char == 'I':
                    count+=1
        return count



    def __str__(self):
        output=''
        for row in range(self.numrows+1):
            thisrow=''
            for col in range(self.numcols+1):
                thisrow+=self.map[col+row*1j].char
            output+=thisrow+'\n'
        output+'\n'
        for row in range(self.numrows+1):
            thisrow=''
            for col in range(self.numcols+1):
                if col+row*1j not in self.dist.keys():
                    thisrow+='.'
                else:
                    thisrow+=str(self.dist[col+row*1j])
            output+=thisrow+'\n'
        output+'\n'
        return output


def part1(inputdata=test_input1):
    m=Map(inputdata)
    m.walk()
    dists=defaultdict(list)
    for k,v in m.dist.items():
        dists[v].append(k)
    looplen=0
    for k,v in dists.items():
        if len(v) == 2:
            looplen=max(looplen,k)
    return looplen+1


def part2(inputdata=test_input2):
    m=Map(inputdata)
    m.walk()
    return m.count_ins()



def day10_01():
    """Run part 1 of Day 7's code"""
    path = "./input/10.txt"
    print("1001:", part1(file_to_str_array(path)))


def day10_02():
    """Run part 2 of Day 1's code"""
    path = "./input/10.txt"
    print("1002:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day10_01()
    day10_02()

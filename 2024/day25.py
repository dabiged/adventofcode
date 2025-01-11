from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

testdata='''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####'''


def isLock(block):
    ''' return true  if lock
        return false if key
        raise if anything else
        '''
    for line in block.split():
        if line == '#####':
            return True
        elif line == '.....':
            return False
        else:
            raise


class Lock():
    def __init__(self,block):
        self.block=block
        cols=defaultdict(str)
        for row in block.split():
            for col,char in enumerate(row):
                cols[col]+=char
        sizes=[]
        for i in range(5):
            sizes.append(cols[i].count('#')-1)
        self.vals=tuple(sizes)

    def keyfits(self,key):
        for i in range(5):
            k=key.vals[i]
            l=self.vals[i]
            if k+l > 5:
                return False
        return True


class Key():
    def __init__(self,block):
        self.block=block
        cols=defaultdict(str)
        for row in block.split():
            for col,char in enumerate(row):
                cols[col]+=char
        sizes=[]
        for i in range(5):
            sizes.append(cols[i].count('#')-1)
        self.vals=tuple(sizes)


def part1(inputdata=testdata.split('\n\n')):
    KeyList=[]
    LockList=[]
    match=0
    for block in inputdata:
        if isLock(block):
            LockList.append(Lock(block))
        else:
            KeyList.append(Key(block))
    for lock in LockList:
        for key in KeyList:
            if lock.keyfits(key):
                match+=1
    return match



def day25_01():
    """Run part 1 of Day 25's code"""
    path = "./input/25.txt"
    print("2501:", part1(('\n'.join(file_to_str_array(path)).split('\n\n'))))


if __name__ == "__main__":
    part1()
    day25_01()

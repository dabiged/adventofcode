from lib.filehelper import get_string_lists_from_file, get_map_from_file, file_to_str_array
# pylint: disable=missing-module-docstring
import itertools
from collections import defaultdict

test_input=['O....#....',
'O.OO#....#',
'.....##...',
'OO.#O....O',
'.O.....O#.',
'O.#..O.#.#',
'..O..#O..O',
'.......O..',
'#....###..',
'#OO..#....']

class Platform():
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.map={}
        self.parse()
        self.offset=0
        self.cycle_len=0

    def parse(self):
        for r,rch in enumerate(self.inputdata):
            for c,ch in enumerate(rch):
                self.map[c+r*1j]=ch

        self.numrows=r
        self.numcols=c

    def locate_rocks(self):

        self.rock_positions=[]
        for k,v in self.map.items():
            if v == 'O':
                self.rock_positions.append(k)
        self.rock_positions.sort(key=lambda x: x.imag*1000+x.real)


    def move_rock(self,start_pos,rotation=1,verbose=False):
        if verbose:
            print('rock at:',start_pos)
        done=False
        pos=start_pos
        while not done:

            candidate_pos=pos - 1j
            if verbose:
                print('candidate:',candidate_pos)
            if candidate_pos not in self.map.keys():
                if verbose:
                    print('outside')
                break
            elif self.map[candidate_pos] in ['O','#']:
                if verbose:
                    print('obstacle')
                break

            else:
                self.map[pos]='.'
                self.map[candidate_pos]='O'
                pos=candidate_pos
                if verbose:
                    print('moved:',pos, 'to',candidate_pos)
            if verbose:
                print(self)

    def roll_north(self):
        self.locate_rocks()
        for rockpos in self.rock_positions:
            self.move_rock(rockpos,-1j)

    def rotate(self):
        newmap={}
        for k,v in self.map.items():
            newmap[k*1j]=v
        self.map=newmap


    def cycle(self,numcycles=0):
        self.scores={}
        maps=set()
        for cycle in range(1,numcycles):
            self.roll_north()
            self.rotate()
            self.roll_north()
            self.rotate()
            self.roll_north()
            self.rotate()
            self.roll_north()
            self.rotate()
            print(cycle)
            self.locate_rocks()
            fingerprint="".join([str(int(i.imag))+str(int(i.real)) for i in self.rock_positions])
            if fingerprint not in maps:
                maps.add(fingerprint)
            else:
                for k,v in self.scores.items():
                    if self.count_load() == v:
                        pass
            self.scores[cycle]=self.count_load()

    def get_score(self,numcycles):
        if not self.offset:
            self.cycle(200)
        if numcycles <= self.offset:
            return self.cycles[numcycles]
        else:
            return self.scores[(( numcycles -120) % 42 ) + 120]
            #print(self)

    def count_load(self):
        total=0
        for r in range(self.numrows+1):
            for c in range(self.numcols+1):
                if self.map[r*1j+c] == 'O':
                    total+=self.numrows-r+1
        return total

    def __str__(self):
        output='\n'
        for r in range(self.numrows+1):
            thisrow=''
            for c in range(self.numcols+1):
                thisrow+=self.map[c+r*1j]
            output+=thisrow+'\n'
        return output



def part1(inputdata=test_input):
    myp=Platform(inputdata)
    myp.roll_north()
    return myp.count_load()




def part2(inputdata=test_input):
    myp=Platform(inputdata)
    ### 197 102193
    ### 198 102144
    ### 199 102095

    print('1000000000',myp.get_score(1000000000))
    return myp.count_load()

def day14_01():
    """Run part 1 of Day 7's code"""
    path = "./input/14.txt"
    #print(part1())
    print("1401:", part1(file_to_str_array(path)))


def day14_02():
    """Run part 2 of Day 1's code"""
    path = "./input/14.txt"
    #print(part2())
    print("1402:", part2(file_to_str_array(path)))


if __name__ == "__main__":
    day14_01()
    day14_02()

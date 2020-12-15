"""
AOC day 15 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class MemoryGame:
    '''
    In this game, the players take turns saying numbers.
    They begin by taking turns reading from a list of starting numbers (your puzzle input).
    Then, each turn consists of considering the most recently spoken number:

    If that was the first time the number has been spoken, the current player says 0.
    Otherwise, the number had been spoken before;
        the current player announces how many turns apart the number is from when it was previously spoken.
    '''
    def __init__(self,inputstr):
        '''Read in input str and intialise variables'''
        self.spoken=[]
        for num in inputstr.split(','):
            self.spoken.append(int(num))


    def taketurn(self, last_spoken):
        if last_spoken not in self.spoken[:-1]:
            self.spoken.append(0)
            return 1
        else:
            found=[]
            for turns_since_spoken_last in reversed(range(0,len(self.spoken))):
                if self.spoken[turns_since_spoken_last] == last_spoken:
                    found.append(turns_since_spoken_last)
                if len(found) == 2:
                    self.spoken.append(found[0]- found[1])
                    break

    def run(self,numruns=2019):
        for turn in range(len(self.spoken),numruns):
            self.taketurn(self.spoken[-1])
        return self.spoken[-1], len(self.spoken)


def day15_01():
    """Run part 1 of Day 15's code"""
    mymemgame=MemoryGame('19,0,5,1,10,13')
    mymemgame.run(numruns=2025)
    result=mymemgame.spoken[2019]
    print(f'1501: {result}')

def day15_02():
    """Run part 2 of Day 15's code"""
    mymemgame=MemoryGame('19,0,5,1,10,13')
    mymemgame.run(numruns=50000)
    result=""
    print(f'1502: {result}')

if __name__ == "__main__":
    #day15_01()
    day15_02()

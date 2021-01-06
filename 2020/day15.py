"""
AOC day 15 2018
"""
# pylint: disable=missing-module-docstring

class MemoryGame:
    '''
    In this game, the players take turns saying numbers.
    They begin by taking turns reading from a list of starting numbers (your puzzle input).
    Then, each turn consists of considering the most recently spoken number:

    If that was the first time the number has been spoken, the current player says 0.
    Otherwise, the number had been spoken before;
        the current player announces how many turns apart the number is from
        when it was previously spoken.
    '''
    def __init__(self,inputstr):
        '''Read in input str and intialise variables'''
        self.spoken={}
        self.index=1
        self.previous=0
        self.inputstr=inputstr
        for num in inputstr.split(','):
            # memory will be a dict of the last two entries.
            self.spoken[int(num)] = [self.index,self.index]
            self.index+=1
            self.previous=int(num)

    def run(self,numturns):
        ''' Play the game for numturns'''
        while self.index <= numturns:
            #if self.index % 1000000 == 0:
                #print("On loop:", self.index)
            # Loop until we get to the last turn
            if self.spoken[self.previous][0] == self.spoken[self.previous][1]:
                # If the last and second last turns are equal this
                #   is the first time we have seen this number.
                self.previous=0
            else:
                # Otherwise calc the difference
                self.previous = self.spoken[self.previous][1]-self.spoken[self.previous][0]

            if self.previous in self.spoken:
                # move the value of the oldest location out, and replace it.
                self.spoken[self.previous][0] = self.spoken[self.previous][1]
                self.spoken[self.previous][1] = self.index
            else:
                self.spoken[self.previous] = [self.index,self.index]

            self.index+=1

        return self.previous

def day15_01():
    """Run part 1 of Day 15's code"""
    mymemgame=MemoryGame('19,0,5,1,10,13')
    result=mymemgame.run(numturns=2020)
    print(f'1501: 2020th number spoken is: {result}')

def day15_02():
    """Run part 2 of Day 15's code"""
    mymemgame=MemoryGame('19,0,5,1,10,13')
    result= mymemgame.run(numturns=30000000)
    print(f'1502: 30,000,000th number spoken is: {result}')

if __name__ == "__main__":
    day15_01()
    day15_02()

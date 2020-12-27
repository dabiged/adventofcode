"""
AOC day 23 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


class CrabCups:
    def __init__(self,labels):
        '''Take in a list and initialise our cycle dict
        the dictionary cycle, points to the next location in our circle'''

        self.cups = labels
        self.maxval=max(self.cups)

        self.currentcup = self.cups[0]

        self.cycle=dict(zip(self.cups, self.cups[1:]))
        self.cycle[self.cups[-1]] = self.cups[0]

    def pickup(self,num=3):
        '''pickup num cups'''
        hand=[]
        # Grab the next cup in the cycle
        hand.append(self.cycle[self.currentcup])
        for _ in range(num-1):
            # Then grab the next card after that... etc.
            hand.append(self.cycle[hand[-1]])
        return hand

    def play(self,numturns=100, verbose=False):
        '''play crab cups for numturns'''
        for turn in range(numturns):
            hand=self.pickup()
            if verbose:
                print("Turn",turn+1)
                print("Hand",hand)
                print(self.cycle)
            next_cup= self.currentcup -1
            while next_cup in hand or next_cup <= 0:
                next_cup -= 1
                if next_cup <=0:
                    next_cup = self.maxval

            # Point the current location, to the location immediately after the last card in our hand.
            self.cycle[self.currentcup] = self.cycle[hand[-1]]
            # point the last card in our hand to the card following the destination cup.
            self.cycle[hand[-1]] = self.cycle[next_cup]
            # point the destination cup to the first card in our hand
            self.cycle[next_cup] = hand[0]
            # the new location is the one immediately following this one.
            self.currentcup = self.cycle[self.currentcup]

    def output(self):
        ''' Part 1 output'''
        output=''
        output+=str(self.cycle[1])
        for i in range(7):
            output+=str(self.cycle[int(output[-1])])
        return output

def day23_01():
    """Run part 1 of Day 23's code"""
    mygame=CrabCups([int(i) for i in '389547612'])
    mygame.play(numturns=100)
    result=mygame.output()
    print(f'2301: Order of crab cup labels is: {result}')

def day23_02():
    """Run part 2 of Day 23's code"""
    mygame=CrabCups([int(i) for i in '389547612']+list(range(10,1000001)))
    mygame.play(numturns=10000000)
    cup1=mygame.cycle[1]
    cup2=mygame.cycle[cup1]
    result = cup1 * cup2
    print(f'2302: Product of cup labels: {result}')

if __name__ == "__main__":
    day23_01()
    day23_02()

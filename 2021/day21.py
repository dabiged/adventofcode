"""
AOC day 21 2018
"""
from lib.filehelper import file_to_str_array
from collections import deque, defaultdict
import itertools
# pylint: disable=missing-module-docstring

class Die:
    def __init__(self):
        self.nums=itertools.cycle(range(1,101))
        self.rolls=0

    def roll(self):
        self.rolls+=3
        return sum(next(self.nums) for _ in range(3))

class DiceGame():
    def __init__(self,p1pos,p2pos):
        self.p1pos=p1pos
        self.p2pos=p2pos
        self.p1score=0
        self.p2score=0
        self.die=Die()

    def move(self,player,num):
        if player == 1:
            self.p1pos = (self.p1pos+num) % 10 +10*((self.p1pos+num) % 10 ==0 )
            self.p1score+=self.p1pos
            print(f'Player 1 Rolls: {num} and moves to {self.p1pos} for a total score of {self.p1score}')
        if player == 2:
            self.p2pos = (self.p2pos+num) % 10 +10*((self.p2pos+num) % 10 ==0 )
            self.p2score+=self.p2pos
            print(f'Player 2 Rolls: {num} and moves to {self.p2pos} for a total score of {self.p2score}')

    def isgameover(self):
        if self.p1score >=1000:
            return True
        if self.p2score >=1000:
            return True
        return False

    def play(self):
        turn=0
        while not self.isgameover():
            turn+=1
            self.move(1,self.die.roll())
            if self.isgameover():
                break

            self.move(2,self.die.roll())

            if self.isgameover():
                break
        if self.p1score >= 1000:
            return self.die.rolls*self.p2score
        elif self.p2score>= 1000:
            return self.die.rolls*self.p1score

    def part2(self):
        pass



def day21_01():
    """Run part 1 of Day 21's code"""
    mygame=DiceGame(8,6)
    result=mygame.play()
    print(f'2101: {result}')

def day21_02():
    """Run part 2 of Day 21's code"""
    path = "./input/day21.txt"
    result=""
    print(f'2102: {result}')

if __name__ == "__main__":
    day21_01()
    #day21_02()

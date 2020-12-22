"""
AOC day 22 2018
"""
from collections import deque
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class CombatGame:
    def __init__(self,inputfile):
        ''' Read in file and setup player hands '''
        with open(inputfile) as f:
            playerhands = f.read().split('\n\n')
        self.player1hand=deque([int(i) for i in playerhands[0].split('\n')[1:]])
        self.player2hand=deque([int(i) for i in playerhands[1].split('\n')[1:]])

    def play(self):
        '''
        Play the game.
        '''
        n=0
        while len(self.player1hand) >0 and len(self.player2hand) >0:
            print("-- Round",n,"--")
            print("Player 1's hand: ",self.player1hand)
            print("Player 2's hand: ",self.player2hand)

            player1card=self.player1hand.popleft()
            print("Player 1 plays:", player1card)
            player2card=self.player2hand.popleft()
            print("Player 2 plays:", player2card)
            if player1card > player2card:
                print("Player 1 wins!")
                self.player1hand.append(player1card)
                self.player1hand.append(player2card)
            elif player2card > player1card:
                print("Player 2 wins!")
                self.player2hand.append(player2card)
                self.player2hand.append(player1card)
            else:
                raise ValueError('Duplicate values found')
            n+=1


        print("== Post Game results ==")
        print("Player 1's deck:",self.player1hand)
        print("Player 2's deck:",self.player2hand)

    def score(self):
        '''
        Return the score of both players.
        '''
        player1score=0
        player2score=0
        n1=1
        n2=1
        while len(self.player1hand) >0 :
            player1score+=self.player1hand.pop()*n1
            n1+=1
        while len(self.player2hand) >0 :
            player2score+=self.player2hand.pop()*n2
            n2+=1

        return player1score, player2score


def day22_01():
    """Run part 1 of Day 22's code"""
    path = "./input/22/input.txt"
    mygame=CombatGame(path)
    mygame.play()
    p1s, p2s = mygame.score()
    print(f'2201: Player1: {p1s}, Player2: {p2s}')

def day22_02():
    """Run part 2 of Day 22's code"""
    path = "./input/22/input.txt"
    result=""
    print(f'2202: {result}')

if __name__ == "__main__":
    day22_01()
    #day22_02()

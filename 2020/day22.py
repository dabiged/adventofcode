"""
AOC day 22 2018
"""
from copy import deepcopy
from collections import deque
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


# Part 1
class CombatGame:
    ''' A combat game to play with a crab?!?!?'''
    def __init__(self,inputfile):
        ''' Read in input data and store hands as deques'''
        ''' Read in file and setup player hands '''
        with open(inputfile) as f:
            playerhands = f.read().split('\n\n')
        self.player1hand=deque([int(i) for i in playerhands[0].split('\n')[1:]])
        self.player2hand=deque([int(i) for i in playerhands[1].split('\n')[1:]])

    def play(self,verbose=False):
        '''  Play the game. '''
        n=0
        while len(self.player1hand) >0 and len(self.player2hand) >0:
            if verbose:
                print("-- Round",n,"--")
                print("Player 1's hand: ",self.player1hand)
                print("Player 2's hand: ",self.player2hand)
                print("Player 1 plays:", player1card)
                print("Player 2 plays:", player2card)
            player1card=self.player1hand.popleft()
            player2card=self.player2hand.popleft()
            if player1card > player2card:
                if verbose:
                    print("Player 1 wins!")
                self.player1hand.append(player1card)
                self.player1hand.append(player2card)
            elif player2card > player1card:
                if verbose:
                    print("Player 2 wins!")
                self.player2hand.append(player2card)
                self.player2hand.append(player1card)
            else:
                raise ValueError('Duplicate values found')
            n+=1
        if verbose:
            print("== Post Game results ==")
            print("Player 1's deck:",self.player1hand)
            print("Player 2's deck:",self.player2hand)

    @staticmethod
    def DetermineWinner(player1hand, player2hand,oldgamestates):
        '''Recursive combat game'''
        if (player1hand,player2hand) in oldgamestates:
            print("Previous Game state seen! Player 1 wins!")
            winner='p1'
        else:
            # each player plays a card from their hand
            player1card = player1hand.popleft()
            player2card = player2hand.popleft()
            if player1card <= len(player1hand) and player2card <= len(player2hand):
                # Both players have at least as many cards remaining in hand so play again
                print("Recursing....")
                winner = self.DetermineWinner(deepcopy(player1hand),deepcopy(player2hand),oldgamestates)
            else:
                # Winner is the highest card
                if player1card > player2card:
                    winner='p1'
                elif player2card > player1card:
                    winner='p2'
        return winner

    def score(self):
        ''' Return the score of both players.'''
        player1score, player2score =0,0
        n1,n2=1,1
        while len(self.player1hand) >0 :
            player1score+=self.player1hand.pop()*n1
            n1+=1
        while len(self.player2hand) >0 :
            player2score+=self.player2hand.pop()*n2
            n2+=1
        return player1score, player2score

# Part 2
class CombatGameP2:
    ''' A recursive version of the combat card game'''
    def __init__(self,inputfile):
        ''' read in input data and store hands as deques'''
        with open(inputfile) as f:
            playerhands = f.read().split('\n\n')
        self.player1hand=deque([int(i) for i in playerhands[0].split('\n')[1:]])
        self.player2hand=deque([int(i) for i in playerhands[1].split('\n')[1:]])

    def recursive_combat(self,player1hand, player2hand, verbose=False): 
        ''' play recursive combat according to the rules
        This is a recursive function.'''
        oldgamestates=[]
        n=0
        while len(player1hand) >0 and len(player2hand) >0:
            if verbose:
                print("-- Round",n,"--")
                print("Player 1's hand: ",player1hand)
                print("Player 2's hand: ",player2hand)

            if (list(player1hand), list(player2hand)) in oldgamestates:
                # if there was a previous round in this game that had exactly the same cards 
                #  in the same order in the same players' decks, the game instantly ends in 
                #  a win for player 1.
                if verbose:
                    print("Existing game state found!")
                    print((list(player1hand), list(player2hand)))
                    print(oldgamestates)
                    print("Ending game for Player 1")
                winner='p1'
                return winner, player1hand, player2hand
            else:
                oldgamestates.append((list(player1hand),list(player2hand)))
                # the players begin the round by each drawing the top card of their deck as normal.
                player1card=player1hand.popleft()
                player2card=player2hand.popleft()
                if verbose:
                    print("Player 1 draws:", player1card)
                    print("Player 2 draws:", player2card)
                # If both players have at least as many cards remaining in their deck as the value 
                #  of the card they just drew, the winner of the round is determined by playing a 
                #  new game of Recursive Combat. Note each player only keeps the number of cards
                #  on the card they played.
                if player1card <= len(player1hand) and player2card <= len(player2hand):
                    winner, _, _ = self.recursive_combat(\
                        deque(list(player1hand.copy())[:player1card]),\
                        deque(list(player2hand.copy())[:player2card]))
                elif player1card > player2card:
                    winner='p1'
                elif player2card > player1card:
                    winner='p2'
                else:
                    raise ValueError('Duplicate values found')
            if winner == 'p1':
                if verbose:
                    print("Player 1 wins!")
                player1hand.append(player1card)
                player1hand.append(player2card)
            elif winner =='p2':
                if verbose:
                    print("Player 2 wins!")
                player2hand.append(player2card)
                player2hand.append(player1card)
            else:
                raise ValueError('Unable to determine winner')
            n+=1
        if verbose:
            print("== Post Game results ==")
            print("Player 1's deck:",player1hand)
            print("Player 2's deck:",player2hand)

        return winner, player1hand, player2hand

    def score(self,player1score, player2score):
        ''' Return the score of both players.'''
        player1score, player2score =0,0
        n1,n2=1,1
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
    print(f'2201: Scores: Player1: {p1s}, Player2: {p2s}')

def day22_02():
    """Run part 2 of Day 22's code"""
    path = "tests/day22_testinput.txt"
    path = "./input/22/input.txt"
    mygame = CombatGameP2(path)
    winner, p1h, p2h = mygame.recursive_combat(mygame.player1hand,mygame.player2hand)
    result=max(mygame.score(p1h,p2h))
    print(f'2202: Winners score: {result}')

if __name__ == "__main__":
    day22_01()
    day22_02()

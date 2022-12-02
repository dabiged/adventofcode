from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


def score(hand):
    if hand == 'A':
        return 1
    if hand == 'B':
        return 2
    if hand == 'C':
        return 3
    if hand == 'X':
        return 1
    if hand == 'Y':
        return 2
    if hand == 'Z':
        return 3

'''
A Rock
B Paper
C Scissors
X Rock
Y Paper
Z Scissors
'''

def Game(P1,P2):
    if  (P1 == 'A' and P2 == 'X') or         (P1== 'B' and P2 == 'Y') or        (P1 == 'C' and P2 =='Z'):
        return (score(P1)+3,score(P2)+3)
    if P1 == 'A':
        if P2 == 'Z':
            return (6+score(P1),score(P2))
        if P2 == 'Y':
            return (score(P1),score(P2)+6)
    if P1 == 'B':
        if P2 == 'X':
            return (6+score(P1),score(P2))
        if P2 == 'Z':
            return (score(P1),score(P2)+6)
    if P1 == 'C':
        if P2 == 'X':
            return (score(P1),score(P2)+6)
        if P2 == 'Y':
            return (6+score(P1),score(P2))


def Game2(P1,Result):
    if Result == 'Y':
        # Draw
        if P1 == 'A':
            return 4
        if P1 == 'B':
            return 5
        if P1 == 'C':
            return 6
    if Result == 'X':
        if P1 == 'A':
            return 3
        if P1 == 'B':
            return 1
        if P1 == 'C':
            return 2
    if Result == 'Z':
        if P1 == 'A':
            return 8
        if P1 == 'B':
            return 9
        if P1 == 'C':
            return 7


def ManyGames(plays):
    P1,P2=(0,0)
    for agame in plays:
        hands=agame.split()
        up1,up2 = Game(hands[0],hands[1])
        P1+=up1
        P2+=up2
    return P2

def ManyGames2(plays):
    P1=0
    for agame in plays:
        hands=agame.split()
        up1 = Game2(hands[0],hands[1])
        P1+=up1
    return P1



def day02_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_02.txt"
    print("0201:",ManyGames(file_to_str_array(path)))


def day02_02():
    """Run part 2 of Day 1's code"""
    path = "./input/input_02.txt"
    print("0202:",ManyGames2(file_to_str_array(path)))

if __name__ == "__main__":
    day02_01()
    day02_02()

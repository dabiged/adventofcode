from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

test_input=[ 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green' ]

class Game():
    def __init__(self,gamestr, red=12, green=13, blue=14):
        self.red=red
        self.green=green
        self.blue=blue
        self.gameid=int(gamestr.split(':')[0].split()[-1])
        hands=gamestr.split(':')[-1]
        self.reveals=[]
        for reveal in hands.split(';'):
            thisreveal={}
            for numcolor in reveal.split(','):
                thisreveal[numcolor.split()[1]]=int(numcolor.split()[0])
            self.reveals.append(thisreveal)

    def valid(self):
        for reveal in self.reveals:
            if 'red' in reveal.keys():
                if reveal['red']>self.red:
                    return False
            if 'blue' in reveal.keys():
                if reveal['blue']>self.blue:
                    return False
            if 'green' in reveal.keys():
                if reveal['green']>self.green:
                    return False
        return True

    def power(self):
        mingreen, minred, minblue = 0, 0, 0 
        for reveal in self.reveals:
            if 'red' in reveal.keys():
                minred = max(reveal['red'],minred)
                    
            if 'blue' in reveal.keys():
                minblue = max(reveal['blue'],minblue)
            if 'green' in reveal.keys():
                mingreen = max(reveal['green'],mingreen)

        return minred*mingreen*minblue




def part1(inputdata=test_input):
    valid=0
    gameidsum=0
    for game in inputdata:
        thisgame=Game(game)
        if thisgame.valid():
            valid+=1
            gameidsum+=thisgame.gameid
    return gameidsum

def part2(inputdata=test_input):
    valid=0
    powersum=0
    for game in inputdata:
        thisgame=Game(game)
        powersum+=thisgame.power()

    return powersum


def day02_01():
    """Run part 1 of Day 1's code"""
    path = "./input/02.txt"
    print("0201:", part1(file_to_str_array(path)))


def day02_02():
    """Run part 2 of Day 1's code"""
    path = "./input/02.txt"
    print("0202:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day02_01()
    day02_02()

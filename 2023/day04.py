from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from collections import defaultdict

test_input=[
'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]

class ScratchCard():
    def __init__(self,data):
        self.data=data
        self.cardnum=-1
        self.winning=set()
        self.numbers=set()
        self.parse()

    def parse(self):
        card = self.data.split(':')
        nums = card[1].strip().split('|')
        self.cardnum=int(card[0].split()[-1])

        for num in nums[0].strip().split():
            self.winning.add(int(num))
        for num in nums[1].strip().split():
            self.numbers.add(int(num))

    def num_winners(self):
        num_winners=self.winning.intersection(self.numbers)
        return len(num_winners)

    def score(self):
        num_winners=self.winning.intersection(self.numbers)
        n=len(num_winners)
        return 2**(n-1) if n >0 else 0

    def __str__(self):
        return f'Card #{self.cardnum}\nWinning Numbers:{self.winning}\nNumbers:{self.numbers}'

def part1(inputdata=test_input):
    total=0
    for card_data in inputdata:
        sc=ScratchCard(card_data)
        total+=sc.score()

    return total

def part2(inputdata=test_input):
    copies=defaultdict(lambda: int(1))
    for card_data in inputdata:
        sc=ScratchCard(card_data)
        score=sc.num_winners()
        cardnum=sc.cardnum
        for i in range(cardnum,cardnum+score):
            copies[i+1]+=copies[cardnum]
    total=0
    for i in range(len(inputdata)):
        total+=copies[i+1]
    return total


def day04_01():
    """Run part 1 of Day 1's code"""
    path = "./input/04.txt"
    print("0401:", part1(file_to_str_array(path)))


def day04_02():
    """Run part 2 of Day 1's code"""
    path = "./input/04.txt"
    print("0402:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day04_01()
    day04_02()

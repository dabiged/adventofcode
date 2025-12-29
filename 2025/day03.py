from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
testdata='''987654321111111
811111111111119
234234234234278
818181911112111'''

testdata=testdata.split('\n')

def largest_joltage(bank: str, k: int):
    n = len(bank)
    pos = 0
    batteries = []
    for remaining in range(k, 0, -1):
        end = n - remaining + 1
        best_digit = max(bank[pos:end])
        pos = bank.index(best_digit, pos, end) + 1
        batteries.append(best_digit)
    return ''.join(batteries)

def part1(inputdata=testdata):
    total_joltage=0
    for line in inputdata:
        total_joltage+=int(largest_joltage(line,2))
    return total_joltage


def part2(inputdata=testdata):
    total_joltage=0
    for line in inputdata:
        total_joltage+=int(largest_joltage(line,12))
    return total_joltage

def day03_01():
    """Run part 1 of Day 03's code"""
    path = "./input/03.txt"
    print("0301:", part1(file_to_str_array(path)))


def day03_02():
    """Run part 2 of Day 03's code"""
    path = "./input/03.txt"
    print("0302:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day03_01()
    day03_02()

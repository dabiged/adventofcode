from lib.filehelper import get_bald_string_list_from_file
# pylint: disable=missing-module-docstring

test_input=''''''.split('\n')

class UnknownOperationError(Exception):
    pass

class Monkey():
    def __init__(self,items,operation,testmod,truemonkey,falsemonkey):
        self.items=items # list of ints
        self.operation=operation # like Operation: new = old + 6
        self.test=testmod  # int
        self.testtrue=truemonkey  # int
        self.testfalse=falsemonkey  # int
        self.inspecteditems=0

    def recieve(self,item):
        self.items.append(item)

    def run(self,allmonkeys,part1=True):
        listop=self.operation.split()
        op=listop[-2]
        value=listop[-1]
        for item in self.items:
            self.inspecteditems+=1
            if value == 'old':
                item=item * item
            elif op == '*':
                item=item * int(value)
            elif op == '+':
                item += int(value)
            else:
                raise UnknownOperationError
            if part1:
                item=item//3
            else:
                item=item % 9699690

            if item % self.test == 0:
                allmonkeys[self.testtrue].recieve(item)
            else:
                allmonkeys[self.testfalse].recieve(item)

        self.items=[]

    def  __repr__(self):
        return f'Monkey({self.items})'#, {self.operation}, {self.test} T:{self.testtrue} F:{self.testfalse})'


def MonkeyGame(data,part1=True):
    allmonkeys=[]
    monkeydefs=data.split('\n\n')
    for i,monkeydef in enumerate(monkeydefs):
        lines=monkeydef.split('\n')
        for line in lines:
            if line.startswith('  Starting items:'):
                items = list(map(int,line.strip().replace(',','').split()[2:]))
            elif line.startswith('  Operation:'):
                operation = " ".join(line.strip().split()[-2:])
            elif line.startswith('  Test: divisible by '):
                testmod=int(line.split()[-1])
            elif line.startswith('    If true: throw to monkey'):
                truemonkey=int(line.split()[-1])
            elif line.startswith('    If false: throw to monkey'):
                falsemonkey=int(line.split()[-1])
        allmonkeys.append(Monkey(items,operation,testmod,truemonkey,falsemonkey))

    numturns=20 if part1 else 10000

    for turn in range(numturns):
        for monkey in allmonkeys:
            monkey.run(allmonkeys,part1)

    inspected=[]
    for monkey in allmonkeys:
        inspected.append(monkey.inspecteditems)

    inspected.sort()
    return inspected[-2]*inspected[-1]


def main1(data):
    inputdata="".join(data)
    return MonkeyGame(inputdata,part1=True)

def main2(data):
    inputdata="".join(data)
    return MonkeyGame(inputdata,part1=False)

def day11_01():
    """Run part 1 of Day 11's code"""
    path = "./input/input_11.txt"
    print("1101:",main1(get_bald_string_list_from_file(path)))

def day11_02():
    """Run part 2 of Day 11's code"""
    path = "./input/input_11.txt"
    print("1102:",main2(get_bald_string_list_from_file(path)))

if __name__ == "__main__":
    day11_01()
    day11_02()

from day08 import node
from collections import defaultdict, deque

class TestDay08:
    def test_part1(self):
        testinput=deque([int (i) for i in '0 3 10 11 12'.split()])
        mynode=node(testinput)
        assert mynode.metadata == [10,11,12]
        assert mynode.children == []

    def test_part2(self):
        testinput=deque([int (i) for i in '1 1 0 1 99 2'.split()])
        mytree=node(testinput)
        print(mytree.metadata)
        assert True == False

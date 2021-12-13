from day11 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay11:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        testoct=node(0,0,0)
        assert len(testoct.neighbours()) == 3

    def test_02(self):
        testoct=node(5,5,0)
        assert len(testoct.neighbours()) == 8

#    def test_03(self):
#        inputfile='tests/input_day11.txt'
#        testGrid=Grid(inputfile)
#        result=testGrid.part1()
#        assert result == 1656
#
#    def test_04(self):
#        inputfile='tests/input_day11.txt'
#        testGrid=Grid(inputfile)
#        result=testGrid.part2()
#        assert result == 1656
#

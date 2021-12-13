from day13 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay13:
    # pylint: disable=missing-module-docstring
    def test_import(self):
        inputfile='tests/input_day13.txt'
        testboard=Board(inputfile)
        print(testboard.folds)
        print(testboard)
        assert testboard.maxx == 10
        assert testboard.maxy == 14

    def test_part1(self):
        inputfile='tests/input_day13.txt'
        testboard=Board(inputfile)
        result=testboard.part1()
        assert result == 17

    def test_part2(self):
        inputfile='tests/input_day13.txt'
        testboard=Board(inputfile)
        result=testboard.part2()

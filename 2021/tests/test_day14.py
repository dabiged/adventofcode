from day14 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay14:
    # pylint: disable=missing-module-docstring
    def test_import(self):
        inputfile='tests/input_day14.txt'
        testPolymer=Polymer(inputfile)
        result=testPolymer.part1()
        assert result == 1588

    def test_part2(self):
        inputfile='tests/input_day14.txt'
        testPolymer=Polymer(inputfile)
        result=testPolymer.part2()
        assert result == 2188189693529

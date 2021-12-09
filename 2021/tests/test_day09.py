from day09 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay09:
    # pylint: disable=missing-module-docstring
    def test_02(self):
        inputfile = "./tests/input_day09.txt"
        testmap=Map(inputfile)
        testmap.process_inputfile()
        result=testmap.get_risk()
        assert result == 15

    def test_02(self):
        inputfile = "./tests/input_day09.txt"
        testmap=Map(inputfile)
        testmap.process_inputfile()
        result=testmap.explore_all_basins()
        result=testmap.part2()
        assert result == 1134


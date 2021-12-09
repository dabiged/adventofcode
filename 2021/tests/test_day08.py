from day08 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay08:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputfile = "./tests/input_day08.txt"
        testdecode=SevenSegDecoder(inputfile)
        result=testdecode.part1()
        assert result == 26


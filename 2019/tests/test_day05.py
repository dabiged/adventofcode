from day04 import IntCodeComputer
from lib.filehelper import file_to_str_array
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay05:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputfile='tests/input_day02.txt'
        myIntcode=IntCodeComputer(inputfile,debug=True)
        myIntcode.program=[1002,4,3,4,33]
        myIntcode.run()
        result=myIntcode.result()
        assert 3500 == result

    def test_05(self):
        pass

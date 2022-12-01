from day02 import IntCodeComputer
from lib.filehelper import file_to_str_array
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay02:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputfile='tests/input_day02.txt'
        myIntcode=IntCodeComputer(inputfile,debug=True)
        result=myIntcode.result()
        assert 3500 == result

    def test_02(self):
        pass

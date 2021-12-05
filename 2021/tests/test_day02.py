from day02 import final_position,final_position2
from lib.filehelper import file_to_str_array
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay02:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputlist=file_to_str_array('tests/input_day02.txt')
        result=final_position(inputlist)
        expected = 150
        assert expected == result

    def test_02(self):
        inputlist=file_to_str_array('tests/input_day02.txt')
        result=final_position2(inputlist)
        expected = 900
        assert expected == result

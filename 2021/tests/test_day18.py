from day01 import gt_previous,gt_previous_smoothed
from lib.filehelper import file_to_array
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay01:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        testlist=file_to_array('tests/input_day01.txt')
        result=gt_previous(testlist)
        expected = 7
        assert expected == result

    def test_02(self):
        testlist=file_to_array('tests/input_day01.txt')
        result=gt_previous_smoothed(testlist)
        expected = 5
        assert expected == result

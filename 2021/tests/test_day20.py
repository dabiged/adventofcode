from day20 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay20:
    # pylint: disable=missing-module-docstring
    def test_demo(self):
        myImage=Image('tests/input_day20.txt')
        print(myImage.enhance())
        print(myImage.enhance())
        result=myImage.countlit()
        assert result == 35
        assert True==False

    def test_helpers(self):
        assert bin2dec(sym2bin('...#...#.')) == 34

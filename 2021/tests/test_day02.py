from day02 import day02_01,day02_02
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay02:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        result=day02_01(['forward 5','down 5','forward 8','up 3','down 8','forward 2'])
        expected = 150
        assert expected == result

    def test_02(self):
        result=day02_02(['forward 5','down 5','forward 8','up 3','down 8','forward 2'])
        expected = 900
        assert expected == result

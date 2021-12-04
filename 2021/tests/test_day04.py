from day04 import day04_01,day04_02
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay04:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        result=day04_01('tests/input_day04.txt')
        expected = (3, 4512)
        assert expected == result

    def test_02(self):
        result=day04_02('tests/input_day04.txt')
        expected = (2,1924)
        assert expected == result

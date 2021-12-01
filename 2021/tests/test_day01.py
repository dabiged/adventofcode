from day01 import day01_01,day01_02
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay01:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        result=day01_01([199,200,208,210,200,207,240,269,260,263])
        expected = 7
        assert expected == result

    def test_02(self):
        result=day01_02([199,200,208,210,200,207,240,269,260,263])
        expected = 5
        assert expected == result

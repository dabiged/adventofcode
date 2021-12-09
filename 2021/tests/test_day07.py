from day07 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay07:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputfile = "./tests/input_day07.txt"
        testfuelcalc=FuelCalc(inputfile)
        testfuelcalc.run()
        position,cost=testfuelcalc.get_best_position()

        assert position == 2
        assert cost == 37

    def test_02(self):
        inputfile = "./tests/input_day07.txt"
        testfuelcalc=FuelCalc(inputfile)
        testfuelcalc.run2()
        position,cost=testfuelcalc.get_best_position()

        assert position==  5
        assert cost == 168


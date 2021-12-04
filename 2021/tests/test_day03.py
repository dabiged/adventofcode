from day03 import day03_01,day03_02,DiagnosticReport
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay02:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        testinput="tests/input_day03.txt"
        testreport=DiagnosticReport(testinput)
        O2 = testreport.O2_rating()
        assert O2 == "10111"


    def test_02(self):
        testinput="tests/input_day03.txt"
        testreport=DiagnosticReport(testinput)
        testreport.O2_rating()
        CO2 = testreport.CO2_rating()
        assert CO2 == "01010"

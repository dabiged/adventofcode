from day01 import calc_most_cal, calc_top3_cal

TestInput=["1000","2000","3000","","4000","","5000","6000","","7000","8000","9000","","10000",""]

class TestDay01:
    def test_most_cal(self):
        assert 24000 == calc_most_cal(TestInput)

    def test_top3_cal(self):
        assert 45000 == calc_top3_cal(TestInput)

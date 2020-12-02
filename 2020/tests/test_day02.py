
from day02 import isvalidpw, ismorevalidpw


class TestDay01:
    def test_isvalidpw_False(self):
        expected = False
        inputtotest = "15-16 l: ksadfsadfsadfsadfll"
        result = isvalidpw(inputtotest)
        assert expected == result

    def test_ismorevalidpw_False(self):
        expected = False
        inputtotest = "15-16 l: ksadfsadfsadfsadfll"
        result = isvalidpw(inputtotest)
        assert expected == result

    def test_isvalidpw_True(self):
        expected = True
        inputtotest = "1-2 l: ksadfsadfsadfsadfll"
        result = isvalidpw(inputtotest)
        assert expected == result

    def test_ismorevalidpw_True(self):
        expected = True
        inputtotest = "1-10 l: lsadfsadfsadfsadfll"
        result = isvalidpw(inputtotest)
        assert expected == result

from day17 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay17:
    # pylint: disable=missing-module-docstring
    def test_demo(self):
        myshot=TrickShot(20,30,-10,-5)
        result=myshot.find_highest(10,10)
        assert result == 45

    # pylint: disable=missing-module-docstring
    def test_directshot(self):
        myshot=TrickShot(20,30,-10,-5)
        result=myshot.shoot(20,-10)
        assert (True, 0) == result

    def test_findall(self):
        myshot=TrickShot(20,30,-10,-5)
        result=myshot.find_all()
        assert 112 == result

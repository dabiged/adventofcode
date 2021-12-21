from day21 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay21:
    # pylint: disable=missing-module-docstring
    def test_demo(self):
        mygame=DiceGame(4,8)
        result=mygame.play()
        assert result==739785

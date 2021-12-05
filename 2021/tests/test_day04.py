from day04 import BingoGame
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay04:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputfile = "./tests/input_day04.txt"
        testgame=BingoGame(inputfile)
        result = testgame.playgame()
        expected = (3, 4512)
        assert expected == result

    def test_02(self):
        inputfile = "./tests/input_day04.txt"
        testgame=BingoGame(inputfile)
        result = testgame.get_worst()
        expected = (2,1924)
        assert expected == result

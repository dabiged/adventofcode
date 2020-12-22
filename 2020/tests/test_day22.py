from day22 import CombatGame

class TestDay22:
    def test_play(self):
        inputfile='tests/day22_testinput.txt'
        mygame= CombatGame(inputfile)
        mygame.play()
        p1s, p2s = mygame.score()
        assert p1s == 0
        assert p2s == 306

from day22 import CombatGame, CombatGameP2

class TestDay22:
    def test_play(self):
        inputfile='tests/day22_testinput.txt'
        mygame= CombatGame(inputfile)
        mygame.play()
        p1s, p2s = mygame.score()
        assert p1s == 0
        assert p2s == 306

    def test_recursive(self):
        inputfile='tests/day22_testinput.txt'
        mygame = CombatGameP2(inputfile)
        winner, p1h, p2h = mygame.recursive_combat(mygame.player1hand,mygame.player2hand)
        score = max(mygame.score(p1h, p2h))
        assert score == 291

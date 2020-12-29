from day23 import CrabCups


class TestDay23:
    def test_init(self):
        mygame = CrabCups('389125467')

    def test_pickup(self):
        mygame = CrabCups('389125467')
        hand=mygame.pickup(3)
        print(hand)


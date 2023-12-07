from day06 import Boat, BoatRacer

test_input=[
'Time:      7  15   30',
'Distance:  9  40  200'
]

class TestDay06:
    def test_boat1(self):
        myboat=Boat(9,7)
        assert myboat.winners() == 4
    
    def test_BoatRacer(self):
        myboatracers=BoatRacer(test_input)
        assert myboatracers.count_winners() == 288

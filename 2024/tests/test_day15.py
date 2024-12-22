from day15 import Warehouse,Grid


input_data1='''#######
#...O..
#......'''



class TestDay12:
    def test_score(self):
        g=Grid(input_data1.split('\n'))
        ans=g.score()
        assert ans == 104


from day06 import Board
from lib.filehelper import file_to_str_array

class TestDay06:
    def test_init_print(self):
        testinput=["350, 353", "238, 298"]
        testboard=Board(testinput)
        #assert testboard.sources == [(350,353),(238,298)]
        assert testboard.source_row_max() == 350
        assert testboard.source_row_min() == 238
        assert testboard.source_col_max() == 353
        assert testboard.source_col_min() == 298
        assert testboard.board_size == 354

#    def test_display_sources(self):
#        expected='..........\n.A........\n..........\n........C.\n...D......\n.....E....\n.B........\n..........\n..........\n........F.\n'
#        testinput=["1, 1", "1, 6", "8, 3","3, 4","5, 5","8, 9"]
#        testboard=Board(testinput)
#        print(testboard)
#        print(expected)
#        assert expected == str(testboard)
#
#    def test_calc_influence(self):
#        expected='aaaaa.cccc\naAaaa.cccc\naaaddecccc\naadddeccCc\n..dDdeeccc\nbb.deEeecc\nbBb.eeee..\nbbb.eeefff\nbbb.eeffff\nbbb.ffffFf\n'
#        testinput=["1, 1", "1, 6", "8, 3","3, 4","5, 5","8, 9"]
#        testboard=Board(testinput)
#        print(testboard)
#        testboard.calc_influence()
#        print(testboard)
#        print(expected)
#        assert expected == str(testboard)
#
#    def test_compute_largest_finite(self):
#        expected = (17, 'E')
#        testinput=["1, 1", "1, 6", "8, 3","3, 4","5, 5","8, 9"]
#        testboard=Board(testinput)
#        testboard.calc_influence()
#        result=testboard.count_highest_finite()
#        assert expected == result

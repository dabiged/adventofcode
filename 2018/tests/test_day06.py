from day06 import Board
from lib.filehelper import file_to_str_array

class TestDay06:
    def test_init_print(self):
        testinput=["350, 353", "238, 298"]
        testboard=Board(testinput)
        #assert testboard.sources == [(350,353),(238,298)]
        assert testboard.source_col_max() == 350
        assert testboard.source_col_min() == 238
        assert testboard.source_row_max() == 353
        assert testboard.source_row_min() == 298

    def test_display_sources(self):
        testinput=["1, 1", "1, 6", "8, 3","3, 4","5, 5","8, 9"]
        testboard=Board(testinput)
        print(testboard)
        assert True == False


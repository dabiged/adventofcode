from day20 import ImageTiler, Tile
from lib.filehelper import file_to_str_array


class TestDay20:
    def test_build_tile(self):
        inputdata=['abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890']
        testtile=Tile(inputdata)
        print(testtile)
        testtile.rotate()
        print(testtile)
        testtile.rotate()
        print(testtile)
        testtile.rotate()
        print(testtile)
        testtile.rotate()
        print(testtile)
        assert True == False



    def test_build_real_tile(self):
        pass

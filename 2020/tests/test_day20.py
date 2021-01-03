from day20 import ImageTiler, Tile
from lib.filehelper import file_to_str_array


class TestDay20:
    def test_build_tile(self):
        inputdata=['abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890']
        testtile=Tile(1234, inputdata, verbose=True)
        assert 'abcdefghij' in testtile.borders
        assert '1234567890' in testtile.borders
        assert 'j0j0j0j0j0' in testtile.borders
        assert 'a1a1a1a1a1' in testtile.borders
        assert 'jihgfedcba' in testtile.borders
        assert '0987654321' in testtile.borders
        assert '0j0j0j0j0j' in testtile.borders
        assert '1a1a1a1a1a' in testtile.borders

    def test_tile_pair(self):
        inputdata1=['abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890','abcdefghij','1234567890']
        inputdata2=['zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','abcdefghij']
        testtile1=Tile(1234, inputdata1, verbose=True)
        testtile2=Tile(3141, inputdata2, verbose=True)
        testtile1.pair(testtile2)
        testtile2.pair(testtile1)
        assert 3141 in testtile1.pairs
        assert 1234 in testtile2.pairs

#    def test_tile_rotate(self):
#        inputdata2=['zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','abcdefghij']
#        testtile2=Tile(3141, inputdata2, verbose=True)
#        testtile2.rotate()
#        testtile2.rotate()
#        assert testtile2.tile[0] == 'jihgfedcba'

    def test_tile_flip(self):
        inputdata2=['zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','zzzzzzzzzz','abcdefghij']
        testtile2=Tile(3141, inputdata2, verbose=True)
        testtile2.flip()
        print(testtile2)


    def test_tile_product_of_corners(self):
        inputdata='tests/day20_testinput.txt'
        testtiler = ImageTiler(file_to_str_array(inputdata))
        print(testtiler.tiles)
        testtiler.pair_tiles()
        result = testtiler.product_of_corners()
        assert result == 20899048083289

    def test_find_monster(self):
        inputdata=['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']
        testtile=Tile(1234, inputdata)
        result = testtile.find_monsters()
        assert result == 1

    def test_find_2_monsters(self):
        inputdata=['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ','                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']
        testtile=Tile(1234, inputdata)
        result = testtile.find_monsters()
        assert result == 2

    def test_find_2_monsters2(self):
        inputdata=['                  #                   # ','#    ##    ##    ####    ##    ##    ###',' #  #  #  #  #  #    #  #  #  #  #  #   ']
        testtile=Tile(1234, inputdata)
        result = testtile.find_monsters()
        assert result == 2




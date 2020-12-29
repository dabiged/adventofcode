from day24 import HexBoard


class TestDay24:
    def test_parseInstr(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        assert myhex.instructions[2]==['se','sw','ne','sw','sw','se','nw','w','nw','se']

    def test_movearound_basic(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        west=myhex.west((0,0))
        origin=myhex.east(west)
        assert origin == (0,0)
        west=myhex.west((0,0))
        sw=myhex.southeast(west)
        se=myhex.east(sw)
        w=myhex.northeast(se)
        nw=myhex.northwest(w)
        ne=myhex.west(nw)
        origin=myhex.southeast(ne)
        assert origin == (0,0)

    def test_locate_tile(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        myhex.instructions[0]=['w','se','e','ne','nw','w','se']
        result = myhex.locate_tile(myhex.instructions[0])
        assert result == (0,0)

    def test_example1(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        myhex.setup()
        myhex.step()
        result = myhex.count_black_tiles()
        assert result == 15
        myhex.step()
        result = myhex.count_black_tiles()
        assert result == 12
        myhex.step()
        result = myhex.count_black_tiles()
        assert result == 25

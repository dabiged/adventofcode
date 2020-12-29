from day24 import HexBoard


class TestDay24:
    def test_parseInstr(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        assert myhex.instructions[2]==['se','sw','ne','sw','sw','se','nw','w','nw','se']

    def test_movearound(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        west=myhex.west((0,0))
        origin=myhex.east(west)
        assert origin == (0,0)
        sw=myhex.southeast(west)
        se=myhex.east(sw)
        w=myhex.northeast(se)
        nw=myhex.northwest(w)
        ne=myhex.west(nw)
        origin=myhex.southwest(ne)
        assert origin == (0,0)

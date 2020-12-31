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

    def test_small_loop1(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        myhex.instructions[0]=['nw','ne']
        result = myhex.locate_tile(myhex.instructions[0])
        assert result == (2,0)

    def test_example1_setup(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        myhex.setup()
        result = myhex.count_black_tiles()
        assert result == 10
        expected=[(0,0),(1,-1),(1,-2),(0,-2),(-1,-2),(-2,-2),(-3,-2),(-2,1),(0,2),(3,1)]
        for testhex in expected:
            assert testhex in myhex.board

    def test_example1_part2(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        myhex.setup()
        results=[15,12,25,14,23,28,41,37,49,37]
        for num in range(10):
            myhex.step()
            print(str(myhex))
            print(num)
            assert myhex.count_black_tiles() == results[num]

    def test_example1_part2a(self):
        inputdata='tests/day24_testinput.txt'
        myhex = HexBoard(inputdata)
        myhex.setup()
        results=[37,132,259,406,566,788,1106,1373,1844,2208]
        for num in range(10):
            for _ in range(10):
                myhex.step()
            print(str(myhex))
            print(num*10)
            assert myhex.count_black_tiles() == results[num]





from day03 import build_empty_grid, read_cut, build_grid, print_fabric


class TestDay03:
    def test_build_2x2_grid(self):
        expected = [[".","."],[".","."]]
        result = build_empty_grid(xsize=2, ysize=2)
        assert expected == result

    def test_build_1x1_grid(self):
        expected = [["."]]
        result = build_empty_grid(xsize=1, ysize=1)
        assert expected == result

    def test_build_5x1_grid(self):
        expected = [[".",".",".",".","."]]
        result = build_empty_grid(xsize=5, ysize=1)
        assert expected == result

    def test_read_cuts1(self):
        expected = (1207, 41, 225, 15, 27)
        testinput= "#1207 @ 41,225: 15x27"
        result = read_cut(testinput)
        assert expected == result

    def test_read_cuts2(self):
        expected = (6, 20, 696, 19, 12)
        testinput= "#6 @ 20,696: 19x12"
        result = read_cut(testinput)
        assert expected == result

    def test_build_1cut_grid(self):
        expected = [["1"]]
        testinput= ["#1 @ 0,0: 1x1"]
        result = build_grid(testinput, xsize=1,ysize=1)
        assert expected == result

    def test_build_example1_grid(self):
        expected = [
        [".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".","1","1","1","1","1",".",".","."],
        [".",".",".","1","1","1","1","1",".",".","."],
        [".",".",".","1","1","1","1","1",".",".","."],
        [".",".",".","1","1","1","1","1",".",".","."],
        [".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".",".","."]]
        testinput= ["#1 @ 3,2: 5x4"]
        result = build_grid(testinput, xsize=11,ysize=9)
        print_fabric(expected)
        print(" ------------------- ")
        print_fabric(result)
        assert len(expected) == len(result)
        assert len(expected[0]) == len(result[0])
        assert expected == result


    def test_build_example2_grid(self):
        expected = [
        [".",".",".",".",".",".",".","."],
        [".",".",".","2","2","2","2","."],
        [".",".",".","2","2","2","2","."],
        [".","1","1","X","X","2","2","."],
        [".","1","1","X","X","2","2","."],
        [".","1","1","1","1","3","3","."],
        [".","1","1","1","1","3","3","."],
        [".",".",".",".",".",".",".","."]]
        testinput= ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]
        result = build_grid(testinput, xsize=8,ysize=8)
        print_fabric(expected)
        print(" ------------------- ")
        print_fabric(result)
        assert expected == result

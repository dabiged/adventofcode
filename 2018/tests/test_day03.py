from day03 import FabricSquare, read_cut


class TestDay03:
    def test_build_2x2_grid(self):
        expected = '..\n..\n'
        result = str(FabricSquare(rows=2, cols=2))
        assert expected == result

    def test_build_10x1_grid(self):
        expected = '.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n'
        result = str(FabricSquare(rows=10, cols=1))
        assert expected == result

    def test_build_1x10_grid(self):
        expected = '..........\n'
        result = str(FabricSquare(rows=1, cols=10))
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
        expected = '1\n'
        testinput= "#1 @ 0,0: 1x1"
        testsquare=FabricSquare(rows=1, cols=1)
        testsquare.addcut(testinput)
        result = str(testsquare)
        assert expected == result

    def test_example1_grid(self):
        expected = '...........\n...........\n...11111...\n...11111...\n...11111...\n...11111...\n...........\n...........\n...........\n'
        testinput= "#1 @ 3,2: 5x4"
        testsquare=FabricSquare(rows=9, cols=11)
        testsquare.addcut(testinput)
        result = str(testsquare)
        assert expected == result

    def test_example2_grid(self):
        expected = '........\n...2222.\n...2222.\n.11XX22.\n.11XX22.\n.111133.\n.111133.\n........\n'
        testinput= ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]
        testsquare=FabricSquare(rows=8, cols=8)
        for cut in testinput:
            testsquare.addcut(cut)
        result = str(testsquare)
        assert expected == result

    def test_shape(self):
        expected = (4, 5)
        testsquare = FabricSquare(rows=4, cols=5)
        result = testsquare.shape()
        assert expected == result

    def test_overlaps(self):
        expected = 4
        testinput= ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]
        testsquare=FabricSquare(rows=8, cols=8)
        for cut in testinput:
            testsquare.addcut(cut)
        result = testsquare.overlaps()
        assert expected == result

    def test_summary(self):
        expected = {'.':32,'1':12,'2':12,'3': 4 ,'X': 4}
        testinput= ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]
        testsquare=FabricSquare(rows=8, cols=8)
        for cut in testinput:
            testsquare.addcut(cut)
        testsquare.summarise()
        result = testsquare.getsummary()
        assert expected == result

    def test_nooverlaps(self):
        expected = '#3'
        testinput= ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]
        testsquare=FabricSquare(rows=8, cols=8)
        for cut in testinput:
            testsquare.addcut(cut)
        testsquare.summarise()
        for cut in testinput:
            if testsquare.nooverlap(cut):
                result= cut.split()[0]
        assert expected == result

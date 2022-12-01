from day15 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay15:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        testoct=Node(0,0,0,3,3)
        assert len(testoct.neighbours()) == 2

    def test_02(self):
        testoct=Node(5,5,0,10,10)
        assert len(testoct.neighbours()) == 4

    def test_03(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile()
        result=testGrid.calc_paths((9,9))
        assert result==40

    def test_04(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((1,0))
        assert result == 1


    def test_05(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((2,0))
        assert result == 3

    def test_06(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((3,0))
        assert result == 6

    def test_07(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((4,0))
        assert result == 13

    def test_08(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((5,0))
        assert result == 14

    def test_09(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((6,0))
        assert result == 15

    def test_10(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((7,0))
        assert result == 18

    def test_11(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((8,0))
        assert result == 19

    def test_12(self):
        inputfile='tests/input_day15.txt'
        testGrid=Grid(inputfile)
        testGrid.processinputfile2()
        print(testGrid)
        result=testGrid.calc_paths((9,0))
        assert result == 21

#    def test_13(self):
#        inputfile='tests/input_day15.txt'
#        testGrid=Grid(inputfile)
#        testGrid.processinputfile2()
#        print(testGrid)
#        result=testGrid.calc_paths((49,49))
#        assert result == 315


from day12 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay12:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputfile='tests/input_day12.txt'
        myGraph=Graph(inputfile)
        myGraph.traverse()
        assert len(myGraph.validjourneys) == 10

    def test_02(self):
        inputfile='tests/input_day12a.txt'
        myGraph=Graph(inputfile)
        myGraph.traverse()
        assert len(myGraph.validjourneys) == 19

    def test_03(self):
        inputfile='tests/input_day12b.txt'
        myGraph=Graph(inputfile)
        myGraph.traverse()
        assert len(myGraph.validjourneys) == 226

#    def test_04(self):
#        inputfile='tests/input_day12.txt'
#        myGraph=Graph(inputfile)
#        myGraph.retraverse()
#        assert len(myGraph.validjourneys) == 36
#    def test_05(self):
#        inputfile='tests/input_day12a.txt'
#        myGraph=Graph(inputfile)
#        myGraph.retraverse()
#        assert len(myGraph.validjourneys) == 103
#
#    def test_06(self):
#        inputfile='tests/input_day12b.txt'
#        myGraph=Graph(inputfile)
#        myGraph.retraverse()
#        assert len(myGraph.validjourneys) == 3509

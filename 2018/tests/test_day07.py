from day07 import WorkGraph

class TestDay07:
    def test_part1(self):
        expected = 'CABDFE'
        testGraph=WorkGraph('tests/day07_testinput.txt')
        testGraph.calc_part1()
        result=testGraph.StepsTaken
        assert expected == result
#    def test_part2(self):
#        expected = 'CABFDE'
#        testGraph=WorkGraph('tests/day07_testinput.txt',numworkers=2)
#        testGraph.calc_part2()
#        result=testGraph.StepsTaken
#        assert expected == result
#

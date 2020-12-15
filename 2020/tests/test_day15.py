from day15 import MemoryGame


class TestDay15:
    def test_run_example1(self):
        expected = 0
        testgame=MemoryGame('0,3,6')
        result=testgame.run(10)
        print(testgame.spoken)
        assert expected == result

    def test_run_example2(self):
        expected = 436
        testgame=MemoryGame('0,3,6')
        result=testgame.run(2020)
        print(testgame.spoken)
        assert expected == result

    def test_run_example3(self):
        expected = 1836
        testgame=MemoryGame('3,1,2')
        result=testgame.run(2020)
        print(testgame.spoken)
        assert expected == result

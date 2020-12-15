from day15 import MemoryGame


class TestDay15:
    def test_example1(self):
        expected = 3
        testgame=MemoryGame('0,3,6')
        testgame.taketurn(testgame.spoken[-1])
        testgame.taketurn(testgame.spoken[-1])
        result= testgame.spoken[-1]
        assert expected == result

    def test_step_example1(self):
        expected = [0,3,6,0,3,3,1,0,4,0]
        testgame=MemoryGame('0,3,6')
        for _ in range(0,7):
            testgame.taketurn(testgame.spoken[-1])
            print(testgame.spoken )
        result= testgame.spoken
        assert expected == result

    def test_run_example1(self):
        expected = [0,3,6,0,3,3,1,0,4,0]
        testgame=MemoryGame('0,3,6')
        testgame.run(numruns=10)
        result=testgame.spoken
        assert expected == result

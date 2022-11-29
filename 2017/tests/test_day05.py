from day05 import Computer


class TestDay05:
    def test_example(self):
        myComputer=Computer("0 3 0 1 -3".split())
        assert 5 == myComputer.run()

    def test_example2(self):
        myComputer=Computer("0 3 0 1 -3".split())
        assert 10 == myComputer.newrun()

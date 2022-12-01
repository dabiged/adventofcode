from day06 import Memory

class TestDay06:
    def test_memory1(self):
        mymem=Memory(["0","2","7","0"])
        assert mymem.get_maxloc() == 2

    def test_memory2(self):
        mymem=Memory(["0","2","7","0"])
        assert 5 == mymem.process()

    def test_memory2(self):
        mymem=Memory(["0","2","7","0"])
        mymem.process()
        assert 4 == mymem.len_cycle()



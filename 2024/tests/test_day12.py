from day12 import Region


class TestDay12:
    def test_single(self):
        r=Region('a')
        r.add(1+1j)
        ans=r.score2()
        assert ans == 4

    def test_two(self):
        r=Region('a')
        r.add(1+1j)
        r.add(1+2j)
        ans=r.score2()
        assert ans == 8

    def test_donut(self):
        r=Region('a')
        r.add(1+1j)
        r.add(1+2j)
        r.add(1+3j)
        r.add(2+3j)
        r.add(3+3j)
        r.add(3+2j)
        r.add(3+1j)
        r.add(2+1j)
        ans=r.score2()
        assert ans == 64


    def test_fivebyfivesquare(self):
        r=Region('a')
        r.add(1+1j)
        r.add(2+1j)
        r.add(3+1j)
        r.add(4+1j)
        r.add(5+1j)
        r.add(1+2j)
        r.add(2+2j)
        r.add(3+2j)
        r.add(4+2j)
        r.add(5+2j)
        r.add(1+3j)
        r.add(2+3j)
        r.add(3+3j)
        r.add(4+3j)
        r.add(5+3j)
        r.add(1+4j)
        r.add(2+4j)
        r.add(3+4j)
        r.add(4+4j)
        r.add(5+4j)
        r.add(1+5j)
        r.add(2+5j)
        r.add(3+5j)
        r.add(4+5j)
        r.add(5+5j)
        ans=r.score2()
        assert ans == 100


    def test_fivebyfivesquare_notch(self):
        r=Region('a')
        r.add(1+1j)
        r.add(2+1j)
        r.add(3+1j)
        #r.add(4+1j)
        #r.add(5+1j)
        r.add(1+2j)
        r.add(2+2j)
        r.add(3+2j)
        #r.add(4+2j)
        #r.add(5+2j)
        r.add(1+3j)
        r.add(2+3j)
        #r.add(3+3j)
        r.add(4+3j)
        r.add(5+3j)
        r.add(1+4j)
        r.add(2+4j)
        r.add(3+4j)
        r.add(4+4j)
        r.add(5+4j)
        r.add(1+5j)
        r.add(2+5j)
        r.add(3+5j)
        r.add(4+5j)
        r.add(5+5j)
        ans=r.score2()
        assert ans == 200











from day07 import Hand, WildHand


class TestDay07:
    def test_score(self):
        myh=Hand('23456')
        assert myh.cardscore() == '0001020304'

    def test_score1(self):
        myh=Hand('TJQKA')
        assert myh.cardscore() == '0809101112'

    def test_fiveofkind(self):
        myh=Hand('KKKKK')
        assert myh.score() == '61111111111'

    def test_fourofkind(self):
        myh=Hand('2222T')
        assert myh.score() == '50000000008'

    def test_fullhouse(self):
        myh=Hand('333QQ')
        assert myh.score() == '40101011010'

    def test_triple(self):
        myh=Hand('3332Q')
        assert myh.score() == '30101010010'

    def test_twopair(self):
        myh=Hand('3322Q')
        assert myh.score() == '20101000010'

    def test_pair(self):
        myh=Hand('3342Q')
        assert myh.score() == '10101020010'

    def test_nothing(self):
        myh=Hand('5342Q')
        assert myh.score() == '0301020010'

    def test_wild1(self):
        myh=WildHand('T55J5')
        assert myh.wildscore() == '50904040004'

    def test_wild2(self):
        myh=WildHand('KTJJT')
        assert myh.wildscore() == '51109000009'

    def test_wild3(self):
        myh=WildHand('QQQJA')
        assert myh.wildscore() == '51010100012'

    def test_wild4(self):
        myh=WildHand('JJJJJ')
        assert myh.wildscore() == '60000000000'

    def test_wildpair(self):
        myh=WildHand('KAJ32')
        assert myh.wildscore() == '11112000201'



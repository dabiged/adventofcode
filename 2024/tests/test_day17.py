from day17 import Computer



class TestDay17:
    def test_Computer1(self):
        m=Computer(0,0,9,'2,6')
        m.run()
        assert m.RegisterB == 1
    def test_Computer2(self):
        m=Computer(10,0,0,'5,0,5,1,5,4')
        output=m.run()
        assert output == '0,1,2'
    def test_Computer3(self):
        m=Computer(2024,0,0,'0,1,5,4,3,0')
        output=m.run()
        assert output == '4,2,5,6,7,7,7,7,3,1,0'
        assert m.RegisterA == 0
    def test_Computer4(self):
        m=Computer(0,29,0,'1,7')
        output=m.run()
        assert m.RegisterB==26
    def test_Computer5(self):
        m=Computer(0,2024,43690,'4,0')
        output=m.run()
        assert m.RegisterB == 44354


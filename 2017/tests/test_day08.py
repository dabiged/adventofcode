from day08 import Computer

testinput='''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''.split('\n')

class TestDay08:
    def test_memory1(self):
        mycomp=Computer(testinput)
        result=mycomp.run()
        assert mycomp.registers['b'] == 0
        assert mycomp.registers['a'] == 1
        assert mycomp.registers['c'] == -10
        assert result == 1

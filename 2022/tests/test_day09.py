from day09 import RopeBoard

Test_input='''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split('\n')

class TestDay09:
    def test_part1(self):
        r=RopeBoard(Test_input)
        r.step('U 1')
        assert r.rope[0] == 0+1j
        assert r.rope[-1] == 0+0j
        r.step('U 1')
        assert r.rope[0] == 0+2j
        assert r.rope[-1] == 0+1j
        r.step('L 1')
        assert r.rope[0] == -1+2j
        assert r.rope[-1] == 0+1j
        b=RopeBoard(Test_input)
        assert 13 == b.run()

    def test_part2(self):
        assert True == True




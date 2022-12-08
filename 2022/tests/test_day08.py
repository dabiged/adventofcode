from day08 import Forest

Test_input='''30373
25512
65332
33549
35390'''.split('\n')

class TestDay08:
    def test_part1(self):
        f=Forest(Test_input)
        f.parse()
        assert f.heightmap[(0,0)]==3
        assert f.heightmap[(4,4)]==0
        f.calc_visible()
        print(f.visible)
        assert f.count_visible() == 21



    def test_part2(self):
        f=Forest(Test_input)
        f.parse()
        assert 5 == f.heightmap[(3,2)]
        assert 2 == f.count_up((3,2))
        assert 2 == f.count_left((3,2))
        assert 1 == f.count_down((3,2))
        assert 2 == f.count_right((3,2))
        assert f.calc_scenic() == 8




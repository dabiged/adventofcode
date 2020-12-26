from day25 import transform, find_loop_size


class TestDay25:
    def test_transform_example(self):
        expected = 5764801
        result = transform(7,8)
        assert expected == result

    def test_transform_example2(self):
        expected = 17807724
        result = transform(7,11)
        assert expected == result

    def test_transform_example3(self):
        expected = 14897079
        result1 = transform(17807724,8)
        result2 = transform(5764801,11)
        assert expected == result1
        assert expected == result2

    def test_find_loopsize1(self):
        expected = 8
        result = find_loop_size(7,5764801)
        assert expected == result

    def test_find_loopsize2(self):
        expected = 11
        result = find_loop_size(7,17807724)
        assert expected == result


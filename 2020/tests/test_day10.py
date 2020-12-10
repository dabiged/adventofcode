from day10 import jolt_diff_dist, number_combinations
from lib.filehelper import file_to_str_array

class TestDay10:
    def test_example1(self):
        expected =35 
        result = jolt_diff_dist(file_to_str_array('tests/day10_testdata.txt'))
        assert expected == result 

    def test_example2(self):
        expected = 220
        result = jolt_diff_dist(file_to_str_array('tests/day10_testdata2.txt'))
        assert expected == result

    def test_part2_example1(self):
        expected = 8
        result = number_combinations(file_to_str_array('tests/day10_testdata.txt'))
        assert expected == result 

    def test_part2_example2(self):
        expected = 19208
        result = number_combinations(file_to_str_array('tests/day10_testdata2.txt'))
        assert expected == result 

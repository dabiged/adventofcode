from day13 import BusSched, BusSched2
from lib.filehelper import file_to_str_array


class TestDay13:
    def test_example1(self):
        expected = 295
        testsched = BusSched('tests/day13_testdata.txt')
        result=testsched.next_bus()
        assert expected == result

    def test_example2(self):
        expected = 1068781
        testsched = BusSched2('tests/day13_testdata.txt')
        result= testsched.find_time()
        print(result)
        assert True == False

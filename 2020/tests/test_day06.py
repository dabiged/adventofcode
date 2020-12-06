from day06 import count_uniq_questions, count_all_answered_questions
from lib.filehelper import file_to_str_array

class TestDay06:
    def test_(self):
        expected=11
        testinput=file_to_str_array("tests/day06_testinput.txt")
        print(testinput)
        result=count_uniq_questions(testinput)
        assert result == expected

    def test_01(self):
        expected=6
        testinput=file_to_str_array("tests/day06_testinput.txt")
        result=count_all_answered_questions(testinput)
        assert result== expected

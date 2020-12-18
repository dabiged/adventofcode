from day18 import FunnyMath, FunnyMath2


class TestDay18:
    def test_example1(self):
        inputvalue = '1 + 2 * 3 + 4 * 5 + 6'
        testmath=FunnyMath(inputvalue)
        result=testmath.run()
        assert result == 71

    def test_remove_brackets_example0(self):
        inputvalue = '1 + (2 * 3) + (4 * (5 + 6))'
        testmath=FunnyMath(inputvalue)
        result=testmath.run()
        assert result == 51

    def test_remove_brackets_example1(self):
        inputvalue = '2 * 3 + (4 * 5)'
        testmath=FunnyMath(inputvalue)
        result=testmath.run()
        assert result == 26

    def test_remove_brackets_example2(self):
        inputvalue = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
        testmath=FunnyMath(inputvalue)
        result=testmath.run()
        assert result == 437

    def test_remove_brackets_example3(self):
        inputvalue = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
        testmath=FunnyMath(inputvalue)
        result=testmath.run()
        assert result == 12240

    def test_remove_brackets_example4(self):
        inputvalue = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        testmath=FunnyMath(inputvalue)
        result=testmath.run()
        assert result == 13632

    def test_part2_example1(self):
        inputvalue = '1 + 2 * 3 + 4 * 5 + 6'
        testmath=FunnyMath2(inputvalue)
        result=testmath.run()
        assert result == 231

    def test_part2_remove_brackets_example0(self):
        inputvalue = '1 + (2 * 3) + (4 * (5 + 6))'
        testmath=FunnyMath2(inputvalue)
        result=testmath.run()
        assert result == 51

    def test_part2_remove_brackets_example1(self):
        inputvalue = '2 * 3 + (4 * 5)'
        testmath=FunnyMath2(inputvalue)
        result=testmath.run()
        assert result == 46

    def test_part2_remove_brackets_example2(self):
        inputvalue = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
        testmath=FunnyMath2(inputvalue)
        result=testmath.run()
        assert result == 1445

    def test_part2_remove_brackets_example3(self):
        inputvalue = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
        testmath=FunnyMath2(inputvalue)
        result=testmath.run()
        assert result == 669060

    def test_part2_remove_brackets_example4(self):
        inputvalue = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        testmath=FunnyMath2(inputvalue)
        result=testmath.run()
        assert result == 23340

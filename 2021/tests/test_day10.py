from day10 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay10:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        fix=FixLine('{([(<{}[<>[]}>{[]{[(<()>')
        result= fix.run_part1()
        assert result==1197

    def test_02(self):
        fix=FixLine('[[<[([]))<([[{}[[()]]]')
        result= fix.run_part1()
        assert result==3

    def test_03(self):
        fix=FixLine('[{[{({}]{}}([{[{{{}}([]')
        result= fix.run_part1()
        assert result==57

    def test_04(self):
        fix=FixLine('[<(<(<(<{}))><([]([]()')
        result= fix.run_part1()
        assert result==3

    def test_06(self):
        fix=FixLine('<{([([[(<>()){}]>(<<{{')
        result= fix.run_part1()
        assert result==25137

    def test_07(self):
        fix=FixLine('[(()[<>])]({[<{<<[]>>(')
        fix.process()
        print(fix.activest)
        assert fix.isIncomplete() == True

    def test_07(self):
        inputfile='./tests/input_day10.txt'
        testfixer=SyntaxFixer(inputfile)
        result=testfixer.part1()
        assert result == 26397


    def test_07(self):
        inputfile='./tests/input_day10.txt'
        testfixer=SyntaxFixer(inputfile)
        result=testfixer.part2()
        assert result == 288957

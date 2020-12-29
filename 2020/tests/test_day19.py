from day19 import RegExpComputer, RegExpComputerRecursive
from lib.filehelper import file_to_str_array


class TestDay19:
    def test_read_data(self):
        testdata='tests/day19_testdata.txt'
        mycomp = RegExpComputer(file_to_str_array(testdata))
        assert (4, 1, 5) == mycomp.rules[0]
        assert 'aaaabbb' in mycomp.messages

    def test_build_regexp(self):
        testdata='tests/day19_testdata.txt'
        mycomp = RegExpComputer(file_to_str_array(testdata))
        # strs
        assert mycomp.build_regexp(rule=4)== 'a'
        assert mycomp.build_regexp(rule=5)== 'b'
        # lists
        assert '(aa|bb)' == mycomp.build_regexp(rule=2)
        # tuples
        assert '(a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b)' == mycomp.build_regexp()

    def test_match(self):
        testdata='tests/day19_testdata.txt'
        mycomp = RegExpComputer(file_to_str_array(testdata))
        result=mycomp.match()
        assert result == 2

    def test_read_data_recursive(self):
        testdata='tests/day19_testdata2.txt'
        mycomp = RegExpComputerRecursive(file_to_str_array(testdata))
        assert (8, 11) == mycomp.rules[0]
        assert 'bbabbbbaabaabba' in mycomp.messages

    def test_build_regexp_recursive(self):
        testdata='tests/day19_testdata2.txt'
        mycomp = RegExpComputerRecursive(file_to_str_array(testdata))
        # strs
        assert mycomp.build_regexp(rule=14)== 'b'
        assert mycomp.build_regexp(rule=1)== 'a'
        # lists
        assert '(aa|ab)' == mycomp.build_regexp(rule=25)
        # tuples
        assert '(aa)' == mycomp.build_regexp(rule=4)
        # rule 8. Replace rule 42 with a single char.
        mycomp.rules[42] = 'x'
        # Rule 8 is just 1 or more of rule 42.
        assert '(x)+' ==  mycomp.build_regexp(rule=8)
        # rule 11. replace rule 31 with a single char
        mycomp.rules[31] = 'y'
        # Rule 11 is of the form xy|xxyy|xxxyyy|xxxxyyyy aka x{1}y{1}|x{2}y{2}...
        assert 'x{1}y{1}|x{2}y{2}' in  mycomp.build_regexp(rule=11)

    def test_match(self):
        testdata='tests/day19_testdata2.txt'
        mycomp = RegExpComputerRecursive(file_to_str_array(testdata))
        result=mycomp.match()
        assert result == 12


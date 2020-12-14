from day14 import Computer, ComputerVer2


class TestDay14:
    def test_bin2int(self):
        expected=73
        mycomp=Computer('tests/day14_testdata.txt') 
        result=mycomp.bin2int('000000000000000000000000000001001001')
        assert result == expected

    def test_int2bin(self):
        expected73='000000000000000000000000000001001001'
        expected101='000000000000000000000000000001100101'
        mycomp=Computer('tests/day14_testdata.txt')
        assert expected73 == mycomp.int2bin(73)
        assert expected101 == mycomp.int2bin(101)

    def test_run_example1(self):
        mycomp=Computer('tests/day14_testdata.txt')
        result=mycomp.run()
        assert result == 165

    def test_applymask2memloc_example2(self):
        mycomp=ComputerVer2('tests/day14_testdata.txt')
        result=mycomp.apply_mask2memloc('000000000000000000000000000000X1001X',42)
        expected = [26,27,58,59]
        assert expected == result

    def test_run_example2(self):
        mycomp=ComputerVer2('tests/day14_testdata2.txt')
        result=mycomp.run()
        expected = 208
        assert expected == result

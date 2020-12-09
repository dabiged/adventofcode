from day09 import XMasDecoder
from lib.filehelper import file_to_str_array


class TestDay09:
    def test_example1(self):
        inputvalue = file_to_str_array('tests/day09_testdata.txt')
        mydecoder = XMasDecoder(inputvalue)
        Isin = mydecoder.checknextn(tocheck=5)
        assert Isin == False

    def test_example1_run(self):
        expected = 127
        inputvalue = file_to_str_array('tests/day09_testdata.txt')
        mydecoder = XMasDecoder(inputvalue)
        result = mydecoder.run_until_missing(tocheck=5)
        assert result == expected


    def test_example2_run(self):
        expected = 62
        inputvalue = file_to_str_array('tests/day09_testdata.txt')
        mydecoder = XMasDecoder(inputvalue)
        result = mydecoder.contiguous_sum(mydecoder.run_until_missing(tocheck=5))
        assert result == expected



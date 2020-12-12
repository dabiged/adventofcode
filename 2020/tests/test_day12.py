from day12 import NavComp
from lib.filehelper import file_to_str_array


class TestDay12:
    def test_turnright(self):
        result = NavComp(file_to_str_array('tests/day12_testdata.txt'))
        print(result.direction)
        result.turn('R90')
        print(result.direction)
        result.turn('L360')
        print(result.direction)
        #assert expected == result

    def test_init_print(self):
        expected = 25
        testnavcomp = NavComp(file_to_str_array('tests/day12_testdata.txt'))
        result = testnavcomp.dist_from_origin()
        assert expected == result

##      def test_init_print(self):
##          expected = 
##          inputvalue = 
##          result = (inputvalue)
##          assert expected == result
##  

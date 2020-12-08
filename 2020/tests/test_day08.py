from day08 import BootCode, VM_InstrNotFound, VM_PositionOutOfBounds
from lib.filehelper import file_to_str_array
import pytest

class TestDay08:
    def test_build_dict(self):
        testinput=file_to_str_array("tests/day08_testdata.txt")
        testbootcode=BootCode(testinput)
        assert testbootcode.bootcode[0] == ['nop','+0']

    def test_step(self):
        testinput=file_to_str_array("tests/day08_testdata.txt")
        testbootcode=BootCode(testinput)
        testbootcode.step()
        assert testbootcode.accumulator == 0 
        assert testbootcode.position == 1
        testbootcode.step()
        assert testbootcode.accumulator == 1
        assert testbootcode.position == 2
        testbootcode.step()
        assert testbootcode.accumulator == 1
        assert testbootcode.position == 6
        testbootcode.step()
        assert testbootcode.accumulator == 2
        assert testbootcode.position == 7
        testbootcode.step()
        assert testbootcode.accumulator == 2
        assert testbootcode.position == 3
        testbootcode.step()
        assert testbootcode.accumulator == 5
        assert testbootcode.position == 4
        testbootcode.step()
        assert testbootcode.accumulator == 5
        assert testbootcode.position == 1

    def test_run(self):
        testinput=file_to_str_array("tests/day08_testdata.txt")
        testbootcode=BootCode(testinput)
        result = testbootcode.run()
        assert result == 5

    def test_unknown_instr_error(self):
        testinput=["nop +0","brk -1"]
        testbootcode=BootCode(testinput)
        with pytest.raises(VM_InstrNotFound):
            result = testbootcode.run()

    def test_position_out_of_bounds(self):
        testinput=["nop +0","jmp +7","acc +1"]
        testbootcode=BootCode(testinput)
        with pytest.raises(VM_PositionOutOfBounds):
            result = testbootcode.run()

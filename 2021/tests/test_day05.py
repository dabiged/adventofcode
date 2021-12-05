from day05 import Seafloor
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay05:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputfile = "./tests/input_day05.txt"
        testSeafloor=Seafloor(inputfile)
        testSeafloor.process_flat()
        result=testSeafloor.get_duplicates()
        assert result ==  5

    def test_02(self):
        inputfile = "./tests/input_day05.txt"
        testSeafloor=Seafloor(inputfile)
        testSeafloor.process_all()
        result=testSeafloor.get_duplicates()
        assert result ==  12


from day06 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay06:
    # pylint: disable=missing-module-docstring
    def test_01(self):
        inputfile = "./tests/input_day06.txt"
        testspawn=FishSpawn(inputfile,18)
        testspawn.run()
        assert 26 == testspawn.count()

    def test_02(self):
        inputfile = "./tests/input_day06.txt"
        testspawn=FishSpawn(inputfile,80)
        testspawn.run()
        assert 5934 == testspawn.count()

    def test_03(self):
        inputfile = "./tests/input_day06.txt"
        testspawn=FishSpawn(inputfile,256)
        testspawn.runp2()
        assert 26984457539 == testspawn.count()

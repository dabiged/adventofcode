from day16 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay16:
    # pylint: disable=missing-module-docstring
    def test_HEX2BIN1(self):
        assert convertH2B('D2FE28')=='110100101111111000101000'

    def test_HEX2BIN2(self):
        assert convertH2B('EE00D40C823060')=='11101110000000001101010000001100100000100011000001100000'

    def test_Binary2Dec(self):
        assert convertB2D('101') == 5
        assert convertB2D('100000') == 32

    def test_literal(self):
        assert packetreader('D2FE28') == 2021


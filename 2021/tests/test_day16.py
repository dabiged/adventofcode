from day16 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay16:
    # pylint: disable=missing-module-docstring
    def test_HEX2BIN1(self):
        testpacket=PacketDecoder('D2FE28')
        assert testpacket.binstr=='110100101111111000101000'

    def test_HEX2BIN2(self):
        testpacket=PacketDecoder('EE00D40C823060')
        assert testpacket.binstr=='11101110000000001101010000001100100000100011000001100000'

    def test_Binary2Dec(self):
        testpacket=PacketDecoder('EE00D40C823060')
        assert testpacket.convertB2D('101') == 5
        assert testpacket.convertB2D('100000') == 32

    def test_version_type(self):
        testpacket=PacketDecoder('D2FE28')
        assert testpacket.version == 6
        assert testpacket.packettypeid == 4

    def test_literal(self):
        testpacket=PacketDecoder('D2FE28')
        assert testpacket.read_literal() == 2021

    def test_run_literal(self):
        testpacket=PacketDecoder('D2FE28')
        assert testpacket.run() == 2021

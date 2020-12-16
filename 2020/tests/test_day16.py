from day16 import Tickets
from lib.filehelper import file_to_str_array

class TestDay16:
    def test_description1(self):
        expected = 71
        testtickets = Tickets(file_to_str_array('tests/day16_testdata.txt'))
        result=testtickets.ticket_scanning_error_rate()
        assert result == expected

    def test_discard_invalid(self):
        expected = ['row', 'class', 'seat']
        testtickets = Tickets(file_to_str_array('tests/day16_testdata.txt'))
        result=testtickets.discard_invalid()
        assert result == expected

    def test_decode_fields(self):
        expected = ['row', 'class', 'seat']
        testtickets = Tickets(file_to_str_array('tests/day16_testdata2.txt'))
        testtickets.discard_invalid()
        result = testtickets.decode_fields()
        assert result == expected







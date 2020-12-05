from day05 import BoardingPass

class TestDay05:
    def test_init_row_seats(self):
        testinput="FBFBBFFRLR"
        testBP=BoardingPass(testinput)
        assert "FBFBBFF" == testBP.rows
        assert "RLR" == testBP.cols

    def test_init_seat_row(self):
        testinput="FBFBBFFRLR"
        testBP=BoardingPass(testinput)
        assert testBP.seat_row() == 44
        assert testBP.seat_col() == 5
        assert testBP.seat_id() == 357

    def test_example_part1(self):
        testinput=["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]
        testseatids, testrows, testcols =[],[],[]
        for test in testinput:
            testBP=BoardingPass(test)
            testseatids.append(testBP.seat_id())
            testrows.append(testBP.seat_row())
            testcols.append(testBP.seat_col())
        assert testseatids == [567, 119, 820]
        assert testrows == [70, 14, 102]
        assert testcols == [7, 7, 4]

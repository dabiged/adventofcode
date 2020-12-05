from day04 import readlog, build_dict, SleepTable
from lib.filehelper import file_to_str_array
from datetime import datetime


class TestDay04:
    def test_read_one_line_log(self):
        expected_info = "Guard #10 begins shift"
        expected_timedate = datetime(1518,11,1,hour=0,minute=0)
        testinput= "[1518-11-01 00:00] Guard #10 begins shift"
        clock, info = readlog(testinput)
        assert expected_info == info
        assert expected_timedate == clock

    def test_read_multiple_lines_and_sort(self):
        expected = ["Guard","falls","wakes"]
        testinput= ["[1518-11-04 00:46] wakes up","[1518-11-04 00:36] falls asleep","[1518-11-01 00:00] Guard #10 begins shift"]
        results=[]
        for logstr in build_dict(testinput):
            # Grab the first word of the logbook text
            results.append(logstr[1].split()[0])
        assert expected == results

    def test_sleepy_guard(self):
        testtable=SleepTable(build_dict(file_to_str_array("tests/day05_testinput.txt")))
        assert 10 == testtable.sleepiest_guard()
        assert 24 == testtable.sleepiest_minute(testtable.sleepiest_guard())

    def test_sleepier_guard(self):
        testtable=SleepTable(build_dict(file_to_str_array("tests/day05_testinput.txt")))
        guard,minute = testtable.sleepiest_minute_ofall()
        assert minute*guard  == 4455

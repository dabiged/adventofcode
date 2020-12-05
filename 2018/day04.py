"""
AOC day 04 2018
"""

from datetime import datetime
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def readlog(line):
    ''' Read an entry in the log book and return the datetime and the logbook entry.

    Logbook formats are like this:
    [1518-11-04 00:02] Guard #99 begins shift
    [1518-11-04 00:36] falls asleep
    [1518-11-04 00:46] wakes up

    '''
    strformat = '[%Y-%m-%d %H:%M'
    clock = line.split('] ')[0]
    info = line.split(sep='] ')[1]
    dateandtime = datetime.strptime(clock,strformat)
    return dateandtime, info

def build_dict(listoflogs):
    '''
    Convert a logbook of strings into a time sorted dictionary
    with keys as the datetime and values as the log entry.
    '''
    logbook={}
    for log in listoflogs:
        dateandtime, info = readlog(log)
        logbook[dateandtime]=info

    return sorted(logbook.items())

class SleepTable:
    """A tool to keep track of sleepy guards """

    def __init__(self, loglist):
        '''
        sequentially parse the sorted logbook and build a dict of
        how many minutes each guard was asleep.
        '''
        self.guard_sleeping_minutes={}
        start_sleep_time=59
        end_sleep_time=0

        # Look through the log book.
        for dateandtime, info in loglist:
            firstshift=True
            if "Guard" in info:
                # If a new guard comes on shift,
                # that means the last shift ended at 59 mins past hour.
                if not firstshift:
                    for minute in range(start_sleep_time,60):
                        self.guard_sleeping_minutes[guard][minute]+=1
                # Read new Guard ID and if it is the first time we have seen it, add it to the dict.
                guard=int(info.split()[1].lstrip('#'))
                if guard not in self.guard_sleeping_minutes.keys():
                    self.guard_sleeping_minutes[guard] = {}
                    for minute in range(60):
                        self.guard_sleeping_minutes[guard][minute]=0
                firstshift=False
            if "falls asleep" in info:
                # If a guard falls asleep record the time they fell asleep.
                start_sleep_time = dateandtime.minute
            if "wakes up" in info:
                end_sleep_time = dateandtime.minute
                for minute in range(start_sleep_time, end_sleep_time):
                    self.guard_sleeping_minutes[guard][minute] += 1

    def sleepiest_guard(self):
        """ which guard slept the most"""
        sleepy_guards={}
        # find the guard that slept the most.
        for guard in self.guard_sleeping_minutes:
            guard_total_mins=0
            for minute in self.guard_sleeping_minutes[guard].values():
                guard_total_mins+=minute
            sleepy_guards[guard]=guard_total_mins
        return max(sleepy_guards, key=sleepy_guards.get)

    def sleepiest_minute(self, guard):
        """on which minute did this guard sleep the most"""
        return max(self.guard_sleeping_minutes[guard], key=self.guard_sleeping_minutes[guard].get)

    def sleepiest_minute_ofall(self):
        """find out which minute is the most slept in and by which guard"""
        checkmin=0
        for guard in self.guard_sleeping_minutes:
            if self.sleepiest_minute(guard) > checkmin:
                largest_guard = guard
        return largest_guard, self.sleepiest_minute(largest_guard)


def day04_01():
    """Run part 1 of Day 4's code"""
    path = "./input/04/input.txt"
    santatable=SleepTable(build_dict(file_to_str_array(path)))
    result=santatable.sleepiest_guard()*santatable.sleepiest_minute(santatable.sleepiest_guard())
    print(f'0401: product of sleepiest guard and their sleepiest minute: {result}')

def day04_02():
    """Run part 2 of Day 4's code"""
    path = "./input/04/input.txt"
    santatable=SleepTable(build_dict(file_to_str_array(path)))
    guard, minute = santatable.sleepiest_minute_ofall()
    result=guard * minute
    print(f'0402: product of the sleepiest minute and that guard: {result}')

if __name__ == "__main__":
    day04_01()
    day04_02()

"""
AOC day 05 2020
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class BoardingPass:
    """
    A binary space partitioned boarding pass.
    """

    def __init__(self,inputstr):
        """Split input string into substrings determining row and cols"""
        self.rows=inputstr[0:7]
        self.cols=inputstr[7:10]

    def seat_row(self) ->int:
        """Given the binary partitioned string, returns the seat's row number.
        This is an integer between 0 and 127.
        """
        lowrow=0
        highrow=127
        for direction in self.rows:
            if direction == "F":
                highrow = (highrow + lowrow) // 2
            if direction == "B":
                lowrow= ((highrow + lowrow) // 2) +1
        assert lowrow==highrow
        return lowrow

    def seat_col(self) -> int:
        """Given the binary partitioned string, returns the seat's col number.
        This is an integer between 0 and 7.
        """
        lowcol=0
        highcol=7
        for direction in self.cols:
            if direction == "L":
                highcol = (highcol + lowcol) // 2
            if direction == "R":
                lowcol= ((highcol + lowcol) // 2 )+1
        assert lowcol==highcol
        return lowcol

    def seat_id(self):
        """The boarding passes seat ID
        Integer between 0 and 1023 assuming all seats occupied."""
        return self.seat_row()*8 + self.seat_col()


def day05_01():
    """Run part 1 of Day 05's code"""
    path = "./input/05/input.txt"
    result = max([BoardingPass(barcode).seat_id() for barcode in file_to_str_array(path)])
    print(f'0501: Highest SeatID: {result}')

def day05_02():
    """Run part 2 of Day 05's code"""
    path = "./input/05/input.txt"
    all_passes = [BoardingPass(barcode).seat_id() for barcode in file_to_str_array(path)]
    all_passes.sort()
    for i in range(min(all_passes),max(all_passes)+1):
        if i not in all_passes:
            result = i
    print(f'0502: Santas Boarding pass number is {result}')

if __name__ == "__main__":
    day05_01()
    day05_02()

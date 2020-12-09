"""
AOC day 09 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class XMasDecoder:
    """
    A class to attack the weakness in the XMAS encryption
    """

    def __init__(self,listofints):
        """Store integers in a list
        position is the location to be checked."""
        self.position=0
        self.tocheck=25
        self.numlist = [ int(i) for i in listofints ]

    def checknextn(self,tocheck=25):
        """ Check that self.numlist[self.position] can be made up of the
        previous tocheck numbers in numlist.
        """
        self.tocheck=tocheck
        # the start, end of the window to look in and the location to check.
        startloc = self.position-self.tocheck
        endloc = self.position
        # Calc all sums of the buffer.
        sums_numbuffer = [ \
        self.numlist[a] + self.numlist[b] \
        for a in range(startloc, endloc) \
        for b in range(a,endloc) ]
        if self.numlist[self.position] in sums_numbuffer:
            return True
        return False

    def run_until_missing(self,tocheck=25):
        """ Repeatedly check the that the locations in numlist can be made up
        of the past tocheck numbers. If not, return the number that cannot be made"""
        self.position=tocheck
        for self.position in range(self.position, len(self.numlist)):
            if self.checknextn(tocheck=tocheck):
                pass
            else:
                return self.numlist[self.position]
        return None

    def contiguous_sum(self,number):
        """Find a sequence of numbers that sum to number in self.numlist"""
        for minloc in range(0,len(self.numlist)):
            for maxloc in range(0,len(self.numlist)):
                if sum(self.numlist[minloc:maxloc]) == number:
                    nums=sorted(self.numlist[minloc:maxloc])
                    return nums[0]+nums[-1]
        return None

def day09_01():
    """Run part 1 of Day 09's code"""
    path = "./input/09/input.txt"
    mydecoder = XMasDecoder(file_to_str_array(path))
    result= mydecoder.run_until_missing(tocheck=25)
    print(f'0901: The number not in the any sum of pairs in the previous 25 numbers: {result}')

def day09_02():
    """Run part 2 of Day 09's code"""
    path = "./input/09/input.txt"
    mydecoder = XMasDecoder(file_to_str_array(path))
    numbertofind = mydecoder.run_until_missing(tocheck=25)
    result=mydecoder.contiguous_sum(numbertofind)

    print(f'0902: The sum of the first and last numbers in the longest contiguous sum is: {result}')

if __name__ == "__main__":
    day09_01()
    day09_02()

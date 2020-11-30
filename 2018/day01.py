from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def calibrate_device(freqchange: list) -> int:
    """
    Returns a final frequency given a list of changes

    Note: freqchange is a list of strs prefixed with a + or -.
    """
    frequency=0
    for freq in freqchange:
        frequency = frequency + int(freq.lstrip("+"))
    return frequency


def calibrate_freq_twice_device(freqchange: list) -> int:
    """
    Returns the first frequency to be seen twice given a list of changes.

    Note: freqchange is a list of strs prefixed with a + or -.
    """
    seenfreqs={}
    frequency=0
    while True:
        for freq in freqchange:
            if frequency not in seenfreqs.keys():
                seenfreqs[frequency]=1
            elif seenfreqs[frequency] == 1:
                return frequency
            frequency = frequency + int(freq.lstrip("+"))


def day01_01():
    """Run part 1 of Day 1's code"""
    path = "./input/01/input.txt"
    final_freq = calibrate_device(file_to_str_array(path))
    print(f"final frequency: {final_freq}")


def day01_02():
    """Run part 2 of Day 1's code"""
    path = "./input/01/input.txt"
    final_freq = calibrate_freq_twice_device(file_to_str_array(path))
    print(f"final frequency: {final_freq}")


if __name__ == "__main__":
    day01_01()
    day01_02()

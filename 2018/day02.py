from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def checksum_one_label(boxid: str) -> dict:
    """
    Create a dict which contains a bool int represetation of if a str contains a double or triple letter.
    """
    # Create a dict of each letter and how many there are.
    characters={}
    
    for character in boxid:
        if character in characters.keys():
            characters[character] += 1
        else:
            characters[character] = 1

    # Create a dict with how many double and triples there are.
    bool_dict = {}
    for key, value in characters.items():
        for num in range(2,4):
            if value == num:
                bool_dict[num] = 1

    return bool_dict

def checksum_multiple_labels(boxidlist: list) -> int:
    """
    Calculate a checksum based on the number of double and triple letters.
    """
    unique_cases={}
    for boxid in boxidlist:
        boxiddict = checksum_one_label(boxid)
        for key, value in boxiddict.items():
            for num in range(2,10):
                if key==num:
                    if num not in unique_cases.keys():
                        unique_cases[num]=1
                    else:
                        unique_cases[num] += 1
    checksum=1
    for value in unique_cases.values():
        checksum*= value
    return checksum




##  def calibrate_freq_twice_device(freqchange: list) -> int:
##      """
##      Returns the first frequency to be seen twice given a list of changes.
##  
##      Note: freqchange is a list of strs prefixed with a + or -.
##      """
##      seenfreqs={}
##      frequency=0
##      while True:
##          for freq in freqchange:
##              if frequency not in seenfreqs.keys():
##                  seenfreqs[frequency]=1
##              elif seenfreqs[frequency] == 1:
##                  return frequency
##              frequency = frequency + int(freq.lstrip("+"))


def day02_01():
    """Run part 1 of Day 2's code"""
    path = "./input/02/input.txt"
    final_checksum = checksum_multiple_labels([boxid for boxid in file_to_str_array(path)])
    print(f"final checksum: {final_checksum}")


def day02_02():
    """Run part 2 of Day 1's code"""
    path = "./input/01/input.txt"
    final_freq = calibrate_freq_twice_device(file_to_str_array(path))
    print(f"final frequency: {final_freq}")


if __name__ == "__main__":
    day02_01()
    #day02_02()

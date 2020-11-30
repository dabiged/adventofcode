"""
AOC day 02 2018
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

def checksum_one_label(boxid: str) -> dict:
    """
    Create a dict which contains a bool int represetation of if a str contains a
    double or triple letter.
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
    for value in characters.values():
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


def find_similar_boxids(boxidlist: list) -> tuple:
    """
    Given a list of str, find the two that are the most similar.
    Similar is equal letters in equal spaces.
    """
    # Create a dict to store scores, and one to store the common characters.
    similarboxids_scores={}
    similarboxids_chars={}
    # Loop over all pairs of boxids
    for boxid1 in boxidlist:
        for boxid2 in boxidlist:
            if boxid1 == boxid2 :
                # don't compre the same boxids.
                break
            if (boxid1, boxid2) in similarboxids_scores.keys():
                # don't compare boxid pairs already seen
                break
            samechars = 0
            similarchars=""
            # compare character in each boxid.
            for char1, char2 in zip(boxid1,boxid2):
                if char1 == char2:
                # If they are the same character add one to the score and
                #    append the character to a temp str.
                    samechars+=1
                    similarchars+=char1
            # Store the scores and character in our dicts, with tuples of boxid pairs.
            similarboxids_scores[(boxid2,boxid1)] = samechars
            similarboxids_chars[(boxid2,boxid1)] = similarchars
    # Return the similar characters of the boxids with the highest score. from here.
    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    return similarboxids_chars[max(similarboxids_scores,key=similarboxids_scores.get)]

def day02_01():
    """Run part 1 of Day 2's code"""
    path = "./input/02/input.txt"
    final_checksum = checksum_multiple_labels(file_to_str_array(path))
    print(f"final checksum: {final_checksum}")


def day02_02():
    """Run part 2 of Day 1's code"""
    path = "./input/02/input.txt"
    common_letters = find_similar_boxids(file_to_str_array(path))
    print(f"Similar Characters: {common_letters}")


if __name__ == "__main__":
    day02_01()
    day02_02()

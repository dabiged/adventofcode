"""
AOC day 05 2018
"""
from lib.filehelper import file_to_str_array
import copy
# pylint: disable=missing-module-docstring

class Polymer:
    """A magic polymer for Santa's suit"""
    def __init__(self, inputstr):
        """ """
        self.inputstr = inputstr
        self.polymer = list(inputstr)

    def __len__(self):
        """Length of the polymer"""
        return len(self.polymer)

    def __repr__(self):
        """Conver the list to a str for display"""
        return "".join(i for i in self.polymer)

    def reactonce(self):
        """Perform one pass of polymer reacting"""
        i = len(self.polymer)-2
        while i >=0:
            if \
            (self.polymer[i].islower() and \
            self.polymer[i+1].isupper() \
            and self.polymer[i] == self.polymer[i+1].lower()) \
            or \
            (self.polymer[i].lower() == self.polymer[i+1] \
            and self.polymer[i].isupper() \
            and self.polymer[i+1].islower()):
                if i == 0:
                    self.polymer = self.polymer[2:]
                    i-=1
                elif i == len(self.polymer)-1 :
                    self.polymer = self.polymer[:-2]
                    i-=2
                else:
                    self.polymer = self.polymer[:i]+self.polymer[i+2:]
                    i-=1
            i-=1



    def react(self):
        """Perform as many reactions as required until the lenght stops changing"""
        oldlen = 0
        while oldlen != len(self.polymer):
            oldlen = len(self.polymer)
            self.reactonce()

    def remove_unit(self,unit):
        """Remove a letter (upper and lower) from the polymer"""
        self.polymer = [value for value in self.polymer \
        if value not in [unit, unit.lower(), unit.upper()]]

def day05_01():
    """Run part 1 of Day 5's code"""
    path = "./input/05/input.txt"
    for string in file_to_str_array(path):
        santa_polymer=Polymer(string)
    santa_polymer.react()
    result=len(santa_polymer)
    print(f'0501: Length of reacted polymer {result}')

def day05_02():
    """Run part 2 of Day 5's code"""
    path = "./input/05/input.txt"
    removed_letters={}
    # Run part 1 and use it's input to each letter
    for string in file_to_str_array(path):
        santa_polymer=Polymer(string)
        santa_polymer.react()
    part2input=santa_polymer.polymer

    for letter in "abcdefghijklmnopqrstuvwxyz":
        santa_polymer=Polymer(part2input)
        santa_polymer.remove_unit(letter)
        santa_polymer.react()
        removed_letters[letter]=len(santa_polymer)
    result=min(removed_letters.values())
    print(f'0502: The length of the shortest polymer produced is {result}')

if __name__ == "__main__":
    day05_01()
    day05_02()

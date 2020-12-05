"""
AOC day 05 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Polymer:
    def __init__(self, inputstr):
        """ """
        self.inputstr = inputstr
        self.polymer = list(inputstr)

    def __len__(self):
        return len(self.polymer)

    def __repr__(self):
        return "".join([i for i in self.polymer])

    def reactonce(self):
        i = len(self.polymer)-2
        while i >=0:
            if (self.polymer[i].islower() and self.polymer[i+1].isupper() and self.polymer[i] == self.polymer[i+1].lower()) or (self.polymer[i].lower() == self.polymer[i+1] and self.polymer[i].isupper() and self.polymer[i+1].islower()):
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
        oldlen = 0
        while oldlen != len(self.polymer):
            oldlen = len(self.polymer)
            self.reactonce()

    def remove_unit(self,unit):
       self.polymer = [value for value in self.polymer if value not in [unit, unit.lower(), unit.upper()]] 

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
    for letter in "abcdefghijklmnopqrstuvwxyz":
        for string in file_to_str_array(path):
            santa_polymer=Polymer(string)
        santa_polymer.remove_unit(letter)
        santa_polymer.react()
        removed_letters[letter]=len(santa_polymer)
    result=min(removed_letters.values())
    print(f'0502: The length of the shortest polymer produced is {result}')

if __name__ == "__main__":
    day05_01()
    day05_02()

"""
AOC day 08 2018
"""
from collections import defaultdict, deque
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class node():
    def __init__(self,treedef):
        self.treedef=treedef
        self.NumChildren=self.treedef.popleft()
        self.NumMetaData=self.treedef.popleft()
        self.children=[]
        self.metadata=[]
        self.add_children()
        self.add_MetaData()
        print(self.children, self.metadata)

    def add_children(self):
        if self.NumChildren != 0:
            for child in range(self.NumChildren):
                NewNode=node(self.treedef)
                self.treedef=NewNode.treedef
                self.children.append(NewNode)
    def add_MetaData(self):
        if self.NumMetaData != 0:
            for MD in range(self.NumMetaData):
                self.metadata.append(self.treedef.popleft())

    def sum_metadata(self):
        if self.NumChildren==0:
            return sum(self.metadata)
        else:
            return sum(self.metadata)+sum([child.sum_metadata() for child in self.children])

def day08_01():
    """Run part 1 of Day 08's code"""
    print(f'0801: The largest finite area is: ')

def day08_02():
    """Run part 2 of Day 08's code"""
    print(f'0802: Number of spaces within')

if __name__ == "__main__":
    day08_01()
    day08_02()

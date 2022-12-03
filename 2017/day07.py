from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from collections import defaultdict


class Node:
    def __init__(self,name,value):
        self.name=name
        self.value=value
        self.neighbours=[]
    def add_neighbour(self,other):
        self.neighbours.append(other)

    def __repr__(self):
        return f"Node({self.name}, Value={self.value}, Neighbours={' '.join(self.neighbours)}"
        

class ProgramStack():
    def __init__(self,GraphDef):
        self.definition=GraphDef
        self.build_graph()

    def build_graph(self):
        self.graph={}
        for line in self.definition:
            entries=line.split()
            name=entries[0]
            value=int(entries[1][1:-1])
            neighbours=[ i[:-1] if ',' in i else i for i in entries[3:] ]

            self.graph[name]=Node(name,value)
            for neighbour in neighbours:
                self.graph[name].add_neighbour(neighbour)

    def find_bottom(self):
        subnodes=set()
        for node in self.graph.values():
            if len(node.neighbours) >0:
                for this_node in node.neighbours:
                    subnodes.add(this_node)
        for node in self.graph.keys():
            if node not in subnodes:
                return node

    def find_value(self,node):
        if not self.graph[node].neighbours:
            return self.graph[node].value
        else:
            total=0
            for subnode in self.graph[node].neighbours:
                total+=self.find_value(subnode)
            return total+self.graph[node].value

    def find_mismatch(self, node):
        vals=defaultdict(int)
        neighs={}

        for neighbour in self.graph[node].neighbours:
            neighs[neighbour] = self.find_value(neighbour)
            vals[self.find_value(neighbour)]+=1

        if len(vals.keys()) != 1:
            for key,value in vals.items():
                if value ==1:
                    for k,v in neighs.items():
                        print(k,v)
                        if v ==key:
                            self.find_mismatch(k)
        else:
            return node


def day07_01():
    """Run part 1 of Day 7's code"""
    path = "./input/07/input.txt"
    myProgram=ProgramStack(file_to_str_array(path))
    print('0701:', myProgram.find_bottom())



def day07_02():
    """Run part 2 of Day 7's code"""
    path = "./input/07/input.txt"
    myProgram=ProgramStack(file_to_str_array(path))
    print('0702:', myProgram.find_mismatch(myProgram.find_bottom()))


if __name__ == "__main__":
    day07_01()
    day07_02()

"""
AOC day XX 2018
"""
from lib.filehelper import file_to_str_array
from collections import defaultdict, deque
from copy import deepcopy
# pylint: disable=missing-module-docstring

class Journey():
    def __init__(self,startlocation):
        self.nodesvisited=startlocation

    def newnode(self,node):
        self.nodesvisited.append(node)

    def currentnode(self):
        return self.nodesvisited[-1]

    def isValid(self):
        node_visit_count=defaultdict(int)
        for i in self.nodesvisited:
            node_visit_count[i]+=1
        for key,value in node_visit_count.items():
            if key == key.lower() and value > 1:
                return False
        return True

    def isp2Valid(self):
        node_visit_count=defaultdict(int)
        if self.nodesvisited.count('end') > 1:
            return False
        if self.nodesvisited.count('start') > 1:
            return False
        for i in self.nodesvisited:
            node_visit_count[i]+=1
        smallcaves=0
        for key,value in node_visit_count.items():
            if key == key.lower() and value > 1:
                if value >2:
                    return False
                smallcaves+=1
                if smallcaves > 1:
                    return False

        return True

    def isFinished(self):
        if 'end' in self.nodesvisited and 'start' in self.nodesvisited:
            return True
        return False

    def __repr__(self):
        return str(self.nodesvisited)

class Graph():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.graph=defaultdict(list)
        self.traverses={}
        self.processinputfile()
        self.validjourneys=[]

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)
        for line in self.input:
            nodes=line.split('-')
            from_node,to_node=nodes[0],nodes[1]
            self.graph[from_node].append(to_node)
            self.graph[to_node].append(from_node)


    def traverse(self):
        travel_queue=deque()
        travel_queue.append(Journey(['start']))
        while len(travel_queue) > 0:
            currentjourney=travel_queue.popleft()
            if not currentjourney.isValid():
                pass
            elif currentjourney.isFinished():
                self.validjourneys.append(currentjourney)
            else:
                for newdest in self.graph[currentjourney.currentnode()]:
                    thisjourn=deepcopy(currentjourney)
                    currentnodes=thisjourn.nodesvisited
                    currentnodes.append(newdest)
                    travel_queue.append(Journey(currentnodes))

    def retraverse(self):
        travel_queue=deque()
        travel_queue.append(Journey(['start']))
        while len(travel_queue) > 0:
            currentjourney=travel_queue.popleft()
            if currentjourney.isFinished():
                self.validjourneys.append(currentjourney)
            elif not currentjourney.isp2Valid():
                pass
            else:
                for newdest in self.graph[currentjourney.currentnode()]:
                    thisjourn=deepcopy(currentjourney)
                    currentnodes=thisjourn.nodesvisited
                    currentnodes.append(newdest)
                    travel_queue.append(Journey(currentnodes))

def day12_01():
    """Run part 1 of Day 12's code"""
    inputfile='input/day12.txt'
    myGraph=Graph(inputfile)
    myGraph.traverse()
    result=len(myGraph.validjourneys)
    print(f'1201: {result} journies through the caves.')

def day12_02():
    """Run part 2 of Day XX's code"""
    inputfile='input/day12.txt'
    myGraph=Graph(inputfile)
    myGraph.retraverse()
    result= len(myGraph.validjourneys) 
    print(f'1202: {result} journies through the cave revisiting at mode 1 small cave')

if __name__ == "__main__":
    day12_01()
    day12_02()

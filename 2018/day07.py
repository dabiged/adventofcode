"""
AOC day 06 2018
"""
# pylint: disable=missing-module-docstring

from lib.filehelper import get_string_lists_from_file

class WorkGraph():
    def __init__(self,filename, numworkers=1):
        self._filename=filename
        self._stepgraph={}
        self._allsteps=set()
        self.StepsTaken=""
        self.import_file(self._filename)
        self.numworkers=numworkers
        self.worktime={}
        self.worktodo=[0 for i in range(self.numworkers)]
        for letter,time in zip([i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'],[i for i in range(1,28)]):
            self.worktime[letter]=time
        print(self.worktime)

    def get_idle_worker(self):
        for i,amount in enumerate(self.worktodo):
            if amount ==0:
                return i
        return None

    def import_file(self,filename):
        a=get_string_lists_from_file(filename)
        for line in a:
            step=line[0].split()[7]
            prereq=line[0].split()[1]
            self._allsteps.add(step)
            self._allsteps.add(prereq)
            if step not in self._stepgraph.keys():
                self._stepgraph[step]=prereq
            else:
                self._stepgraph[step]=self._stepgraph[step]+prereq
        for step in self._allsteps:
            if step not in self._stepgraph.keys():
                self._stepgraph[step]=''
        return True

    def calc_part2(self):
        while len(self._stepgraph) >0:
            alphakeys=sorted(self._stepgraph.keys(), key=lambda x:x.lower())
            for key in alphakeys:
                val=self._stepgraph[key]
                if val == "":
                    for worker,workpending in enumerate(self.worktodo):
                        if workpending==0:
                            self.worktodo[worker]=self.worktime[key]
                            break
                    self.StepsTaken+=key
                    del self._stepgraph[key]
                    self._stepgraph=self.perform_step2(key)
                    break 
    def perform_step2(self,step):
        print(self.worktodo)
        print(self.StepsTaken)
        for worker,workpending in enumerate(self.worktodo):
            if workpending !=0:
                self.worktodo[worker] = workpending -1
            else:
                self.perform_step(step)
        return self._stepgraph

    def calc_part1(self):
        while len(self._stepgraph) >0:
            alphakeys=sorted(self._stepgraph.keys(), key=lambda x:x.lower())
            for key in alphakeys:
                val=self._stepgraph[key]
                if val == "":
                    self.StepsTaken+=key
                    del self._stepgraph[key]
                    self._stepgraph=self.perform_step(key)
                    break 
        return True

    def perform_step(self,step):
        for key,val in self._stepgraph.items():
            if step in val:
                remsteps=list(val)
                remsteps.remove(step)
                if len(remsteps) > 1 and remsteps != None:
                    self._stepgraph[key]="".join([ i for i in remsteps])
                elif len(remsteps) == 1:
                    self._stepgraph[key]=remsteps[0]
                else:
                    self._stepgraph[key]=''
        return self._stepgraph

def day07_01():
    """Run part 1 of Day 07's code"""
    path = "./input/07/input.txt"
    myGraph=WorkGraph(filename=path)
    myGraph.calc_part1()
    results=myGraph.StepsTaken
    print(f'0701: {result}')

def day07_02():
    """Run part 2 of Day 07's code"""
    path = "./input/07/input.txt"
    myGraph=WorkGraph(filename=path, numworkers=4)
    result=myGraph.get_idle_worker()
    print(f'0702: {result}')

if __name__ == "__main__":
    day07_01()
    day07_02()

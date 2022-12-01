from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Memory:
    def __init__(self,blocks):
        self.blocks=list(map(int,blocks))
        self.count=0
        self.seenstates=[]

    def get_maxloc(self):
        maxval=max(self.blocks)
        return self.blocks.index(maxval)

    def redist(self):
        position=self.get_maxloc()
        to_dist=self.blocks[position]
        self.blocks[position]=0
        while to_dist >0:
            position+=1
            position = position % len(self.blocks)
            self.blocks[position]+=1
            to_dist-=1

    def process(self):
        while self.blocks not in self.seenstates:
            self.seenstates.append(self.blocks.copy())
            self.count+=1
            self.redist()
        return self.count

    def len_cycle(self):
        return len(self.seenstates) - self.seenstates.index(self.blocks)

    def __repr__(self):
        return f'Memory({self.blocks})'


def day06_01():
    """Run part 1 of Day 6's code"""
    path = "./input/06/input.txt"
    myMem=Memory(file_to_str_array(path)[0].split('\t'))
    print('0601:', myMem.process())



def day06_02():
    """Run part 2 of Day 6's code"""
    path = "./input/06/input.txt"
    myMem=Memory(file_to_str_array(path)[0].split('\t'))
    myMem.process()
    print('0602:',myMem.len_cycle())


if __name__ == "__main__":
    day06_01()
    day06_02()

from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

testdata='''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

class Grid:
    def __init__(self,inputdata):
        # Store the input data for later (part 2)
        self.inputdata=inputdata
        self.grid=defaultdict(str)
        self.antennalocs=defaultdict(list)
        self.antinodelocs=set()
        for rownum,row in enumerate(inputdata):
            for colnum, char in enumerate(row):
                self.grid[colnum+rownum*1j]=char
                if char != '.':
                    self.antennalocs[char].append(colnum+rownum*1j)

        self.numrows=max([int(i.imag) for i in self.grid.keys()])
        self.numcols=max([int(i.real) for i in self.grid.keys()])
        
    def __str__(self):
        # helper method to print the grid
        output=''
        for im in range(self.numrows+1):
            for re in range(self.numcols+1):
                if re+im*1j in self.antinodelocs:
                    output+='#'
                else:
                    output+=self.grid[re+im*1j]
            output+='\n'
        return output

    def calc_antinodes(self):
        for antennatype,locs in self.antennalocs.items():
            for loca in locs:
                for locb in locs:
                    if loca!=locb:
                        candidate=(locb-loca)+locb
                        if 0<= candidate.imag <= self.numcols and 0<= candidate.real <= self.numrows:
                            self.antinodelocs.add((locb-loca)+locb)

    def calc_allantinodes(self):
        for antennatype,locs in self.antennalocs.items():
            # add the locations of the antenna with more than 1 location
            if len(locs) >1:
                for loc in locs:
                    self.antinodelocs.add(loc)
            for loca in locs:
                for locb in locs:
                    if loca!=locb:
                        delta=locb-loca
                        candidate=delta+locb
                        while 0<= candidate.imag <= self.numcols and 0<= candidate.real <= self.numrows:
                            self.antinodelocs.add(candidate)
                            candidate+=delta




def part1(inputdata=testdata.split('\n')):
    g=Grid(inputdata)
    g.calc_antinodes()
    print(g)
    return len(g.antinodelocs)

def part2(inputdata=testdata.split('\n')):
    g=Grid(inputdata)
    g.calc_allantinodes()
    print(g)
    return len(g.antinodelocs)


def day08_01():
    """Run part 1 of Day 08's code"""
    path = "./input/08.txt"
    print("0801:", part1(file_to_str_array(path)))


def day08_02():
    """Run part 2 of Day 08's code"""
    path = "./input/08.txt"
    print("0802:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day08_01()
    day08_02()

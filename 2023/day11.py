from lib.filehelper import file_to_str_array, get_bald_string_list_from_file, file_to_array
# pylint: disable=missing-module-docstring

test_input=['...#......',
'.......#..',
'#.........',
'..........',
'......#...',
'.#........',
'.........#',
'..........',
'.......#..',
'#...#.....']

def transpose(inputlist):
    output=[''.join(a) for a in list(map(list,zip(*inputlist)))]
    return output


class Map():
    def __init__(self,inputmap,expansion=1):
        self.inputmap=inputmap
        self.expansion=expansion
        self.emptyrows=[]
        self.emptycols=[]
        self.expand()
        self.galaxies={}
        self.find_galaxies()
        self.distances={}
        self.find_all_dist()

    def parse(self):
        pass

    def expandrows(self,inputmap,rows=True):
        outputmap=[]
        for i,row in enumerate(inputmap):
            if all([i=='.' for i in row]):
                if rows:
                    self.emptyrows.append(i)
                else:
                    self.emptycols.append(i)
            outputmap.append(row)
        return outputmap

    def expand(self):
        self.expandedmap=self.expandrows(self.inputmap)
        self.expandedmap=transpose(self.expandedmap)
        self.expandedmap=self.expandrows(self.expandedmap,rows=False)
        self.expandedmap=transpose(self.expandedmap)

    def find_galaxies(self):
        gal_number=1
        for row,rowchars in enumerate(self.expandedmap):
            for col, char in enumerate(rowchars):
                loc=col+row*1j
                if char == '#':
                    self.galaxies[gal_number] = loc
                    gal_number+=1

    def find_all_dist(self):
        for num1, loc1 in self.galaxies.items():
            for num2, loc2 in self.galaxies.items():
                if num2 <= num1:
                    pass
                else:
                    self.distances[(num1,num2)] = self.dist(loc1,loc2)

    def calc_all_dist(self):
        counter=0
        for dist in self.distances.values():
            counter+=dist
        return counter

    def dist(self,p1,p2):
        p1row,p1col = int(p1.imag),int(p1.real)
        p2row,p2col = int(p2.imag),int(p2.real)
        rowdiff = abs(p1row-p2row)
        coldiff = abs(p1col-p2col)
        for expandedrow in self.emptyrows:
            if min(p1row,p2row) < expandedrow and max(p1row,p2row) > expandedrow:
                rowdiff+=self.expansion-1
        for expandedcol in self.emptycols:
            if min(p1col,p2col) < expandedcol and max(p1col,p2col) > expandedcol:
                coldiff+=self.expansion-1
        return rowdiff + coldiff



def part1(inputdata=test_input):
    m=Map(inputdata,2)
    return m.calc_all_dist()


def part2(inputdata=test_input):
    m=Map(inputdata,1000000)
    return m.calc_all_dist()

def day11_01():
    """Run part 1 of Day 7's code"""
    path = "./input/11.txt"
    print("1101:", part1(file_to_str_array(path)))


def day11_02():
    """Run part 2 of Day 1's code"""
    path = "./input/11.txt"
    print("1102:", part2(file_to_str_array(path)))


if __name__ == "__main__":
    day11_01()
    day11_02()

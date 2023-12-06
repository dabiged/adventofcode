from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

test_input='''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

class Mapping():
    def __init__(self,source,dest,data):
        self.source=source
        self.dest=dest
        self.data=data


    def get_dest(self,source):
        for row in self.data:
            vals=row.split()
            deststart=int(vals[0])
            sourcestart=int(vals[1])
            count=int(vals[2])
            offset=source- sourcestart
            if 0 <= offset < count:
                return deststart+offset
        return source

    def get_source(self,dest):
        for row in self.data:
            vals=row.split()
            deststart=int(vals[0])
            sourcestart=int(vals[1])
            count=int(vals[2])
            offset=dest - deststart
            if 0 <= offset < count:
                return sourcestart+offset
        return dest

    def __str__(self):
        return f''

class BulkMapping:
    def __init__(self,inputdata):
        self.seeds=[]
        self.dest_map={}
        self.source_map={}
        for block in inputdata.split('\n\n'):
            if 'seeds:' in block:
                self.seeds=[int(i) for i in block.split()[1:]]
            else:
                data=[]
                for i,row in enumerate(block.split('\n')):
                    if i == 0:
                        firstrow=row.split('-to-')
                        source=firstrow[0]
                        dest=firstrow[1].split()[0]
                    else:
                        data.append(row)
                self.dest_map[source]=Mapping(source,dest,data)
                self.source_map[dest]=Mapping(source,dest,data)

    def lookup_dest(self,seed:int,currloc):
        return self.dest_map[currloc].get_dest(seed),self.dest_map[currloc].dest

    def lookup_source(self,seed:int,currloc):
        return self.source_map[currloc].get_source(seed),self.source_map[currloc].source

    def get_seed_from_location(self,location):
        currloc='location'
        while currloc != 'seed':
            newval,newloc=self.lookup_source(location,currloc)
            location,currloc = newval,newloc
        return location

    def get_location_from_seed(self,seed):
        currloc='seed'
        while currloc != 'location':
            newval,newloc=self.lookup_dest(seed,currloc)
            seed,currloc = newval,newloc
        return seed

def part1(inputdata=test_input):
    mybm=BulkMapping(inputdata)
    finallocs=[]
    for seed in mybm.seeds:
        finallocs.append(mybm.get_location_from_seed(seed))
    return min(finallocs)


def part2(inputdata=test_input):
    mybm=BulkMapping(inputdata)
    ranges =  list(zip(mybm.seeds[::2], mybm.seeds[1::2]))

    startinglocation=148041800
    #startinglocation=0
    done=False
    while not done:
        if startinglocation % 10000 ==0:
            print(startinglocation)
        location=startinglocation
        seed_value=mybm.get_seed_from_location(location)
        for minval,count in ranges:
            if minval <= seed_value < (minval+count):
                done=True
                break
        if not done:
            startinglocation+=1
    return startinglocation




def day05_01():
    """Run part 1 of Day 5's code"""
    path = "./input/05.txt"
    print("0501:", part1("\n".join(file_to_str_array(path))))


def day05_02():
    """Run part 2 of Day 1's code"""
    path = "./input/05.txt"
    print("0502:", part2("\n".join(file_to_str_array(path))))

if __name__ == "__main__":
    day05_01()
    day05_02()

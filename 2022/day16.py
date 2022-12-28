from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

from itertools import combinations

test_input='''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''.split('\n')

class Valve():
    def __init__(self,name,flow,neighbours):
        self.name=name
        self.flow=flow
        self.count=0
        self.neighbours=neighbours
    def __repr__(self):
        return f'Valve: Flow: {self.flow}; Neighbours: {self.neighbours}; Count {self.count}'


def parse_input(input_data):
    output={}
    for line in input_data:
        name=line.split()[1]
        rate=line.split()[4]
        rate=rate.replace(';','').split('=')[-1]
        valves=line.split('valve')[-1].lstrip('s ').split(', ')
        output[name]=Valve(name,rate,valves)
    return output

valves=parse_input(test_input)


def min_dist(from_valve,to_valve,valve_map):
    for valve in valve_map.values():
        valve.count=0
    seen=set()
    tocheck=[(0,valve_map[from_valve])]

    while len(tocheck):
        dist,valve=tocheck.pop(0)
        if valve.name in seen:
            continue
        seen.add(valve.name)
        if valve == valve_map[to_valve]:
            return dist
        for valve in valve.neighbours:
            tocheck.append((dist+1,valve_map[valve]))

print(min_dist('AA','HH',parse_input(test_input)))
print(min_dist('AA','AA',parse_input(test_input)))
print(min_dist('AA','EE',parse_input(test_input)))


NZvalves=[]
for k,v in valves.items():
    if int(v.flow) >0:
        NZvalves.append(k)

all_dists={}
for pair in combinations(NZvalves,2):
    all_dists[tuple(pair)]=min_dist(pair[0],pair[1],valves)

print(all_dists)


def day16_01():
    """Run part 1 of Day 16's code"""
    path = "./input/input_16.txt"
    print("1601:")

def day16_02():
    """Run part 2 of Day 16's code"""
    path = "./input/input_16.txt"
    print("1602:")

if __name__ == "__main__":
    day16_01()
    day16_02()

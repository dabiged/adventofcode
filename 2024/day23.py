from lib.filehelper import file_to_str_array
from collections import defaultdict
# pylint: disable=missing-module-docstring

pairs=[]
testdata='''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''



def part1(inputdata=testdata.split('\n')):
    clique_3=set()
    pairs=[]
    for i in inputdata:
        pairs.append(i)
    for i,pair1 in enumerate(pairs):
        p1n1=pair1.split('-')[0]
        p1n2=pair1.split('-')[1]
        for j,pair2 in enumerate(pairs[i+1:]):
            p2n1=pair2.split('-')[0]
            p2n2=pair2.split('-')[1]
            if   p1n2 == p2n1:
                if p1n1+'-'+p2n2 in pairs or p2n2+'-'+p1n1 in pairs:
                    if p1n1[0] == 't' or p2n1[0] == 't' or p2n2[0] == 't' or p1n2[0] == 't':
                        clique_3.add(tuple(sorted([p1n1,p1n2,p2n2])))
            elif p1n1 == p2n1:
                if p1n2+'-'+p2n2 in pairs or p2n2+'-'+p1n2 in pairs:
                    if p1n1[0] == 't' or p2n1[0] == 't' or p2n2[0] == 't' or p1n2[0] == 't':
                        clique_3.add(tuple(sorted([p1n1,p1n2,p2n2])))
            elif p1n2 == p2n2:
                if p1n1+'-'+p2n1 in pairs or p2n1+'-'+p1n1 in pairs:
                    if p1n1[0] == 't' or p2n1[0] == 't' or p2n2[0] == 't' or p1n2[0] == 't':
                        clique_3.add(tuple(sorted([p1n1,p1n2,p2n1])))
    return len(clique_3)
                


def part2(inputdata=testdata.split('\n')):
    graph=defaultdict(set)
    for i in inputdata:
        n1=i.split('-')[0]
        n2=i.split('-')[1]
        graph[n1].add(n2)
        graph[n2].add(n1)


    def bron_kerbosh(selected, candidates, excluded):
        '''
        https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm#Without_pivoting
        '''
        if not candidates and not excluded:
            return selected
        max_clique=set()
        for vertex in candidates.copy():
            clique=bron_kerbosh(selected.union({vertex}),
                                 candidates.intersection(graph[vertex]),
                                 excluded.intersection(graph[vertex])
                                 )
            max_clique = max(max_clique,clique,key=len)
            candidates.remove(vertex)
            excluded.add(vertex)
        return max_clique

    max_clique = bron_kerbosh(set(), set(graph),set())
    return ','.join(sorted(max_clique))


def day23_01():
    """Run part 1 of Day 23's code"""
    path = "./input/23.txt"
    print("2301:", part1(file_to_str_array(path)))


def day23_02():
    """Run part 2 of Day 23's code"""
    path = "./input/23.txt"
    print("2302:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day23_01()
    day23_02()

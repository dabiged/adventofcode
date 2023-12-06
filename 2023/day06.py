from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring
from collections import defaultdict

test_input=[
'Time:      7  15   30',
'Distance:  9  40  200'
]


class Boat():
    def __init__(self,distance,totaltime):
        self.distance=distance
        self.totaltime=totaltime

    def wins(self,waittime):
        velocity=waittime
        time_moving=self.totaltime-waittime
        distance_moved=velocity*time_moving
        if distance_moved > self.distance:
            return True
        return False

    def winners(self):
        numwinners=0
        for waittime in range(self.totaltime):
            if self.wins(waittime):
                numwinners+=1
        return numwinners

class BoatRacer():
    def __init__(self,data):
        self.data=data
        self.parse()

    def parse(self):
        self.times=self.data[0].split()[1:]
        self.distances=self.data[1].split()[1:]

    def count_winners(self):
        count=1
        for t,d in zip(self.times,self.distances):
            thisboat=Boat(int(d),int(t))
            count*=thisboat.winners()
        return count

    def __str__(self):
        return f''

def part1(inputdata=test_input):
    myboatracer=BoatRacer(inputdata)
    return myboatracer.count_winners()

def part2(inputdata=test_input):
    modifiedinput=[]
    for row in inputdata:
        row=row.split()
        modifiedinput.append(" ".join([row[0],"".join(row[1:])]))

    myboatracer=BoatRacer(modifiedinput)
    return myboatracer.count_winners()


def day06_01():
    """Run part 1 of Day 1's code"""
    path = "./input/06.txt"
    print("0601:", part1(file_to_str_array(path)))


def day06_02():
    """Run part 2 of Day 1's code"""
    path = "./input/06.txt"
    print("0602:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    day06_01()
    day06_02()

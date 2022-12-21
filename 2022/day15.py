from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


test_input='''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.split('\n')


def parse(line):
    parts=line.replace('=',' ').replace(':',' ').replace(',',' ').split(" ")
    sx=parts[3]
    sy=parts[6]
    bx=parts[-4]
    by=parts[-1]
    return (int(sx)+int(sy)*1j), (int(bx)+int(by)*1j)


class Map():
    def __init__(self,inputtext):
        self.inputtext=inputtext
        self.sensors=[]
        self.beacons=[]
        self.dists={}
        self.mincol=0
        self.maxcol=0
        self.minrow=0
        self.maxrow=0
        self.parse()

    def checkline(self,ycoord):
        count=0
        for realcoord in range(self.mincol,self.maxcol):
            if self.inrange(realcoord+ycoord*1j):
                count+=1
        return count

    def parse(self):
        for line in self.inputtext:
            s_loc, b_loc = parse(line)
            self.sensors.append(s_loc)
            self.beacons.append(b_loc)

            dist=int(abs((s_loc-b_loc).real)+abs((s_loc-b_loc).imag))

            self.dists[s_loc]=dist

            self.mincol=min(self.mincol,int(s_loc.real-dist))
            self.maxcol=max(self.maxcol,int(s_loc.real+dist))
            self.minrow=min(self.minrow,int(s_loc.imag-dist))
            self.maxrow=max(self.maxrow,int(s_loc.imag+dist))

    def inrange(self,point):
        for s_loc,dist in self.dists.items():
            if point in self.beacons or point in self.sensors:
                return False
            if int(abs((s_loc-point).real)) + int(abs((s_loc-point).imag)) <= dist:
                return True
        return False

    def empty(self,point):
        for s_loc,dist in self.dists.items():
            if point in self.beacons or point in self.sensors:
                return False
            if int(abs((s_loc-point).real)) + int(abs((s_loc-point).imag)) <= dist:
                return False
        return True

    def halo(self,sensor):
        halo=[]
        x=int(sensor.real)
        y=int(sensor.imag)
        # Start at east point.
        #coord=sensor+self.dists[sensor]+1
        # travel down and left
        #inc=-1+1j
        #while coord not in halo:
        #    halo.append(coord)
        #    if int(coord.imag) - int(sensor.imag) > 0 and int(coord.real)==int(sensor.real):
        #        # up and left
        #        inc=-1-1j
        #    elif int(coord.real) - int(sensor.real) < 0 and int(coord.imag)==int(sensor.imag):
        #        # up and right
        #        inc=1-1j
        #    elif int(coord.imag) - int(sensor.imag) < 0 and int(coord.real)==int(sensor.real):
        #        inc=1+1j
        #    coord+=inc
        d=self.dists[sensor]+1
        halo.append([ x+d-i+(y+i)*1j for i in range(d+1) ])
        halo.append([ x-d+i+(y-i)*1j for i in range(d+1) ])
        halo.append([ x-d+i+(y+i)*1j for i in range(d+1) ])
        halo.append([ x+d-i+(y-i)*1j for i in range(d) ])
        return [loc for part in halo  for loc in part if int(loc.real) < 4_000_000 and int(loc.imag)<=4_000_000 ]


    def part2(self,boundary=20):
        self.sensorboundaries={}
        for i, sensor1 in enumerate(self.sensors):
            for j,sensor2 in enumerate(self.sensors[i+1:]):
                for sensor in [sensor1, sensor2]:
                    if sensor not in self.sensorboundaries.keys():
                        self.sensorboundaries[sensor]=self.halo(sensor)
                overlap=set(self.sensorboundaries[sensor1]).intersection(set(self.sensorboundaries[sensor2]))

                for loc in list(overlap):
                    if 0 > int(loc.real) or int(loc.real) > boundary or 0 > int(loc.imag) or int(loc.imag) > boundary:
                        continue
                    if self.empty(loc):
                        return int(loc.real)*4_000_000+int(loc.imag)


def day15_01():
    """Run part 1 of Day 9's code"""
    path = "./input/input_15.txt"
    print("1501:",Map(file_to_str_array(path)).checkline(2_000_000))

def day15_02():
    """Run part 2 of Day 9's code"""
    path = "./input/input_15.txt"
    print("1502:",Map(file_to_str_array(path)).part2(boundary=4_000_000))

if __name__ == "__main__":
    day15_01()
    day15_02()

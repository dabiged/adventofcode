from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

import json

test_data='''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''.split('\n')

def parse(inputtext):
    inputdata=[]
    for row in inputtext:
        k=int(row.split(',')[0])
        v=int(row.split(',')[1])
        x=int(row.split(',')[2])
        inputdata.append((k,v,x))
    return inputdata

def calculate1(all_cubes):

    totalsides=0
    for cube in all_cubes:
        x,y,z=cube
        totalsides+=6
        if (x+1,y,z) in all_cubes:
            totalsides+= -1
        if (x-1,y,z) in all_cubes:
            totalsides+= -1
        if (x,y+1,z) in all_cubes:
            totalsides+= -1
        if (x,y-1,z) in all_cubes:
            totalsides+= -1
        if (x,y,z+1) in all_cubes:
            totalsides+= -1
        if (x,y,z-1) in all_cubes:
            totalsides+= -1
    return totalsides

def calculate2(all_cubes):
    minx,miny,minz=99999,999999,99999
    maxx,maxy,maxz=-99999,-999999,-999999    
    for cube in all_cubes:
        minx=min(minx,cube[0])
        miny=min(miny,cube[1])
        minz=min(minz,cube[2])
        maxx=max(maxx,cube[0])
        maxy=max(maxy,cube[1])
        maxz=max(maxz,cube[2])


    minx+=-1
    miny+=-1
    minz+=-1
    maxx+=2
    maxy+=2
    maxz+=2

    visited=set()
    outside_faces=0
    steam=[]
    steam.append((minx,miny,minz))

    while steam:
        (x,y,z)=steam.pop()
        if (x,y,z) not in visited:
            visited.add((x,y,z))
            for newx,newy,newz in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
                if (newx,newy,newz) in visited:
                    continue
                elif (newx,newy,newz) in all_cubes:
                    outside_faces+=1
                elif newx <= maxx and newx >= minx and newy <= maxy and newy >= miny and newz <= maxz and newz >= minz:
                    steam.append((newx,newy,newz))
    
    return outside_faces



def day18_01():
    """Run part 1 of Day 18's code"""
    path = "./input/input_18.txt"
    print("1801:",calculate1(parse(file_to_str_array(path))))

def day18_02():
    """Run part 2 of Day 18's code"""
    path = "./input/input_18.txt"
    print("1802:",calculate2(parse(file_to_str_array(path))))

if __name__ == "__main__":
    day18_01()
    day18_02()


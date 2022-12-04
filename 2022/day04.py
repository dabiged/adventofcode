from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

test_data='''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.split('\n')




def main1(data):
    numoverlap=0
    for row in data:
        pairs=row.split(',')
        pair1range,pair2range = pairs[0],pairs[1]
        if check_inside(pair1range, pair2range):
            numoverlap+=1
    return numoverlap

def main2(data):
    numoverlap=0
    for row in data:
        pairs=row.split(',')
        pair1range,pair2range = pairs[0],pairs[1]
        if check_anyoverlap(pair1range, pair2range):
            numoverlap+=1
    return numoverlap
        

        

def check_inside(range1,range2):
    min1,max1 = range1.split('-')
    min2,max2 = range2.split('-')
    ids_1=set([i for i in range(int(min1),int(max1)+1)])
    ids_2=set([i for i in range(int(min2),int(max2)+1)])
    if ids_1.intersection(ids_2) == ids_1 or ids_1.intersection(ids_2) == ids_2:
        return True
    return False

def check_anyoverlap(range1,range2):
    min1,max1 = range1.split('-')
    min2,max2 = range2.split('-')
    ids_1=set([i for i in range(int(min1),int(max1)+1)])
    ids_2=set([i for i in range(int(min2),int(max2)+1)])
    if len(ids_1.intersection(ids_2)) > 0 :
        return True
    return False


def day04_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_04.txt"
    print("0401:", main1(file_to_str_array(path)))

def day04_02():
    """Run part 4 of Day 1's code"""
    path = "./input/input_04.txt"
    print("0402:", main2(file_to_str_array(path)))

if __name__ == "__main__":
    day04_01()
    day04_02()

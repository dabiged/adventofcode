from lib.filehelper import file_to_array
# pylint: disable=missing-module-docstring

import copy

test_data='''1
2
-3
3
-2
0
4'''.split('\n')




def decode(enc,out):
    for num in enc:
        i,val = num
        currpos=out.index(num)
        if num==0:
            continue
        del out[currpos]
        newpos=currpos+val
        newpos=newpos%len(out)
        if newpos<=0:
            newpos+=len(out)
        out.insert(newpos,num)
    return out


def parse(inputtext,key):
    output=[]
    for i,val in enumerate(inputtext):
        if val==0:
            zeroval=(i,int(val))
        output.append((i,int(val)*key))
    return output,zeroval


def getnth(data,item,n):
    loc=data.index(item)
    loc+=n
    loc%=len(data)
    return data[loc]



def main1(input_data):
    output,zeroval=parse(input_data,key=1)
    encrypted=copy.deepcopy(output)
    output=decode(encrypted,output)
    return getnth(output,zeroval,1000)[1]+getnth(output,zeroval,2000)[1]+getnth(output,zeroval,3000)[1]





def main2(input_data):
    output,zeroval=parse(input_data,key=811589153)
    encrypted=copy.deepcopy(output)
    for i in range(10):
        output=decode(encrypted,output)
    return getnth(output,zeroval,1000)[1]+getnth(output,zeroval,2000)[1]+getnth(output,zeroval,3000)[1]

def day20_01():
    """Run part 1 of Day 20's code"""
    path = "./input/input_20.txt"
    print("2001:", main1(file_to_array(path)))

def day20_02():
    """Run part 2 of Day 20's code"""
    path = "./input/input_20.txt"
    print("2002:", main2(file_to_array(path)))

if __name__ == "__main__":
    day20_01()
    day20_02()


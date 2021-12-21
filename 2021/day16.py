"""
AOC day 16 2018
"""
from lib.filehelper import file_to_str_array
from collections import deque, defaultdict
from copy import deepcopy


def convertH2B(hexstr):
    outputstr=''
    for char in hexstr:
        outputstr+=str(bin(int(char,16))[2:]).zfill(4)
    return outputstr

def convertB2D(binarystring):
    return int(binarystring,2)

#class PacketDecoder():
#    def __init__(self,inputstring):
#        self.inputstring=inputstring
#        self.pointer=0
#        self.version=0
#        self.packettypeid=0
#        self.binstr=convertH2B(self.inputstring)
#        self.decode_header()
#
#    def decode_header(self):
#        self.version=convertB2D(self.binstr[self.pointer:self.pointer+3])
#        self.pointer+=3
#        self.packettypeid=convertB2D(self.binstr[self.pointer:self.pointer+3])
#        self.pointer+=3
#
#    def read_literal(self):
#        done=False
#        binaryvalue=''
#        while not done:
#            if self.binstr[self.pointer] == '0':
#                done =True
#            binaryvalue+=str(self.binstr[self.pointer+1:self.pointer+5])
#            self.pointer+=5
#        return convertB2D(binaryvalue)
#
#    def read_operator(self):
#        self.lengthtypeid=self.binstr[self.pointer]
#        self.pointer+=1
#
#        if self.lengthtypeid == 0:
#            self.subpacketlength=convertB2D(self.binstr[self.pointer,self.pointer+15])
#            self.pointer+=15
#            startpacketloc=deepcopy(self.pointer)
#
#            while self.pointer < startpacketloc+self.subpacketlength:
#                
#        elif self.lengthtypeid == 1:
#            self.numsubpacket=convertB2D(self.binstr[self.pointer,self.pointer+11])
#            self.pointer+=11
#
#        else:
#            raise ValueError(f'Unknown lengthTypeID found')
#
#    def run(self):
#        if self.packettypeid == 4:
#            result=self.read_literal()
#        else:
#            
#            result=
#        return result
#
#    def __repr__(self):
#        return 'Packet: '+self.binstr+'\n  version: '+str(self.version)+'\n  typeid: '+str(self.packettypeid)
#
def day16_01():
    """Run part 1 of Day 16's code"""
    path = "./input/day16.txt"
    result=""
    print(f'1601: {result}')

def day16_02():
    """Run part 2 of Day 16's code"""
    path = "./input/day16.txt"
    result=""
    print(f'1602: {result}')

if __name__ == "__main__":
    day16_01()
    #day16_02()

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

def packetreader(inputstr,location):
    inputstr=convertH2B(inputstr[location:])
    bin_version=inputstr[0:3]
    bin_typeid=inputstr[3:6]
    if convertB2D(bin_typeid) == 4:
        binaryvalue=''
        pointer=6
        while True:
            binaryvalue+=str(inputstr[pointer+1:pointer+5])
            print(binaryvalue)
            if inputstr[pointer] == '0':
                return convertB2D(binaryvalue), pointer+=5
            pointer+=5
    else:
        bin_lengthtypeid= inputstr[7]
        if bin_lengthtypeid =='0':
            bin_length_bits=inputstr[8:24]
            print(convert_B2D(bin_length_bits))
            remlength=convertB2D(bin_length_bits)
            values=[]
            while remlength > 0 :
                value,pointer=packetreader(inputstr, 
                
        elif bin_lengthtypeid=='1':
            bin_num_subpackets=inputstr[8:24]
            print(convert_B2D(bin_num_subpackets))
            startlocation=25
            values=[]
            for packet in range(convert_B2D(bin_num_subpackets)):
                value, pointer=packetreader(inputstr, startlocation)
                values.append(value)
                startlocation+=pointer
        else:
            raise ValueError('Unknown Length typeid')




        
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

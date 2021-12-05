"""
Advent of Code Day 02 2021
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class DiagnosticReport():
    def __init__(self,inputfile):
        self.inputdata=file_to_str_array(inputfile)
        self.read_rows()
        self.read_cols(self.rows)

    def read_rows(self):
        self.rows={}
        for rownum,row in enumerate(self.inputdata):
            self.rows[rownum]=row

    def read_cols(self,rowinput):
        self.columns={}
        for row,line in rowinput.items():
            for i,val in enumerate(line):
                if i not in self.columns.keys():
                    self.columns[i]=''
                self.columns[i]+=val

    def find_most_common(self,mystr,chem='O2'):
        if mystr.count('1') > mystr.count('0'):
            return '1'
        elif mystr.count('1') < mystr.count('0'):
            return '0'
        elif mystr.count('1') == mystr.count('0'):
            return '1'

    def gamma(self):
        output=""
        for binstr in self.columns.values():
            output+=self.find_most_common(binstr)
        return output

    def bin2int(self,inputstr):
        return int(inputstr,2)

    def flip(self,inputstr):
        output=""
        for char in inputstr:
            if char == '1':
                output+='0'
            elif char == '0':
                output+='1'
        return output

    def delta(self):
        return self.flip(self.gamma())

    def power_consumption(self):
        return self.bin2int(self.delta())*self.bin2int(self.gamma())

    def O2_rating(self):
        self.rows={}
        self.read_rows()
        self.read_cols(self.rows)
        for i in range(len(self.columns[0])):
            mostcommon=self.find_most_common(self.columns[i],chem='O2')
            rows_to_delete=[]
            for rownum,row in self.rows.items():
                if row[i] != mostcommon:
                    rows_to_delete.append(rownum)
            for row in rows_to_delete:
                del(self.rows[row])
            self.read_cols(self.rows)
            if len(self.rows) == 1:
                for i in self.rows.values():
                    return i 

    def CO2_rating(self):
        self.rows={}
        self.columns={}
        self.read_rows()
        self.read_cols(self.rows)
        for i in range(len(self.columns[0])):
            mostcommon=self.find_most_common(self.columns[i],chem='CO2')
            rows_to_delete=[]
            for rownum,row in self.rows.items():
                if row[i] == mostcommon:
                    rows_to_delete.append(rownum)
            for row in rows_to_delete:
                del(self.rows[row])
            self.read_cols(self.rows)
            if len(self.rows) == 1:
                for i in self.rows.values():
                    return i 

    def life_support_rating(self):
        O2 = self.O2_rating()
        CO2=self.CO2_rating()
        return self.bin2int(self.O2_rating())*self.bin2int(self.CO2_rating())

def day03_01():
    """Run part 1 of Day 2's code"""
    inputfile = "./input/day03.txt"
    myreport=DiagnosticReport(inputfile)
    result=myreport.power_consumption()
    print(f'0301: {result} is the power consumption of the submarine')

def day03_02():
    """Run part 2 of Day 2's code"""
    inputfile = "./input/day03.txt"
    myreport=DiagnosticReport(inputfile)
    result=myreport.life_support_rating()
    print(f'0302: {result} is the life support rating of the submarine')

if __name__ == "__main__":
    day03_01()
    day03_02()

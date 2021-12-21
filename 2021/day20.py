"""
AOC day 20 2018
"""
from lib.filehelper import file_to_str_array
from collections import deque, defaultdict
# pylint: disable=missing-module-docstring

def sym2bin(inputstr):
    return inputstr.replace("#","1").replace(".","0")

def bin2dec(inputstr):
    return int(inputstr,2)


class Image():
    def __init__(self,inputfile):
        self.inputfile=inputfile
        self.code=''
        self.pattern=defaultdict(lambda: '.')

        self.processinputfile()

    def processinputfile(self):
        self.input=file_to_str_array(self.inputfile)
        self.code=self.input[0]
        for row,line in enumerate(self.input[2:]):
            for col,char in enumerate(line):
                self.pattern[(row,col)]=char


    def enhance(self):
        newImage=defaultdict(lambda: '.')
        for loc,symbol in self.pattern.items():
            row,col=loc
            symbol=''
            for drow in range(-1,2):
                for dcol in range(-1,2):
                    if (row+drow,col+dcol) not in self.pattern.keys():
                        symbol+='.'
                    else:
                        symbol+=self.pattern[(row+drow,col+dcol)]
            newImage[loc]=self.code[bin2dec(sym2bin(symbol))]
        self.pattern=newImage
        print(self.show())

    def countlit(self):
        countlit=0
        for symbol in self.pattern.values():
            if symbol == '#':
                countlit+=1
        return countlit

    def show(self):
        maxrow,maxcol = 0,0
        minrow,mincol = 10000,10000
        for loc in self.pattern.keys():
            row,col = loc
            minrow=min(minrow,row)
            mincol=min(mincol,col)
            maxrow=max(maxrow,row)
            maxcol=max(maxcol,col)

        minrow-=4
        mincol-=4
        maxrow+=4
        maxcol+=4
        output=''
        for row in range(minrow,maxrow+1):
            thisrow=''
            for col in range(mincol,maxcol+1):
                thisrow+=self.pattern[(row,col)]
            output+=thisrow+'\n'
        return output

    


    def part2(self):
        pass



def day20_01():
    """Run part 1 of Day 20's code"""
    myImage=Image('input/day20.txt')
    print(myImage.enhance())
    print(myImage.enhance())
    result=myImage.countlit()
    print(f'2001: {result}')

def day20_02():
    """Run part 2 of Day 20's code"""
    path = "./input/day20.txt"
    result=""
    print(f'2002: {result}')

if __name__ == "__main__":
    day20_01()
    #day20_02()

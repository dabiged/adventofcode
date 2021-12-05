"""
AOC day 05 2021
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Seafloor():
    def __init__(self,inputfile):
        self.list_of_links=file_to_str_array(inputfile)
        self.numrows=-1
        self.numcols=-1
        self.get_board_size()
        self.seafloor={}
        self.initialise_seafloor()

    def __repr__(self):
        seafloor=[]        
        for col in range(self.numcols):
            thisrow=''
            for row in range(self.numrows):
                thisrow+=str(self.seafloor[(row,col)])
            seafloor.append(thisrow)
        return "\n".join(seafloor)

    def process_all(self):
        for link in self.list_of_links:
            self.add_line_all(self.process_row(link))

    def process_flat(self):
        for link in self.list_of_links:
            self.add_line_flat(self.process_row(link))

    def get_duplicates(self):
        num_dupe=0
        for loc,val in self.seafloor.items():
            if val > 1:
                num_dupe+=1
        return num_dupe

    def initialise_seafloor(self):
        for row in range(self.numrows):
            for col in range(self.numcols):
                self.seafloor[(row,col)] = 0

    def add_line_flat(self,lineparams):
        row1,col1,row2,col2 = lineparams

        if row1 == row2 :
            for col in range(min(col1,col2),max(col1,col2)+1):
                self.seafloor[(row1,col)] += 1
        elif col1 == col2 :
            for row in range(min(row1,row2),max(row1,row2)+1):
                self.seafloor[(row,col1)] += 1
        else:
            pass

    def add_line_all(self,lineparams):
        row1,col1,row2,col2 = lineparams

        if row1!=row2 and col1!=col2:
            rowinc=(row2-row1)/abs(row2-row1)
            colinc=(col2-col1)/abs(col2-col1)
            if rowinc == 1:
                if colinc ==1:
                    for row in range(row1,row2+1):
                        for col in range(col1,col2+1):
                            if (row-row1)==(col-col1):
                                self.seafloor[(row,col)]+=1
                elif colinc ==-1:
                    const=row1+col1
                    for row in range(row1,row2+1):
                        for col in range(col2,col1+1):
                            if row+col == const:
                                self.seafloor[(row,col)]+=1
                else:
                    raise ValueError(f'Unexpected col increment {colinc}')
            elif rowinc == -1:
                if colinc ==1:
                    const=row1+col1
                    for row in range(row2,row1+1):
                        for col in range(col1,col2+1):
                            if row+col == const:
                                self.seafloor[(row,col)]+=1
                elif colinc ==-1:
                    for row in range(row2,row1+1):
                        for col in range(col2,col1+1):
                            if (row-row1)==(col-col1):
                                self.seafloor[(row,col)]+=1
            else:
                raise ValueError(f'Unexpected row increment {rowinc}')

        else:
            self.add_line_flat(lineparams)

    def get_board_size(self):
        for row in self.list_of_links:
            row1,col1,row2,col2 = self.process_row(row)
            self.numrows=max(self.numrows,row1)
            self.numrows=max(self.numrows,row2)
            self.numcols=max(self.numcols,col1)
            self.numcols=max(self.numcols,col2)
        self.numrows+=1
        self.numcols+=1

    def process_row(self,row):
        point1,point2 = row.split(" -> ")
        point1 = point1.split(",")
        point2 = point2.split(",")
        return int(point1[0]), int(point1[1]), int(point2[0]), int(point2[1])



def day05_01():
    """Run part 1 of Day 05's code"""
    path = "./input/input_05.txt"
    Myseafloor=Seafloor(path)
    Myseafloor.process_flat()
    result=Myseafloor.get_duplicates()
    print(f'0501: {result}')

def day05_02():
    """Run part 2 of Day 05's code"""
    path = "./input/input_05.txt"
    Myseafloor=Seafloor(path)
    Myseafloor.process_all()
    result=Myseafloor.get_duplicates()
    print(f'0502: {result}')

if __name__ == "__main__":
    day05_01()
    day05_02()

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


testdata='23331331214141314020'

class File:
    def __init__(self,location,length):
        self.location=location
        self.length=length

class FileSystem:
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.disk=[]
        self.files=[]
        self.empty=[]
        self.fileid=0
        location=0
        for i,value in enumerate(map(int,inputdata)):
            if i % 2 == 0:
                self.files.append(File(location,int(value)))
                for j in range(int(value)):
                    self.disk.append(int(self.fileid))
                self.fileid+=1
            else:
                if value>0:
                    self.empty.append(File(location,int(value)))
                for j in range(int(value)):
                    self.disk.append(-1)
            location+=value
                    

    def __str__(self):
        return "".join(self.disk)

    def defrag(self):
        while -1 in self.disk:
            val=self.disk.pop()
            if val != -1:
                self.disk=self.disk[:self.disk.index(-1) ]+[val]+self.disk[self.disk.index(-1)+1:]

    def defrag2(self):
        for file in self.files[::-1]:
            for empty_space in self.empty:
                if empty_space.location >= file.location:
                    # if empty space location is after the file location don't do anything
                    break
                if file.length <= empty_space.length:
                    # if the file fits into the empty space
                    for i in range(file.length):
                        # Adjust the disk structure
                        # move file to empty space
                        self.disk[ empty_space.location + i] = self.disk[ file.location + i ]
                        # set old file location to empty
                        self.disk[ file.location+i] = -1
                    # update the empty space tables.
                    empty_space.location = empty_space.location+file.length
                    empty_space.length = empty_space.length - file.length
                    break

    def checksum(self):
        cksum=0
        for i,val in enumerate(self.disk):
            if val >0:
                cksum+=i*val
        return cksum

def part1(inputdata=testdata):
    a=FileSystem(inputdata)
    a.defrag()
    return a.checksum()

def part2(inputdata=testdata):
    a=FileSystem(inputdata)
    a.defrag2()
    return a.checksum()


def day09_01():
    """Run part 1 of Day 09's code"""
    path = "./input/09.txt"
    print("0901:", part1(file_to_str_array(path)[0]))


def day09_02():
    """Run part 2 of Day 09's code"""
    path = "./input/09.txt"
    print("0902:", part2(file_to_str_array(path)[0]))

if __name__ == "__main__":
    day09_01()
    day09_02()

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


testdata='2333133121414131402'




class FileSystem:
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.disk=[]
        self.fileid=0
        for i,value in enumerate(inputdata):
            if i % 2 == 0:
                for j in range(int(value)):
                    self.disk.append(str(self.fileid))
                self.fileid+=1
            else:
                for j in range(int(value)):
                    self.disk.append('.')
                    

    def __str__(self):
        return "".join(self.disk)

    def defrag(self):
        while '.' in "".join(self.disk):
            val=self.disk.pop()
            if val != '.':
                self.disk=self.disk[:self.disk.index('.') ]+[val]+self.disk[self.disk.index('.')+1:]
            print(self.disk.count('.'))


    def checksum(self):
        cksum=0
        for i,val in enumerate(self.disk):
            cksum+=i*int(val)
        return cksum

class File:
    def __init__ (self,position, fileid, length, isempty,moved=False):
        self.position=position
        self.fileid=fileid
        self.length=length
        self.isempty=isempty

    def __str__(self):
        if self.isempty:
            return f'<Empty: len={self.length}>'
        else:
            return f'<File: id={self.fileid},len={self.length}>'

    def __len__(self):
        return int(self.length)


class FileSystem2:
    def __init__(self,inputdata):
        self.inputdata=inputdata
        self.disk=[]
        self.fileid=0
        self.position=0
        self.skip=-1
        for i,value in enumerate(inputdata):
            if i % 2 == 0:
                self.disk.append(File(self.position,self.fileid,value,False))
                self.fileid+=1
            else:
                if int(value) > 0:
                   self.disk.append(File(self.position,0,value,True))

            for j in range(int(value)):
                self.position+=0
                    

    def __str__(self):
        output='-----\n'
        for file in self.disk:
            output+=str(file)+'\n'
        output+='-----'
        return output

    def defrag_step(self):
        # get the last file.
        thisfile=self.disk.pop(self.skip)

        print(self.skip,thisfile)

        found=False
        if thisfile.isempty:
            # if empty just forget about it.
            self.skip-=1
        else:
            # look for empty space to put it.
            for loc, file in enumerate(self.disk):
                if len(file) > len(thisfile) and file.isempty:
                    # found somewhere to put it, but it is slightly too smal
                    found=True
                    self.disk=self.disk[:loc]+[thisfile]+[File(file.position+len(thisfile),0,len(file)-len(thisfile),True)]+self.disk[loc+1:]
                    break
                elif len(file) == len(thisfile) and file.isempty:
                    # found somewhere and the size matches
                    found=True
                    self.disk=self.disk[:locl]+[thisfile]+self.disk[loc+1:]
                    break
            # if none found, put it back at the end, and skip it.
        if not found:
            if self.skip == -1:
                self.disk.append(thisfile)
            else:
                print('before')
                print(self)
                self.disk=self.disk[:self.skip]+[thisfile]+self.disk[self.skip+1:]
                print('after')
                print(self)
            self.skip-=1






def part1(inputdata=testdata):
    a=FileSystem(inputdata)
    a.defrag()
    print(a.checksum())

    

def part2(inputdata=testdata):
    a=FileSystem2(inputdata)
    print(a)
    a.defrag_step()
    print(a)
    a.defrag_step()
    print(a)
    a.defrag_step()
    print(a)
    a.defrag_step()
    print(a)
    a.defrag_step()
    print(a)
    a.defrag_step()
    print(a)
    a.defrag_step()
    print(a)
    a.defrag_step()
    print(a)
    a.defrag_step()
    print(a)



def day09_01():
    """Run part 1 of Day 09's code"""
    path = "./input/09.txt"
    print("0901:", part1(file_to_str_array(path)[0]))


def day09_02():
    """Run part 2 of Day 09's code"""
    path = "./input/09.txt"
    print("0902:", part2(file_to_str_array(path)))

if __name__ == "__main__":
    #part1()
    #day09_01()
    part2()
    #day09_02()

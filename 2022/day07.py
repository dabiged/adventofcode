from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class UnrecognisedInput(Exception):
    pass

class Dir():
    def __init__(self,name,parent):
        self.name=name
        self.parent=parent
        self.files={}
        self.dirs=[]

    def add_file(self,name,size):
        self.files[name]=int(size)

    def add_dir(self,name):
        self.dirs.append(name)

    def get_size(self):
        filesize=sum(self.files.values()) + sum([subdir.get_size() for subdir in self.dirs])
        return filesize

    def up_dir(self):
        return self.parent

    def chdir(self,name):
        return self.dirs[self.dirs.index(name)]

    def __repr__(self):
        if self.parent is None:
            return str(f'Dir({self.name}, dirs:{",".join([dir.name for dir in self.dirs])}, files: {";".join(str(k+":"+str(v)) for k,v in self.files.items())}, parent=none)') 
        return str(f'Dir({self.name}, dirs:{",".join([dir.name for dir in self.dirs])}, files: {";".join(str(k+":"+str(v)) for k,v in self.files.items())}, parent={self.parent.name})') 


class FileSystem():
    def __init__(self,inputtext):
        self.inputtext=inputtext
        self.currdir=None
        self.dirsizes={}

    def parse(self):
        self.root=Dir('/',None)
        for line in self.inputtext:
            if line.startswith('$'):
                if line.split()[1] == 'ls':
                    pass
                elif line.split()[1] == 'cd':
                    if line.split()[2] == '/':
                        self.currdir=self.root
                    elif line.split()[2] == '..':
                        self.currdir=self.currdir.up_dir()
                    else:
                        for subdir in self.currdir.dirs:
                            if subdir.name == self.currdir.name+line.split()[2]:
                                self.currdir = subdir
            else:
                parts=line.split()
                dirsize=parts[0]
                name=parts[1]

                if dirsize == 'dir':
                    self.currdir.add_dir(Dir(self.currdir.name+name,self.currdir))
                else:
                    self.currdir.add_file(self.currdir.name+name,dirsize)

        self.get_all_sizes()

    def goto_root(self):
        while self.currdir.name != '/':
            self.currdir = self.currdir.up_dir()

    def get_all_sizes(self):
        self.goto_root()
        queue=[self.currdir]
        while len(queue):
            self.currdir=queue.pop()
            for child_dir in self.currdir.dirs:
                queue.append(child_dir)
            self.dirsizes[self.currdir.name]=self.currdir.get_size()

    def get_dir_size(self,name):
        return self.dirsizes[name]

    def __repr__(self):
        return str(self.currdir)

    def sum_under_100k(self):
        
        sum_under_100k=0
        keys = list(self.dirsizes.keys())
        keys.sort()
        for k in keys:
            v=self.dirsizes[k]
            if v <= 100_000:
                sum_under_100k+=v
        return sum_under_100k

    def cleanup(self):
        sizerequired=30_000_000
        currspace=70_000_000-self.dirsizes["/"]
        neededspace=sizerequired-currspace

        values= list(self.dirsizes.values())
        values.sort()
        for v in values:
            if v > neededspace:
                return v



def main1(data):
    fs=FileSystem(data)
    fs.parse()
    return fs.sum_under_100k()

def main2(data):
    fs=FileSystem(data)
    fs.parse()
    return fs.cleanup()

def day07_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_07.txt"
    print("0701:", main1(file_to_str_array(path)))

def day07_02():
    """Run part 4 of Day 1's code"""
    path = "./input/input_07.txt"
    print("0702:",main2(file_to_str_array(path)))

if __name__ == "__main__":
    day07_01()
    day07_02()

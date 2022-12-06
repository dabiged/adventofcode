from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


class PacketProcessor():
    def __init__(self,packetstream, msglen=4):
        self.packetstream=packetstream
        self.msglen=msglen

    def get_sop_mark(self):
        for i in range(self.msglen-1,len(self.packetstream)):
            thesechars=set()
            for char in self.packetstream[i-self.msglen:i]:
                thesechars.add(char)
            if len(thesechars) == self.msglen:
                return i




def day06_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_06.txt"
    print("0601:", PacketProcessor(file_to_str_array(path)[0]).get_sop_mark())

def day06_02():
    """Run part 4 of Day 1's code"""
    path = "./input/input_06.txt"
    print("0602:", PacketProcessor(file_to_str_array(path)[0],14).get_sop_mark())

if __name__ == "__main__":
    day06_01()
    day06_02()

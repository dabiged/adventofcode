"""
AOC day 13 2018
"""
from sympy.ntheory.modular import crt
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class BusSched:
    #pylint: disable=too-few-public-methods
    ''' A bus schedule to find the best bus to take'''
    def __init__(self, inputdata):
        ''' Store bus frequency and offset in self.buses.
        stroe departure time stamp in departts.'''
        self.buses=[]
        self.departts=0
        for i, line in enumerate(file_to_str_array(inputdata)):
            if i == 0:
                self.departts=int(line)
            elif i == 1:
                self.buses=line.split(',')
            else:
                print('EOF')

    def next_bus(self):
        '''find the best bus to take and return the
        product of it's number with the number of minutes we need to wait'''
        bustimes=[]
        for bus in self.buses:
            if bus !='x':
                bustimes.append(int(bus))
        time=self.departts
        done=False
        while not done:
            time+=1
            for bus in bustimes:
                if time % bus == 0:
                    ourbus=bus
                    done=True
                    break
        return ourbus*(time-self.departts)

class BusSched2:
    #pylint: disable=too-few-public-methods
    '''
    Bus Schedule for the second part of the question.
    '''
    def __init__(self, inputdata):
        """Read in the data and initialise the class

        bus frequency and offsets stored in a dict called self.buses.
        """
        self.buses={}
        for i, line in enumerate(file_to_str_array(inputdata)):
            if i == 0:
                pass
            elif i == 1:
                for key,busnum in enumerate(line.split(',')):
                    self.buses[key]=busnum
    def find_time(self):
        """
        Use the Chinese remainder theorem to find the answer.
        """
        moduli=[]
        remainder=[]
        for key,value in self.buses.items():
            if value != 'x':
                moduli.append(int(value))
                remainder.append(int(value)-int(key))
        return crt(moduli, remainder)[0]


def day13_01():
    """Run part 1 of Day 13's code"""
    path = "./input/13/input.txt"
    mysched=BusSched(path)
    result=mysched.next_bus()
    print(f'1301: Product of bus to take, and minutes waited: {result}')

def day13_02():
    """Run part 2 of Day 13's code"""
    path = "./input/13/input.txt"
    mysched=BusSched2(path)
    result=mysched.find_time()
    print(f'1302: Time where all buses lineup: {result}')

if __name__ == "__main__":
    day13_01()
    day13_02()

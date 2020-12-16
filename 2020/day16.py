"""
AOC day 16 2018
"""
from collections import deque
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Tickets:
    def __init__(self, inputdata):
        ''' read input file into 3 variables'''
        # Rules format: dict[rule_name] = list of values
        self.rules={}
        # myticket format: list of ints
        self.myticket=[]
        # Other ticket format: list of list of ints.
        self.othertickets=[]
        # other ticket by field:key = location, value =set of values
        self.otherticketbyfield={}
        # rules_allowedValues: key=fieldname, value = set of valid values
        self.rules_allowedvalues={}
        # self.mapping is the mapping of field names to locations.
        self.mapping={}

        section='rules'
        for line in inputdata:

            if line.startswith('your ticket:'):
                section =  'your ticket'
            elif line.startswith('nearby tickets'):
                section = 'other tickets'
            elif line.strip() == '':
                pass
            else:
                if section == 'rules':
                    key=line.split(': ')[0]
                    values=line.split(': ')[1].split(' or ')
                    self.rules[key] = values
                elif section == 'your ticket':
                    self.myticket = line.split(',')
                elif section == 'other tickets':
                    self.othertickets.append(line.split(','))
                else:
                    print("Unknown Section found")


    def ticket_scanning_error_rate(self):
        allowed_values=set()
        for rules in self.rules.values():
            for rule in rules:
                minval,maxval = int(rule.split('-')[0]), int(rule.split('-')[1])
                for i in range(minval,maxval+1):
                    allowed_values|=set({str(i)})
        invalid_values=[]
        for ticket in self.othertickets:
            for value in ticket:
                if value not in allowed_values:
                    invalid_values.append(int(value))
        return sum(invalid_values)

    def discard_invalid(self):

        # Build a set of global allowed values for any field
        allowed_values=set()
        for key,rules in self.rules.items():
            thisrule_allowedvalues=set()
            for rule in rules:
                # build a set of values allowed for this fieldname
                minval,maxval = int(rule.split('-')[0]), int(rule.split('-')[1])
                for i in range(minval,maxval+1):
                    allowed_values|=set({str(i)})
                    thisrule_allowedvalues|=set({str(i)})
            self.rules_allowedvalues[key]=thisrule_allowedvalues
        # Check if the current ticket is valid.
        for ticket in self.othertickets:
            valid=True
            for value in ticket:
                if value not in allowed_values:
                    valid=False

            # if ticket is valid add its value to the dict. 
            if valid:
                for fieldnum, value in enumerate(ticket):
                    if fieldnum not in self.otherticketbyfield.keys():
                        self.otherticketbyfield[fieldnum]=set({value})
                    else: 
                        self.otherticketbyfield[fieldnum]|=set({value})

    def decode_fields(self):
        field_queue=deque([])
        for key in self.rules.keys():
            field_queue.append(key)
        # The name to field mapping like {'seat':1, 'row':2}
        name_to_field_mapping={}
        counter=0
        while len(field_queue) >0:
            # get the next field name
            field=field_queue.pop()
            print(field)
            # check if any of the fields match this fields allowed values.
            possible=[]
            for fieldnum in self.otherticketbyfield.keys():
                # all of the values are a match, this field may match)
                if all([ value in self.rules_allowedvalues[field] for value in self.otherticketbyfield[fieldnum]]):
                   possible.append((field,fieldnum))
            #if only one field matched our rule, this is the mapping
            if len(possible) ==1:
                # save it to the output dict.
                name_to_field_mapping[possible[0][0]]=possible[0][1]
                #print(name_to_field_mapping)
                # Remove this field from input
                del(self.otherticketbyfield[possible[0][1]])
            else:
            # otherwise put this field back in the queue and try another.
                field_queue.appendleft(field)
            counter+=1
            if counter >len(self.rules)**2:
                break
        self.mapping = {k:v for k, v in sorted(name_to_field_mapping.items(), key=lambda item: item[1])}
        #print(self.mapping)
        return [k for k, v in sorted(name_to_field_mapping.items(), key=lambda item: item[1])]


    def multiply_departure_fields(self):
        output=1
        for key, value in self.mapping.items():
            if key.startswith('departure'):
                print(key,':',value)
                output*=int(self.myticket[value])
        return output



def day16_01():
    """Run part 1 of Day 16's code"""
    path = "./input/16/input.txt"
    mytickets = Tickets(file_to_str_array(path))
    result= mytickets.ticket_scanning_error_rate()
    print(f'1601: Ticket scanning error rate is:{result}')

def day16_02():
    """Run part 2 of Day 16's code"""
    path = "./input/16/input.txt"
    #path = 'tests/day16_testdata2.txt'
    mytickets=Tickets(file_to_str_array(path))
    mytickets.discard_invalid()
    mytickets.decode_fields()
    result=mytickets.multiply_departure_fields()
    print(f'1602: {result}')

if __name__ == "__main__":
    #day16_01()
    day16_02()

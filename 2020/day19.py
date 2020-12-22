"""
AOC day 19 2018
"""
from itertools import product
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class RegExpComputer:
    def __init__(self, inputdata):
        ''' Read data from file and store internally:
        self.rules:  a dictionary  of rules, with:
            key = rule number
            value = list of str in the rule
        self.messages: a list of strs containing messages '''

        self.rules={}
        self.messages=[]

        for linenum, line in enumerate(inputdata):
            if ':' in line:
                self.rules[int(line.split(': ')[0])] = line.split(': ')[1].strip().replace('"','') 
            elif 'a' in line or 'b' in line:
                self.messages.append(line.strip())
            elif line == '':
                pass
            else:
                print('Unknown input found on line:',linenum)
                print('Input looked like \n',line)
        print(self.rules)


    def check_one_message(self,message):
        '''
        Check one message against all rules to see if it is valid.d
        '''
        # find all single chars and replace references to them with their values.
        thisstep_alpha={}
        for rulenum, rule in self.rules.items():
            if all([ char == '|' or char == ' ' or char.isalpha() for char in rule]):
                thisstep_alpha[rulenum] = rule
        print(thisstep_alpha)
        for alphanum ,alpha in thisstep_alpha.items():
            print("Running: ", alpha)
            for rulenum, rule in self.rules.items():
                if str(alphanum) in rule :
                    self.rules[rulenum] = rule.replace(str(alphanum),alpha)
            del self.rules[alphanum]
        print(self.rules)



        ##  allowed_msgs=[]
        ##  for rule in self.rules:

        ##  for rule in listofrules:
        ##      look at all rules:
        ##          if any item in any rule is a single character, 
        ##              replace that number with the character in that rule:

        ##      # 0: 4 1 5
        ##      # 1: 2 3 | 3 2
        ##      # 2: 4 4 | 5 5
        ##      # 3: 4 5 | 5 4
        ##      # 4: "a"
        ##      # 5: "b"


        ##      # 0: a 1 b
        ##      # 1: 2 3 | 3 2
        ##      # 2: a a | b b
        ##      # 3: a b | b a

        ##          

def day19_01():
    """Run part 1 of Day 19's code"""
    path = "./input/19/input.txt"
    result=""
    print(f'1901: {result}')

def day19_02():
    """Run part 2 of Day 19's code"""
    path = "./input/19/input.txt"
    result=""
    print(f'1902: {result}')

if __name__ == "__main__":
    day19_01()
    #day19_02()

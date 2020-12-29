"""
AOC day 19 2018
"""
import re
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class RegExpComputer:
    def __init__(self, inputdata):
        ''' Read data from file and store internally:
        self.rules:  a dictionary  of rules, with:
            key = rule number
            value = if tuple => tuple of rules
                    if list of tuples => match either
                    if str match literal.
        self.messages: a list of strs containing messages 

        rule:                         0:4 1 5 : tuple
                                     /|\
                                    / | \
                                   /  |  \
                                  a   1   b
                                      |
                               -------------------
                               /                  \
1: 2 3 | 3 2: list of tuple (2,3)                (3,2)
                             /  \                  /  \
                            /    \                /    \
                           /      \              /      \
2: 4 4 | 5 5             2         \            /        2
3: 4 5 | 5 4            /\          3          3         /\
                       /  \         /\        /\        /  \
                      /    \       /  \      /  \      /    \
4: a str             4 4   5 5  4 5  5 4    4 5 5 4  4 4    5 5
5: b str             | |   | |  | |  | |    | | | |  | |    | |
                     a a   b b  a b  b a    a b b a  a a    b b
        '''
        self.rules={}
        self.messages=[]

        for linenum, line in enumerate(inputdata):
            if ':' in line:
                key ,rule =int(line.split(': ')[0]), line.split(': ')[1]
                # Rule section
                if '|' in line:
                    # An or rule
                    or_rule=[]
                    for subrule in rule.split('|'):
                        or_rule.append(tuple([int(i) for i in subrule.strip().split()]))
                    self.rules[key]=or_rule
                elif '"' in line:
                    # A single Char
                    self.rules[key]=str(rule.replace('"',''))
                else:
                    # A list of rules e.g.  4 1 5
                    self.rules[key]=tuple([int(i) for i in rule.strip().split()])
            elif 'a' in line or 'b' in line:
                # Message section
                self.messages.append(line.strip())
            elif line == '':
                # The blank line separating rules and messages
                pass
            else:
                print('Unknown input found on line:',linenum)
                print('Input looked like \n',line)

    def build_regexp(self,rule=0):
        '''Recursively build a regexp according to rule.
        If the rule contains a str, this is a single char, so return it.
        '''
        if type(self.rules[rule]) is str:
            return self.rules[rule]

        if type(self.rules[rule]) is list:
            options=[]
            for subrule in self.rules[rule]:
                option=''
                for part in subrule:
                    option+=self.build_regexp(rule=part)
                options.append(option)
            return '(' + '|'.join(options)+')'
        if type(self.rules[rule]) is tuple:
            options=[]
            for subrule in self.rules[rule]:
                option=''
                option+=self.build_regexp(rule=subrule)
                options.append(option)
            return '(' + ''.join(options)+')'

    def match(self):
        '''
        count the number of matches.
        '''
        countmatch=0
        regexp=re.compile('^'+self.build_regexp()+'$')
        for message in self.messages:
            if regexp.match(message.rstrip()):
                countmatch+=1
        return countmatch

class RegExpComputerRecursive:
    '''Convert a Normal Choamsky form rule list into a regexp and cound the
    number of matching messages in a list.

    Allows for certain rules to be recursive'''
    def __init__(self, inputdata):
        ''' Read data from file and store internally
        self.rules:  a dictionary  of rules, with:
            key = rule number
            value = if tuple => tuple of rules
                    if list of tuples => match either
                    if str match literal.
        self.messages: a list of strs containing messages 

                rule:                         0:4 1 5 : tuple
                                             /|\
                                            / | \
                                           /  |  \
                                          a   1   b
                                              |
                                       -------------------
                                       /                  \
        1: 2 3 | 3 2: list of tuple (2,3)                (3,2)
                                     /  \                  /  \
                                    /    \                /    \
                                   /      \              /      \
        2: 4 4 | 5 5             2         \            /        2
        3: 4 5 | 5 4            /\          3          3         /\
                               /  \         /\        /\        /  \
                              /    \       /  \      /  \      /    \
        4: a str             4 4   5 5  4 5  5 4    4 5 5 4  4 4    5 5
        5: b str             | |   | |  | |  | |    | | | |  | |    | |
                             a a   b b  a b  b a    a b b a  a a    b b
                '''
        self.rules={}
        self.messages=[]

        for linenum, line in enumerate(inputdata):
            if ':' in line:
                key ,rule =int(line.split(': ')[0]), line.split(': ')[1]
                # Rule section
                if '|' in line:
                    # An or rule
                    or_rule=[]
                    for subrule in rule.split('|'):
                        or_rule.append(tuple([int(i) for i in subrule.strip().split()]))
                    self.rules[key]=or_rule
                elif '"' in line:
                    # A single Char
                    self.rules[key]=str(rule.replace('"',''))
                else:
                    # A list of rules e.g.  4 1 5
                    self.rules[key]=tuple([int(i) for i in rule.strip().split()])
            elif 'a' in line or 'b' in line:
                # Message section
                self.messages.append(line.strip())
            elif line == '':
                # The blank line separating rules and messages
                pass
            else:
                print('Unknown input found on line:',linenum)
                print('Input looked like \n',line)

        self.rules[8] = [(42),(42,8)]
        self.rules[11] = [(42,31),(42,11,31)]

    def build_regexp(self,rule=0):
        '''Recursively build a regexp according to rule.
        If the rule contains a str, this is a single char, so return it.
        if the rule is a list, make an or statement of each subrule.
        if the rule is a tuple, it is just a concatenated series of rules.
        '''
        if rule ==8:
            # rule 8 translates to: match one or more of rule 42.
            # Use the regexp '+' for this
            return '('+self.build_regexp(rule=42)+')+'

        if rule == 11:
            # rule 11 translate to:
            #    match ab or aabb or aaabbb or aaaabbbb ...
            # or     a{1}b{1}|a{2}b{2}|a{3}b{3}|a{4}b{4}
            output=''
            for i in range(1,len(max(self.messages, key=len))//2):
                output+=self.build_regexp(rule=42)+'{'+str(i)+'}'+self.build_regexp(rule=31)+'{'+str(i)+'}|'
            # drop the final or char.
            output=output[:-1]
            return '('+output+')'

        if type(self.rules[rule]) is str:
            return self.rules[rule]

        if type(self.rules[rule]) is list:
            options=[]
            for subrule in self.rules[rule]:
                option=''
                for part in subrule:
                    option+=self.build_regexp(rule=part)
                options.append(option)
            return '(' + '|'.join(options)+')'
        if type(self.rules[rule]) is tuple:
            options=[]
            for subrule in self.rules[rule]:
                option=''
                option+=self.build_regexp(rule=subrule)
                options.append(option)
            return '(' + ''.join(options)+')'

    def match(self):
        '''
        count the number of matches.
        '''
        countmatch=0
        regexp=re.compile('^'+self.build_regexp()+'$')
        for message in self.messages:
            if regexp.match(message.rstrip()):
                countmatch+=1
        return countmatch

def day19_01():
    """Run part 1 of Day 19's code"""
    path = "./input/19/input.txt"
    mycomp = RegExpComputer(file_to_str_array(path))
    result=mycomp.match()
    print(f'1901: number of messages that match: {result}')

def day19_02():
    """Run part 2 of Day 19's code"""
    path = "./input/19/input.txt"
    mycomp = RegExpComputerRecursive(file_to_str_array(path))
    result=mycomp.match()
    print(f'1902: number of messages that match: {result}')

if __name__ == "__main__":
    day19_01()
    day19_02()

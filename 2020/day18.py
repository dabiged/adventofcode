"""
AOC day 18 2018
"""
from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class FunnyMath:
    ''' A way to evaluate math expressions using strange precendence.
    precendence is brackets, then left to right'''
    def __init__(self,equation):
        '''Read in equation and store as self.equation, a list'''
        self.equation=list(equation.replace(' ',''))

    @staticmethod
    def calculate(equation):
        #pylint: disable=eval-used
        '''Calculate an equation according to the new algebra
        Note equations must not have brackets!

        equation is a list, returns an int
        '''
        assert ')' not in equation
        assert '(' not in equation
        for key,value in enumerate(equation):
            if key % 2 == 1:
                pass
            elif key == 0:
                answer=value
                # set the answer to the first entry in the bracket free dict
            else:
                # Update the answer by applying the previous operator to the current value.
                answer=str(eval(answer+str(equation[key-1])+str(equation[key])))
        return int(answer)

    def remove_brackets(self):
        #pylint: disable=undefined-loop-variable
        ''' This function modifies self.equation by
        replacing one set of brackets with the evaluated integer'''
        assert '(' in self.equation
        assert ')' in self.equation
        # Example.
        # ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
        openbrakets, closebrakets = [],[]
        for key,value in enumerate(self.equation):
            if value == '(':
                openbrakets.append(key)
            elif value == ')' :
                closebrakets.append(key)
        # Example
        # openbrakets =   [0,  1,  9]
        # closebrackets = [7, 17, 20]
        # take the first close braket symbol.
        endbraket=closebrakets[0]
        # Look backwards through all open bracket locations to the first one
        #  before the first close bracket symbol.
        for startbraket in openbrakets[::-1]:
            if startbraket < endbraket:
                break
        # startbraket = 1
        # end braket = 7
        # Evaluate this section and delete the rest of the bracketed section
        self.equation[startbraket] = str(self.calculate(self.equation[startbraket+1:endbraket]))
        del self.equation[startbraket+1:endbraket+1]

    def run(self):
        ''' Evaluate the equation and return the value'''
        while '(' in self.equation:
            self.remove_brackets()
        return self.calculate(self.equation)

class FunnyMath2:
    ''' A way to evaluate math expressions using strange precendence.
    precendence is brackets, then addition, then multiplication'''
    def __init__(self,equation):
        '''Read in equation and store as self.equation, a list'''
        self.equation=list(equation.replace(' ',''))

    @staticmethod
    def calculate_plus(equation):
        #pylint: disable=eval-used
        '''Calculate an equation according to the new algebra
        Note equations must not have brackets!

        equation is a list, returns an int
        '''
        assert ')' not in equation
        assert '(' not in equation
        # Deal with all the additions.
        while '+' in equation:
            listofpluses=[]
            for key,value in enumerate(equation):
                if value == '+':
                    listofpluses.append(key)
            # Since the removal of list elements causes a renumbering,
            #   start at the end and work backwards.
            for pluslocation in reversed(sorted(listofpluses)):
                equation[pluslocation]=str(eval(equation[pluslocation-1]\
                                            +"+"+equation[pluslocation+1]))
                del equation[pluslocation-1]
                del equation[pluslocation]

        assert '+' not in equation
        # Now do all the multiplications as before.
        for key,value in enumerate(equation):
            if key % 2 == 1:
                pass
            elif key == 0:
                answer=value
                # set the answer to the first entry in the bracket free, addition free equation
            else:
                # Update the answer by applying the previous operator to the current value.
                answer=str(eval(answer+str(equation[key-1])+str(equation[key])))
        return int(answer)

    def remove_brackets(self):
        #pylint: disable=undefined-loop-variable
        ''' This function modifies equationdict representing an equation
        and replaces one set of brackets with the evaluated integers'''
        assert '(' in self.equation
        assert ')' in self.equation
        # Example.
        # ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
        openbrakets, closebrakets = [],[]
        for key,value in enumerate(self.equation):
            if value == '(':
                openbrakets.append(key)
            elif value == ')' :
                closebrakets.append(key)
        # Example
        # openbrakets =   [0,  1,  9]
        # closebrackets = [7, 17, 20]
        # take the first close braket symbol.
        endbraket=closebrakets[0]
        # Look backwards through all open bracket locations to the first one
        #  before the first close bracket symbol.
        for startbraket in openbrakets[::-1]:
            if startbraket < endbraket:
                break
        # startbraket = 1
        # end braket = 7
        # Evaluate this section and delete the rest of the bracketed section
        self.equation[startbraket] = str(self.calculate_plus(\
                                        self.equation[startbraket+1:endbraket]))
        del self.equation[startbraket+1:endbraket+1]

    def run(self):
        '''Solve the equation and return the result'''
        while '(' in self.equation:
            self.remove_brackets()
        return self.calculate_plus(self.equation)

def day18_01():
    """Run part 1 of Day 18's code"""
    path = "./input/18/input.txt"
    result=sum([FunnyMath(inputeqn).run() for inputeqn in file_to_str_array(path)])
    print(f'1801: Sum of all problems in homework: {result}')

def day18_02():
    """Run part 2 of Day 18's code"""
    path = "./input/18/input.txt"
    result=sum([FunnyMath2(inputeqn).run() for inputeqn in file_to_str_array(path)])
    print(f'1802: Sum of all problems in homework with addition precedence: {result}')

if __name__ == "__main__":
    day18_01()
    day18_02()

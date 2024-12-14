from lib.filehelper import file_to_str_array, get_file
import sympy as sym
# pylint: disable=missing-module-docstring


testdata='''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''



def calc_cost(A,B):
    return 3*A+B

def solve(inputdata,delta=0):
    '''
    x,y = sym.symbols('x,y')
    eq1 = sym.Eq(x+y,5)
    eq2 = sym.Eq(x**2+y**2,17)
    result = sym.solve([eq1,eq2],(x,y))
    print(result)
    '''
    for line in inputdata.split('\n'):
        if "Button A:" in line:
            eq1_coefA=int(line.split()[2][1:-1])
            eq2_coefA=int(line.split()[3][1:])
        if "Button B:" in line:
            eq1_coefB=int(line.split()[2][1:-1])
            eq2_coefB=int(line.split()[3][1:])
        if "Prize:" in line:
            eq1_ans=int(line.split()[1][2:-1])+delta
            eq2_ans=int(line.split()[2][2:])+delta

    A,B = sym.symbols('A B')
    eq1 = sym.Eq(eq1_coefA * A + eq1_coefB * B , eq1_ans)
    eq2 = sym.Eq(eq2_coefA * A + eq2_coefB * B , eq2_ans)
    results = sym.solve((eq1,eq2),(A,B))
    if results[A].is_integer and results[B].is_integer:
        if len(results) > 2:
            print(results)
            raise
        return calc_cost(results[A],results[B])
    return 0

def part1(inputdata=testdata.split('\n\n')):
    total_cost=0
    for eqn in inputdata:
        total_cost+=solve(eqn)
    return total_cost

def part2(inputdata=testdata.split('\n\n')):
    total_cost=0
    for eqn in inputdata:
        total_cost+=solve(eqn,delta=10000000000000)
    return total_cost


def day13_01():
    """Run part 1 of Day 13's code"""
    path = "./input/13.txt"
    print("1301:", part1(get_file(path).split('\n\n')))


def day13_02():
    """Run part 2 of Day 13's code"""
    path = "./input/13.txt"
    print("1302:", part2(get_file(path).split('\n\n')))

if __name__ == "__main__":
    day13_01()
    day13_02()

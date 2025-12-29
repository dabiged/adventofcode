from lib.filehelper import file_to_bald_str_array, file_to_str_array
# pylint: disable=missing-module-docstring

testdata='''123 328  51 64 
 45 64  387 23 
  6 98  215 314
                
*   +   *   +  '''

testdata=testdata.split('\n')

def part1(inputdata=testdata):
    parameters=inputdata[-1].split()
    line1=inputdata[0].split()
    line2=inputdata[1].split()
    line3=inputdata[2].split()
    line4=inputdata[3].split()

    assert len(line1)==len(line2)
    assert len(line2)==len(line3)
    assert len(line3)==len(line4)
    total=0
    for i,val in enumerate(parameters):
        total+=eval(f'{line1[i]} {parameters[i]} {line2[i]} {parameters[i]} {line3[i]} {parameters[i]} {line4[i]}')
    return total

def part2(inputdata=testdata):
    total=0
    oldval=None
    transpose=[''.join(s) for s in zip(inputdata[0],inputdata[1],inputdata[2],inputdata[3],inputdata[4])]
    evaluate=''
    for i in transpose:
        if '*' in i or '+' in i:
            op=i[-1]
            evaluate=i[:-1]
        elif not i.strip():
            total+=eval(evaluate)
            evaluate=''
        else:
            evaluate+=f'{op}{i}'
    total+=eval(evaluate)

    return total




def day06_01():
    """Run part 1 of Day 06's code"""
    path = "./input/06.txt"
    print("0601:", part1(file_to_str_array(path)))


def day06_02():
    """Run part 2 of Day 06's code"""
    path = "./input/06.txt"
    print("0602:", part2(file_to_bald_str_array(path)))

if __name__ == "__main__":
    day06_01()
    day06_02()

from lib.filehelper import file_to_bald_str_array
# pylint: disable=missing-module-docstring

test_data='''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split('\n')

def showcargo(row):
    i=0
    while i < len(row):
        yield row[i:i+3]
        i+=4

def generate_stacks(stacks):
    stackdef={}
    stacks.reverse()
    for i,row in enumerate(stacks):
        if i == 0:
            for stackname in row.split():
                stackdef[stackname]=[]
        else:
            for stack,cargo in enumerate(showcargo(row)):
                if cargo != '   ':
                    stackdef[str(stack+1)].append(cargo)
    return stackdef


def parse_input(data):
    columndef=data[:data.index("")]
    instructions=data[data.index("")+1:]
    return instructions, columndef



def main1(data):
    instrs, init = parse_input(data)
    stacks= generate_stacks(init)
    for instr in instrs:
        inst=instr.split()
        num_move=int(inst[1])
        from_move=inst[3]
        to_move=inst[5]
        for i in range(num_move):
            stacks[to_move].append(stacks[from_move].pop())

    output=''
    for cargo in stacks.values():
        output+=cargo.pop().replace('[','').replace(']','')
    return output

def main2(data):
    instrs, init = parse_input(data)
    stacks= generate_stacks(init)
    for instr in instrs:
        inst=instr.split()
        num_move=int(inst[1])
        from_move=inst[3]
        to_move=inst[5]
        bufferlist=[]
        for i in range(num_move):
            bufferlist.append(stacks[from_move].pop())
        bufferlist.reverse()
        for i in bufferlist:
            stacks[to_move].append(i)

    output=''
    for cargo in stacks.values():
        output+=cargo.pop().replace('[','').replace(']','')
    return output


def day05_01():
    """Run part 1 of Day 1's code"""
    path = "./input/input_05.txt"
    print("0501:", main1(file_to_bald_str_array(path)))

def day05_02():
    """Run part 4 of Day 1's code"""
    path = "./input/input_05.txt"
    print("0502:", main2(file_to_bald_str_array(path)))

if __name__ == "__main__":
    day05_01()
    day05_02()

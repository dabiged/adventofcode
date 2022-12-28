from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring


def newshape():
    shape0=['####']
    shape1=['.#.','###','.#.']
    shape2=['..#','..#','###']
    shape3=['#','#','#','#']
    shape4=['##','##']
    shapes=[shape0,shape1,shape2,shape3,shape4]
    i=-1
    while True:
        i+=1
        shapenum=i%len(shapes)
        yield shapes[i%len(shapes)]
i=-1
for shape in newshape():
    i+=1
    print("")
    print("\n".join(shape))
    if i >5:
        break


def day17_01():
    """Run part 1 of Day 9's code"""
    path = "./input/input_17.txt"
    print("1701:")

def day17_02():
    """Run part 2 of Day 9's code"""
    path = "./input/input_17.txt"
    print("1702:")

if __name__ == "__main__":
    day17_01()
    day17_02()

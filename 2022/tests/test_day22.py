from day22 import Maze
from lib.filehelper import get_bald_string_list_from_file

path = "./input/input_22.txt"

class TestDay01:
    def test_a1(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=1j
        mymaze.currloc=60+149j
        mymaze.walk('1')
        print(mymaze.maze[49+160j])
        assert mymaze.currloc==49+160j
        assert mymaze.direction == -1

    def test_a2(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=1
        mymaze.currloc=49+162j
        mymaze.walk('1')
        print(mymaze.maze[62+149j])
        assert mymaze.currloc==62+149j
        assert mymaze.direction == -1j

    def test_b1(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=-1
        mymaze.currloc=50+60j
        mymaze.walk('1')
        print(mymaze.maze[10+100j])
        assert mymaze.currloc==10+100j
        assert mymaze.direction == 1j

    def test_b2(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=-1j
        mymaze.currloc=10+100j
        mymaze.walk('1')
        print(mymaze.maze[50+60j])
        assert mymaze.currloc==50+60j
        assert mymaze.direction == 1

    def test_c1(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=1j
        mymaze.currloc=110+49j
        mymaze.walk('1')
        print(mymaze.maze[99+60j])
        assert mymaze.currloc==99+60j
        assert mymaze.direction == -1

    def test_c2(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=1
        mymaze.currloc=99+60j
        mymaze.walk('1')
        print(mymaze.maze[110+49j])
        assert mymaze.currloc==110+49j
        assert mymaze.direction == -1j

    def test_d1(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=1
        mymaze.currloc=149+10j
        mymaze.walk('1')
        print(mymaze.maze[139j+99])
        assert mymaze.currloc==139j+99
        assert mymaze.direction == -1

    def test_d2(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=1
        mymaze.currloc=139j+99
        mymaze.walk('1')
        print(mymaze.maze[149+10j])
        assert mymaze.currloc==149+10j
        assert mymaze.direction == -1

    def test_e1(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=-1j
        mymaze.currloc=0j+112
        mymaze.walk('1')
        print(mymaze.maze[12+199j])
        assert mymaze.currloc==12+199j
        assert mymaze.direction == -1j

    def test_e2(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=1j
        mymaze.currloc=12+199j
        mymaze.walk('1')
        print(mymaze.maze[112+0j])
        assert mymaze.currloc==112+0j
        assert mymaze.direction == 1j

    def test_f1(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=-1j
        mymaze.currloc=0j+62
        mymaze.walk('1')
        print(mymaze.maze[0+162j])
        assert mymaze.currloc==0+162j
        assert mymaze.direction == 1

    def test_f2(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=-1
        mymaze.currloc=0+162j
        mymaze.walk('1')
        print(mymaze.maze[62+0j])
        assert mymaze.currloc==62+0j
        assert mymaze.direction == 1j

    def test_g1(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=-1
        mymaze.currloc=50+19j
        mymaze.walk('1')
        print(mymaze.maze[0+130j])
        assert mymaze.currloc==0+130j
        assert mymaze.direction == 1

    def test_g2(self):
        input_data=get_bald_string_list_from_file(path)
        mymaze=Maze(input_data[:-2],input_data[-1])
        mymaze.parse()
        mymaze.parseinstr()
        mymaze.start_walk()
        mymaze.direction=-1
        mymaze.currloc=0+131j
        mymaze.walk('1')
        print(mymaze.maze[50+18j])
        assert mymaze.currloc==50+18j
        assert mymaze.direction == 1

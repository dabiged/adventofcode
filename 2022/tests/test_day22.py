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
        mymaze.direction=-1j
        mymaze.currloc=10+100j
        mymaze.walk('1')
        print(mymaze.maze[50+60j])
        assert mymaze.currloc==50+60j
        assert mymaze.direction == 1

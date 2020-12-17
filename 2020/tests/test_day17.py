from day17 import Conway3D, Conway4D
from lib.filehelper import file_to_str_array


class TestDay17:
    def test_get_all_neighbours(self):
        mygame = Conway3D(file_to_str_array('tests/day17_testdata.txt'))
        neighbourhood = []
        for neighbour in mygame.get_all_neighbours((10,10,10)):
            neighbourhood.append(neighbour)
        assert (9,9,9) in neighbourhood
        assert (10,10,10) not in neighbourhood


    def test_count_neighbours(self):
        mygame = Conway3D(file_to_str_array('tests/day17_testdata.txt'))        
        result=mygame.count_occupied((1,1,0))
        assert result == 5

    def test_step(self):
        mygame = Conway3D(file_to_str_array('tests/day17_testdata.txt'))        
        print(str(mygame))
        mygame.step()
        print(mygame.board)
        result=mygame.count_active()
        assert result == 11

    def test_run_1(self):
        mygame = Conway3D(file_to_str_array('tests/day17_testdata.txt'))        
        result=mygame.run(1)
        assert result == 11

    def test_run_6(self):
        mygame = Conway3D(file_to_str_array('tests/day17_testdata.txt'))        
        result=mygame.run(6)
        assert result == 112


    def test_run_1_4D(self):
        my4dgame = Conway4D(file_to_str_array('tests/day17_testdata.txt'))
        result = my4dgame.run(1)
        print(str(my4dgame))
        assert result == 29

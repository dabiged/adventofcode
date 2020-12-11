from day11 import BoardingLounge
from lib.filehelper import file_to_str_array


class TestDay11:
    def test_init_print(self):
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        expected='L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL\n'
        result = str(testlounge)
        assert expected == result
        assert testlounge.numrows == 10
        assert testlounge.numrows == 10


    def test_occupied(self):
        expected=False
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        result =testlounge.occupied(0,0)
        assert expected == result

    def test_get_neighbors(self):
        expected=0
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        result =testlounge.get_neighbours(0,0)
        assert expected == result

    def test_calc_neighbors(self):
        expected=0
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        testlounge.calc_neighbours()
        result = testlounge.numneighbours[0][0]
        assert expected == result

    def test_update(self):
        expected='#.##.##.##\n#######.##\n#.#.#..#..\n####.##.##\n#.##.##.##\n#.#####.##\n..#.#.....\n##########\n#.######.#\n#.#####.##\n'
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        testlounge.update()
        result= str(testlounge)
        assert result == expected

    def test_two_updates(self):
        expected='#.LL.L#.##\n#LLLLLL.L#\nL.L.L..L..\n#LLL.LL.L#\n#.LL.LL.LL\n#.LLLL#.##\n..L.L.....\n#LLLLLLLL#\n#.LLLLLL.L\n#.#LLLL.##\n'
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        testlounge.update()
        testlounge.update()
        result= str(testlounge)
        assert result == expected

    def test_ten_updates(self):
        expected='#.#L.L#.##\n#LLL#LL.L#\nL.#.L..#..\n#L##.##.L#\n#.#L.LL.LL\n#.#L#L#.##\n..L.L.....\n#L#L##L#L#\n#.LLLLLL.L\n#.#L#L#.##\n'
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        for _ in range(10):
            testlounge.update()
        result= str(testlounge)
        assert result == expected

    def test_n_updates(self):
        expected='#.#L.L#.##\n#LLL#LL.L#\nL.#.L..#..\n#L##.##.L#\n#.#L.LL.LL\n#.#L#L#.##\n..L.L.....\n#L#L##L#L#\n#.LLLLLL.L\n#.#L#L#.##\n'
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        old_state=''
        count=0
        while str(testlounge) != old_state:
            old_state=str(testlounge)
            testlounge.update()
            count+=1
        result=str(testlounge)
        assert result == expected

    def test_calc_neighbors_part2(self):
        expected='#.LL.LL.L#\n#LLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLL#\n#.LLLLLL.L\n#.LLLLL.L#\n'
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        testlounge.update(part=2)
        testlounge.update(part=2)
        result = str(testlounge)
        assert expected == result

    def test_n_updates_part2(self):
        expected='#.L#.L#.L#\n#LLLLLL.LL\nL.L.L..#..\n##L#.#L.L#\nL.L#.LL.L#\n#.LLLL#.LL\n..#.L.....\nLLL###LLL#\n#.LLLLL#.L\n#.L#LL#.L#\n'
        testlounge = BoardingLounge(file_to_str_array('tests/day11_testdata.txt'))
        testlounge.run(part=2)
        result=str(testlounge)
        assert result == expected

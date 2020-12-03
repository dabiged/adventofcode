from day03 import ToboganRun

class TestDay03:
    def test_import_geom_and_print(self):
        expected="""..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#\n"""
        testinput=["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]
        myrun=ToboganRun(testinput,repeats=1)
        result=str(myrun)
        assert myrun.numrows() == 11
        assert myrun.numcols() == 11
        print(result)
        print(expected)
        assert expected == result

    def test_treecount(self):
        testinput=["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]
        expected=7
        myrun=ToboganRun(testinput,repeats=5)
        result=myrun.tree_count(right=3, down=1)
        assert expected == result


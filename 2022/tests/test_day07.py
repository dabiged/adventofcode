from day07 import FileSystem

Test_input='''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.split('\n')

class TestDay07:
    def test_part1(self):
        fs=FileSystem(Test_input)
        fs.parse()
        assert fs.get_dir_size('/ae') == 584
        assert fs.get_dir_size('/a') == 94853
        assert fs.get_dir_size('/d') == 24933642
        assert fs.get_dir_size('/') == 48381165
        
        assert fs.sum_under_100k() == 95437



    def test_part2(self):
        fs=FileSystem(Test_input)
        fs.parse()
        assert 24933642 == fs.cleanup()


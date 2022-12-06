from day06 import PacketProcessor

test1=('mjqjpqmgbljsphdztnvjfqwrcgsmlb',7,19)
test2=('bvwbjplbgvbhsrlpgdmjqwftvncz',5,23)
test3=('nppdvjthqldpwncqszvftbrmjlhg',6,23)
test4=('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',10,29)
test5=('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',11,26)


class TestDay06:
    def test_part1(self):
        for inputstr,ans,_ in [test1, test2, test3, test4, test5]:
            assert ans == PacketProcessor(inputstr).get_sop_mark()

    def test_part2(self):
        for inputstr,_,ans in [test1, test2, test3, test4, test5]:
            assert ans == PacketProcessor(inputstr,14).get_sop_mark()

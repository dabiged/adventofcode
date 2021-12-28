from day25 import *
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class TestDay25:
    # pylint: disable=missing-module-docstring
    def test_moveeast(self):
        myboard=Board(['...>>>>>...'])
        myboard.step()
        myboard.step()
        assert str(myboard) == '...>>>.>.>.\n'

    def test_moveboth(self):
        testboard=Board(['..........','.>v....v..','.......>..','..........'])
        testboard.step()
        print(testboard)
        expected='..........\n.>........\n..v....v>.\n..........\n'
        #print(expected)
        assert str(testboard) == expected

    def test_wrap(self):
        testboard=Board(['...>...','.......','......>','v.....>','......>','.......','..vvv..'])
        testboard.step()
        print(testboard)
        expected='..vv>..\n.......\n>......\nv.....>\n>......\n.......\n....v..\n'
        print(expected)
        assert str(testboard) == expected


    def test_counter(self):
        myboard=Board(['...>>>>>...'])
        count=myboard.step()
        assert count == 2

    def test_run(self):
        myboard=Board(['v...>>.vv>','.vv>>.vv..','>>.>v>...v','>>v>>.>.v.','v>v.vv.v..','>.>>..v...','.vv..>.>v.','v.v..>>v.v','....v..v.>'        ])
        result=myboard.run()
        assert result == 58

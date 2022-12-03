from day07 import ProgramStack

testinput=[
"pbga (66)",
"xhth (57)",
"ebii (61)",
"havc (66)",
"ktlj (57)",
"fwft (72) -> ktlj, cntj, xhth",
"qoyq (66)",
"padx (45) -> pbga, havc, qoyq",
"tknk (41) -> ugml, padx, fwft",
"jptl (61)",
"ugml (68) -> gyxo, ebii, jptl",
"gyxo (61)",
"cntj (57)"
]


class TestDay07:
    def test_memory1(self):
        mystack=ProgramStack(testinput)
        assert 'tknk' == mystack.find_bottom()

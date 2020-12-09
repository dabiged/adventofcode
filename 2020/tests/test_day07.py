from day07 import build_dict, bags_that_can_contain_our_bag, bags_in_our_bag
from day07 import bags_could_contain_our_bag_queue
from lib.filehelper import file_to_str_array

class TestDay07:
    def test_build_dict(self):
        testinput=file_to_str_array("tests/day07_testdata.txt")
        mydict=build_dict(testinput)
        assert mydict['dotted black'] == {}
        assert mydict['light red']['bright white'] == 1

    def test_path_finder(self):
        testinput=file_to_str_array("tests/day07_testdata.txt")
        mydict=build_dict(testinput)
        our_bag={'shiny gold': 1}
        result=bags_that_can_contain_our_bag(our_bag,mydict)
        assert 'muted yellow' in result
        assert 'bright white' in result
        assert 'light red' in result
        assert 'dark orange' in result

    def test_bags_in_our_bag(self):
        testinput=file_to_str_array("tests/day07_testdata.txt")
        mydict=build_dict(testinput)
        our_bag={'shiny gold': 1}
        result=bags_in_our_bag(our_bag,mydict)
        assert result == 32

    def test_bags_in_our_bag2(self):
        testinput=file_to_str_array("tests/day07_testdata2.txt")
        mydict=build_dict(testinput)
        our_bag={'shiny gold': 1}
        result=bags_in_our_bag(our_bag,mydict)
        assert result == 126

    def test_bags_could_contain_our_bag_queue(self):
        testinput=file_to_str_array("tests/day07_testdata.txt")
        mydict=build_dict(testinput)
        our_bag={'shiny gold': 1}
        result=bags_could_contain_our_bag_queue(our_bag,mydict)
        assert 'muted yellow' in result
        assert 'bright white' in result
        assert 'light red' in result
        assert 'dark orange' in result


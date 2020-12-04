from day04 import IdentityList
from lib.filehelper import file_to_str_array

class TestDay04:
    def test_init_and_print(self):
        expected="0\nbyr:1971\n\n"
        testinput=["byr:1971"]
        myidlist = IdentityList(testinput)
        result=str(myidlist)
        print(result)
        assert expected == result

    def test_multiple_init_and_print(self):
        testinput=["byr:1971","eyr:2039","hgt:172in pid:170cm hcl:17106b iyr:2012 ecl:gry","cid:339","","hgt:161cm eyr:2027","ecl:grn iyr:2011 hcl:#a97842 byr:1977 pid:910468396"]
        expected="0\nbyr:1971\neyr:2039\nhgt:172in\npid:170cm\nhcl:17106b\niyr:2012\necl:gry\ncid:339\n\n1\nhgt:161cm\neyr:2027\necl:grn\niyr:2011\nhcl:#a97842\nbyr:1977\npid:910468396\n\n"
        testidlist=IdentityList(testinput)
        result=str(testidlist)
        print(result)
        assert expected == result
        assert 2 == testidlist.numids()

    def test_valid_byr_passports(self):
        testinput=["byr:1971","eyr:2039","hgt:172in pid:170cm hcl:17106b iyr:2012 ecl:gry","cid:339","","hgt:161cm eyr:2027","ecl:grn iyr:2011 hcl:#a97842 byr:1977 pid:910468396"]
        testidlist=IdentityList(testinput)
        expected=2
        result=testidlist.count_valid(["byr"])
        assert expected == result

    def test_valid_cid_passports(self):
        testinput=["byr:1971","eyr:2039","hgt:172in pid:170cm hcl:17106b iyr:2012 ecl:gry","cid:339","","hgt:161cm eyr:2027","ecl:grn iyr:2011 hcl:#a97842 byr:1977 pid:910468396"]
        testidlist=IdentityList(testinput)
        expected=1
        print(testidlist)
        result=testidlist.count_valid(["cid"])
        assert expected == result

    def test_exampledata(self):
        testinput=file_to_str_array("tests/day04_testdata.txt")
        expected=2
        req_keys=["byr","eyr","hgt","pid","hcl","iyr","ecl"]
        testidlist=IdentityList(testinput)
        print(testidlist)
        result= testidlist.count_valid(req_keys)
        assert result == expected

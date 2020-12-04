from day04 import Passport
from lib.filehelper import file_to_str_array

class TestDay04:
    def test_init_passport(self):
        expected=1971
        testinput={"byr":1971}
        testpassport = Passport(testinput)
        result=testpassport.byr()
        assert expected == result

    def test_init_valid_big_passport(self):
        testinput={"hgt":"159cm","pid":"312887994","cid":"205","iyr":"2016","ecl":"hzl","hcl":"#866857","eyr":"2029","byr":"1944"}
        testpassport = Passport(testinput)
        assert testpassport.byr() == "1944"
        assert testpassport.byr(checkIsValid=True) == True
        assert testpassport.eyr() == "2029"
        assert testpassport.eyr(checkIsValid=True) == True
        assert testpassport.iyr() == "2016"
        assert testpassport.iyr(checkIsValid=True) == True
        assert testpassport.hgt() == "159cm"
        assert testpassport.hgt(checkIsValid=True) == True
        assert testpassport.pid() == "312887994"
        assert testpassport.pid(checkIsValid=True) == True
        assert testpassport.cid() == "205"
        assert testpassport.cid(checkIsValid=True) == True
        assert testpassport.ecl() == "hzl"
        assert testpassport.ecl(checkIsValid=True) == True
        assert testpassport.hcl() == "#866857"
        assert testpassport.hcl(checkIsValid=True) == True
        assert testpassport.isValid() == True

    def test_init_invalid_toobig_passport(self):
        testinput={"hgt":"200cm","pid":"3012887994","cid":"299205","iyr":"2023","ecl":"red","hcl":"#86685g","eyr":"2035","byr":"2018"}
        testpassport = Passport(testinput)
        assert testpassport.byr(checkIsValid=True) == False
        assert testpassport.eyr(checkIsValid=True) == False
        assert testpassport.iyr(checkIsValid=True) == False
        assert testpassport.hgt(checkIsValid=True) == False
        assert testpassport.pid(checkIsValid=True) == False
        assert testpassport.ecl(checkIsValid=True) == False
        assert testpassport.hcl(checkIsValid=True) == False
        assert testpassport.isValid() == False

    def test_init_invalid_toosmall_passport(self):
        testinput={"hgt":"001cm","pid":"32887994","cid":"299205","iyr":"2000","ecl":"red","hcl":"#86685","eyr":"2018","byr":"1850"}
        testpassport = Passport(testinput)
        assert testpassport.byr(checkIsValid=True) == False
        assert testpassport.eyr(checkIsValid=True) == False
        assert testpassport.iyr(checkIsValid=True) == False
        assert testpassport.hgt(checkIsValid=True) == False
        assert testpassport.pid(checkIsValid=True) == False
        assert testpassport.ecl(checkIsValid=True) == False
        assert testpassport.hcl(checkIsValid=True) == False
        assert testpassport.isValid() == False

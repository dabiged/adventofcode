"""
AOC day 04 2020
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Passport:
    """A passport containing fields.
    You can return each field by calling the field method, or by passing the option "checkIsValid=True" 
    you can check if the formatting on that field is correct."""

    def __init__(self, inputdict):
        """Initialise the Passport by reading a python dict: note keys and values are str"""
        self.fields=inputdict
        required_keys=["byr","eyr","hgt","pid","hcl","iyr","ecl"]
        optional_keys=['cid']

    def byr(self,checkIsValid=False):
        """Holder's Birth year four digits; at least 1920 and at most 2002"""
        if checkIsValid:
            return True if 1920 <= int(self.byr()) <= 2002 and len(self.byr()) == 4 else False
        return self.fields['byr'] if 'byr' in self.fields.keys() else None

    def iyr(self,checkIsValid=False):
        """Passport Issue Year four digits; at least 2010 and at most 2020."""
        if checkIsValid:
            return True if 2010 <= int(self.iyr()) <= 2020 and len(self.iyr()) == 4 else False
        return self.fields['iyr'] if 'iyr' in self.fields.keys() else None

    def eyr(self,checkIsValid=False):
        """Passport Expiration year four digits; at least 2020 and at most 2030."""
        if checkIsValid:
            return True if 2020 <= int(self.eyr()) <= 2030 and len(self.eyr()) == 4 else False
        return self.fields['eyr'] if 'eyr' in self.fields.keys() else None

    def hgt(self,checkIsValid=False):
        """Holder's height (note inches or cm)
        a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76."""
        if checkIsValid:
            if "cm" in self.hgt():
                return True if 150 <= int(self.hgt().rstrip("cm")) <= 193 else False
            elif "in" in self.hgt():
                return True if 59 <= int(self.hgt().rstrip("in")) <= 76 else False
            return False
        return self.fields['hgt'] if 'hgt' in self.fields.keys() else None

    def hcl(self,checkIsValid=False):
        """Holder's hair colour  a # followed by exactly six characters 0-9 or a-f."""
        if checkIsValid:
            if len(self.hcl()) != 7:
                return False
            if self.hcl()[0] != "#":
                return False
            for char in self.hcl()[1:7]:
                if str(char) not in list("0123456789abcdef"):
                    return False
            return True
        return self.fields['hcl'] if 'hcl' in self.fields.keys() else None

    def ecl(self,checkIsValid=False):
        """Eye colour - exactly one of: amb blu brn gry grn hzl oth."""
        if checkIsValid:
            return True if self.ecl() in "amb blu brn gry grn hzl oth".split() else False
        return self.fields['ecl'] if 'ecl' in self.fields.keys() else None

    def pid(self,checkIsValid=False):
        """Passport ID - pid (Passport ID) - a nine-digit number, including leading zeroes."""
        if checkIsValid:
            try:
                # Occasionally pid contains heights or hcls with non-numeric characters.
                return True if self.pid() == str(int(self.pid())).zfill(9) and  len(self.pid()) == 9 else False
            except:
                return False
        return self.fields['pid'] if 'pid' in self.fields.keys() else None

    def cid(self,checkIsValid=False):
        """Country ID - cid (Country ID) - ignored, missing or not."""
        if checkIsValid:
            return True
        return self.fields['cid'] if 'cid' in self.fields.keys() else None

    def isValid(self):
        """Check if all mandatory fields are populated for this passport"""
            if None in [self.byr(), self.eyr(), self.iyr(), self.hgt(), self.ecl(), self.hcl(), self.pid()]:
                return False
            return True

    def isValidStrict(self):
        """Check that all manadatory fields are populated, and all of those fields have valid values"""
        if None in [self.byr(), self.eyr(), self.iyr(), self.hgt(), self.ecl(), self.hcl(), self.pid()]:
            return False
        return self.byr(checkIsValid=True) and self.eyr(checkIsValid=True) and \
        self.iyr(checkIsValid=True) and self.hgt(checkIsValid=True) and \
        self.ecl(checkIsValid=True) and self.hcl(checkIsValid=True) and \
        self.pid(checkIsValid=True)

def day04_01():
    """Run part 1 of Day 04's code"""
    path = "./input/04/input_formatted.txt"
    ValidPassports=0
    for passport_details in file_to_str_array(path):
        if Passport(eval(passport_details)).isValid():
            ValidPassports+=1
    print(f'0401: Number of valid passports: {ValidPassports}')

def day04_02():
    """Run part 2 of Day 04's code"""
    path = "./input/04/input_formatted.txt"
    ValidPassports=0
    for passport_details in file_to_str_array(path):
        if Passport(eval(passport_details)).isValidStrict():
            ValidPassports+=1
    print(f'0402: Number of valid passports: {ValidPassports}')

if __name__ == "__main__":
    day04_01()
    day04_02()

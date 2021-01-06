"""
AOC day 04 2020
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Passport:
    """A passport containing fields.
    You can return each field by calling the field method, or by passing the
    option "checkisvalid=True" you can check if the formatting on that field
    is correct."""

    def __init__(self, inputdict):
        """Initialise the Passport by reading a python dict: note keys and values are str"""
        self.fields=inputdict

    def byr(self,checkisvalid=False):
        """Holder's Birth year four digits; at least 1920 and at most 2002"""
        if checkisvalid:
            return bool(1920 <= int(self.byr()) <= 2002 and len(self.byr()) == 4 )
        return self.fields['byr'] if 'byr' in self.fields.keys() else None

    def iyr(self,checkisvalid=False):
        """Passport Issue Year four digits; at least 2010 and at most 2020."""
        if checkisvalid:
            return bool(2010 <= int(self.iyr()) <= 2020 and len(self.iyr()) == 4)
        return self.fields['iyr'] if 'iyr' in self.fields.keys() else None

    def eyr(self,checkisvalid=False):
        """Passport Expiration year four digits; at least 2020 and at most 2030."""
        if checkisvalid:
            return bool(2020 <= int(self.eyr()) <= 2030 and len(self.eyr()) == 4)
        return self.fields['eyr'] if 'eyr' in self.fields.keys() else None

    def hgt(self,checkisvalid=False):
        """Holder's height (note inches or cm)
        a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76."""
        if checkisvalid:
            if "cm" in self.hgt():
                return bool(150 <= int(self.hgt().rstrip("cm")) <= 193)
            if "in" in self.hgt():
                return bool(59 <= int(self.hgt().rstrip("in")) <= 76 )
            return False
        return self.fields['hgt'] if 'hgt' in self.fields.keys() else None

    def hcl(self,checkisvalid=False):
        """Holder's hair colour  a # followed by exactly six characters 0-9 or a-f."""
        if checkisvalid:
            if len(self.hcl()) != 7:
                return False
            if self.hcl()[0] != "#":
                return False
            for char in self.hcl()[1:7]:
                if str(char) not in list("0123456789abcdef"):
                    return False
            return True
        return self.fields['hcl'] if 'hcl' in self.fields.keys() else None

    def ecl(self,checkisvalid=False):
        """Eye colour - exactly one of: amb blu brn gry grn hzl oth."""
        if checkisvalid:
            return bool(self.ecl() in "amb blu brn gry grn hzl oth".split())
        return self.fields['ecl'] if 'ecl' in self.fields.keys() else None

    def pid(self,checkisvalid=False):
        """Passport ID - pid (Passport ID) - a nine-digit number, including leading zeroes."""
        if checkisvalid:
            try:
                # Occasionally pid contains heights or hcls with non-numeric
                # characters.
                return bool(self.pid() == str(int(self.pid())).zfill(9) and  \
                len(self.pid()) == 9 )
            except ValueError:
                return False
        return self.fields['pid'] if 'pid' in self.fields.keys() else None

    def cid(self,checkisvalid=False):
        """Country ID - cid (Country ID) - ignored, missing or not."""
        if checkisvalid:
            return True
        return self.fields['cid'] if 'cid' in self.fields.keys() else None

    def is_valid(self):
        """Check if all mandatory fields are populated for this passport"""
        if None in [self.byr(), self.eyr(), self.iyr(), self.hgt(), self.ecl(), \
        self.hcl(), self.pid()]:
            return False
        return True

    def is_valid_strict(self):
        """Check that all manadatory fields are populated, and all of those
        fields have valid values"""
        if None in [self.byr(), self.eyr(), self.iyr(), self.hgt(), self.ecl(), \
        self.hcl(), self.pid()]:
            return False
        return self.byr(checkisvalid=True) and self.eyr(checkisvalid=True) and \
        self.iyr(checkisvalid=True) and self.hgt(checkisvalid=True) and \
        self.ecl(checkisvalid=True) and self.hcl(checkisvalid=True) and \
        self.pid(checkisvalid=True)

def day04_01():
    #pylint: disable=eval-used
    """Run part 1 of Day 04's code"""
    path = "./input/04/input_formatted.txt"
    validpassports=0
    for passport_details in file_to_str_array(path):
        if Passport(eval(passport_details)).is_valid():
            validpassports+=1
    print(f'0401: Number of valid passports: {validpassports}')

def day04_02():
    #pylint: disable=eval-used
    """Run part 2 of Day 04's code"""
    path = "./input/04/input_formatted.txt"
    validpassports=0
    for passport_details in file_to_str_array(path):
        if Passport(eval(passport_details)).is_valid_strict():
            validpassports+=1
    print(f'0402: Number of strictly valid passports: {validpassports}')

if __name__ == "__main__":
    day04_01()
    day04_02()

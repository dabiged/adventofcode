"""
AOC day 04 2020
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

class Passport:
    """A passport containing fields."""

    def __init__(self, inputdict):
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
                return True if self.pid() == str(int(self.pid())).zfill(9) and  len(self.pid()) == 9 else False
            except:
                return False
        return self.fields['pid'] if 'pid' in self.fields.keys() else None

    def cid(self,checkIsValid=False):
        """Country ID - cid (Country ID) - ignored, missing or not."""
        if checkIsValid:
            return True
        return self.fields['cid'] if 'cid' in self.fields.keys() else None

    def isValid(self, part1=True, part2=False):
        if part1:
            if None in [self.byr(), self.eyr(), self.iyr(), self.hgt(), self.ecl(), self.hcl(), self.pid()]:
                return False
            return True
        if part2:

            if None in [self.byr(), self.eyr(), self.iyr(), self.hgt(), self.ecl(), self.hcl(), self.pid()]:
                return False
            return self.byr(checkIsValid=True) and self.eyr(checkIsValid=True) and \
            self.iyr(checkIsValid=True) and self.hgt(checkIsValid=True) and \
            self.ecl(checkIsValid=True) and self.hcl(checkIsValid=True) and \
            self.pid(checkIsValid=True)

class IdentityList:
    """
    A list of identity values
    """

    def __init__(self, listofrun):
        """
        Initialises the Identity List by reading rows from a file.
        """
        self.identities={}
        identity_number=0
        for row in listofrun:
            if row == "":
                identity_number+=1
            if identity_number not in self.identities.keys():
                self.identities[identity_number]={}
            for id_entry in row.split():
                idkey, idvalue = id_entry.split(":")
                self.identities[identity_number][idkey]=idvalue

    def __repr__(self):
        """
        """
        output=""
        for identity, idinfo in self.identities.items():
            output+=str(identity)+"\n"
            for idkey, idval in idinfo.items():
                output+=str(idkey)+":"+str(idval)+"\n"
            output+="\n"
        return output

    def numids(self):
        """The Number of columns in the grid"""
        return len(self.identities.keys())

    def count_valid(self,reqkeys):
        """
        Count the number of ids containing all keys in reqkeys
        """
        count_valid_passports=0
        for identity, idinfo in self.identities.items():
            if set(reqkeys).issubset( set(idinfo.keys())):
                count_valid_passports+=1
        return count_valid_passports

##      def count_more_valid(self,reqkeys):
##          """
##          Count the number of ids containing all keys in reqkeys
##          """
##          count_invalid_passports=0
##          for identity, idinfo in self.identities.items():
##              ValidPassport=True
##              if not 1920 <= int(idinfo['byr']) <= 2002:
##                  # Birth Year) - four digits; at least 1920 and at most 2002.
##                  ValidPassport = False
##              if not 2010 <= int(idinfo['iyr']) <= 2020:
##                  #(Issue Year) - four digits; at least 2010 and at most 2020.
##                  ValidPassport = False
##              if not 2020 <= idinfo['eyr'] <= 2030:
##                  # (Expiration Year) - four digits; at least 2020 and at most 2030.
##                  ValidPassport = False
##              if "cm" in idinfo['hgt'] and not 150 <= int(idinfo['hgt'][0:2]) <= 193:
##                  # (Height) - a number followed by either cm or in: 
##                  # If cm, the number must be at least 150 and at most 193.
##                  ValidPassport = False
##              if "in" in idinfo['hgt'] and not 59 <= int(idinfo['hgt'][0:1]) <= 76:
##                  # (Height) - a number followed by either cm or in: 
##                  # If in, the number must be at least 59 and at most 76.
##                  ValidPassport = False
##              if idinfo['hcl']
##                  # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
##              if idinfo['ecl'] not in ["amb","blu","brn","gry","grn","hzl","oth"]
##                  # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
##                  ValidPassport = False
##              if idinfo['pid']
##                  # (Passport ID) - a nine-digit number, including leading zeroes.
##                  ValidPassport = False
##              if not set(reqkeys).issubset( set(idinfo.keys())):
##                  ValidPassport=False
##  
##              if ValidPassport:
##                  count_valid_passports += 1
##  
##          return count_valid_passports


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
        if Passport(eval(passport_details)).isValid(part2=True, part1=False):
            ValidPassports+=1
    print(f'0402: Number of valid passports: {ValidPassports}')

if __name__ == "__main__":
    day04_01()
    day04_02()

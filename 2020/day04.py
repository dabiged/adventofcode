"""
AOC day 04 2020
"""

from lib.filehelper import file_to_str_array
# pylint: disable=missing-module-docstring

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



def day04_01():
    """Run part 1 of Day 04's code"""

    path = "./input/04/input.txt"
    myidlist=IdentityList(file_to_str_array(path))
    req_keys=["byr","eyr","hgt","pid","hcl","iyr","ecl"]
    result=myidlist.count_valid(req_keys)
    print(f'0401: Number of valid passports: {result}')
    pass

def day04_02():
    """Run part 2 of Day 04's code"""
    path = "./input/04/input.txt"
    #print(f'0402: Number of Trees Intercepted on 5 runs:{result}')
    pass

if __name__ == "__main__":
    day04_01()
    #day04_02()

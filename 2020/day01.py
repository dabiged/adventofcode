"""
Advent of Code Day 01 2020
"""

from lib.filehelper import file_to_array
# pylint: disable=missing-module-docstring

def product_of_sumto2020(expenses: list) -> int:
    """
    Find two expenses in a list of expenses and return the product of the
    two expenses whose sum is 2020.
    """
    for expense1 in expenses:
        for expense2 in expenses:
            if expense1+ expense2 == 2020:
                return expense1*expense2
    return None

def product_of_3_sumto2020(expenses: list) -> int:
    """
    Find three expenses in a list of expenses and return the product of the
    three expenses whose sum is 2020.
    """
    for expense1 in expenses:
        for expense2 in expenses:
            for expense3 in expenses:
                if expense1+ expense2 +expense3 == 2020:
                    return expense1*expense2*expense3
    return None


def day01_01():
    """Run part 1 of Day 1's code"""
    path = "./input/01/input.txt"
    product = product_of_sumto2020(file_to_array(path))
    print(f"0101: product of two numbers summing to 2020: {product}")


def day01_02():
    """Run part 2 of Day 1's code"""
    path = "./input/01/input.txt"
    product = product_of_3_sumto2020(file_to_array(path))
    print(f"0102: product of three numbers summing to 2020: {product}")


if __name__ == "__main__":
    day01_01()
    day01_02()

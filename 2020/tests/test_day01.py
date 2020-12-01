from day01 import product_of_sumto2020, product_of_3_sumto2020


class TestDay01:
    def test_product_of_sumto2020(self):
        expected = 514579
        inputtotest = [1721, 979, 366, 299, 675, 1456]
        result = product_of_sumto2020(inputtotest)
        assert expected == result

    def test_product_of_3_sumto2020(self):
        expected = 241861950
        inputtotest = [1721, 979, 366, 299, 675, 1456]
        result = product_of_3_sumto2020(inputtotest)
        assert expected == result

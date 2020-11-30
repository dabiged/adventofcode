from day02 import checksum_one_label, checksum_multiple_labels, find_similar_boxids


class TestDay02:
    def test_example1(self):
        expected = {}
        inputvalue = "abcdef"
        result = checksum_one_label(inputvalue)
        assert expected == result

    def test_example2(self):
        expected = {2: 1, 3: 1}
        inputvalue = "bababc"
        result = checksum_one_label(inputvalue)
        assert expected == result

    def test_example3(self):
        expected = {2: 1}
        inputvalue = "abbcde"
        result = checksum_one_label(inputvalue)
        assert expected == result

    def test_example4(self):
        expected = {3: 1}
        inputvalue = "abcccd"
        result = checksum_one_label(inputvalue)
        assert expected == result

    def test_example5(self):
        expected = {2: 1}
        inputvalue = "aabcdd"
        result = checksum_one_label(inputvalue)
        assert expected == result

    def test_example6(self):
        expected = {2: 1}
        inputvalue = "abcdee"
        result = checksum_one_label(inputvalue)
        assert expected == result

    def test_example7(self):
        expected = {3: 1}
        inputvalue = "ababab"
        result = checksum_one_label(inputvalue)
        assert expected == result

    def test_multiplechecksums(self):
        expected = 12
        inputvalue = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        result = checksum_multiple_labels(inputvalue)
        assert expected == result

    def test_find_similar_boxids(self):
        expected = "fgij"
        inputvalue = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
        result = find_similar_boxids(inputvalue)
        assert expected == result

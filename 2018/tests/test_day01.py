from day01 import calibrate_device, calibrate_freq_twice_device


class TestDay01:
    def test_frequency_positive1(self):
        expected = 1
        frequencylist = ["+1"]
        result = calibrate_device(frequencylist)
        assert expected == result

    def test_frequency_negative1(self):
        expected = -1
        frequencylist = ["-1"]
        result = calibrate_device(frequencylist)
        assert expected == result

    def test_frequency_example1(self):
        expected = 3
        frequencylist = ["+1", "+1", "+1"]
        result = calibrate_device(frequencylist)
        assert expected == result

    def test_frequency_example2(self):
        expected = 0
        frequencylist = ["+1", "+1", "-2"]
        result = calibrate_device(frequencylist)
        assert expected == result

    def test_frequency_example3(self):
        expected = -6
        frequencylist = ["-1", "-2", "-3"]
        result = calibrate_device(frequencylist)
        assert expected == result

    def test_first_double_frequency_example1(self):
        expected = 0
        frequencylist = ["+1", "-1"]
        result = calibrate_freq_twice_device(frequencylist)
        assert expected == result

    def test_first_double_frequency_example2(self):
        expected = 10
        frequencylist = ["+3", "+3", "+4", "-2", "-4"]
        result = calibrate_freq_twice_device(frequencylist)
        assert expected == result

    def test_first_double_frequency_example3(self):
        expected = 5
        frequencylist = ["-6", "+3", "+8", "+5", "-6"]
        result = calibrate_freq_twice_device(frequencylist)
        assert expected == result

    def test_first_double_frequency_example4(self):
        expected = 14
        frequencylist = ["+7", "+7", "-2", "-7", "-4"]
        result = calibrate_freq_twice_device(frequencylist)

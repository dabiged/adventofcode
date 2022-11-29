from day01 import calc_captcha, calc_recaptcha, calc_match


class TestDay01:
    def test_catcha1(self):
        expected = 3
        digit_seq = "1122"
        result = calc_captcha(digit_seq)
        assert expected == result

    def test_catcha2(self):
        expected = 4
        digit_seq = "1111"
        result = calc_captcha(digit_seq)
        assert expected == result

    def test_catcha3(self):
        expected = 0
        digit_seq = "1234"
        result = calc_captcha(digit_seq)
        assert expected == result

    def test_catcha4(self):
        expected = 9
        digit_seq = "91212129"
        result = calc_captcha(digit_seq)
        assert expected == result

    def test_calc_match(self):
        assert 3 == calc_match(0,'123123')
        assert 4 == calc_match(1,'123123')
        assert 5 == calc_match(2,'123123')
        assert 0 == calc_match(3,'123123')
        assert 1 == calc_match(4,'123123')
        assert 2 == calc_match(5,'123123')
        assert 4 == calc_match(0,'12341234')
        assert 5 == calc_match(1,'12341234')
        assert 6 == calc_match(2,'12341234')
        assert 7 == calc_match(3,'12341234')
        assert 0 == calc_match(4,'12341234')
        assert 1 == calc_match(5,'12341234')
        assert 2 == calc_match(6,'12341234')
        assert 3 == calc_match(7,'12341234')


    def test_recatcha1(self):
        expected = 6
        digit_seq = "1212"
        result = calc_recaptcha(digit_seq)
        assert expected == result

    def test_recatcha2(self):
        expected = 0
        digit_seq = "1221"
        result = calc_recaptcha(digit_seq)
        assert expected == result

    def test_recatcha3(self):
        expected = 4
        digit_seq = "123425"
        result = calc_recaptcha(digit_seq)
        assert expected == result

    def test_recatcha4(self):
        expected = 12
        digit_seq = "123123"
        result = calc_recaptcha(digit_seq)
        assert expected == result

    def test_recatcha5(self):
        expected = 4
        digit_seq = "12131415"
        result = calc_recaptcha(digit_seq)
        assert expected == result


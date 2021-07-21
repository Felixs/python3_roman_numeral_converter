import unittest
import src.roman_numeral_converter as rnc


class Test_roman_numeral_converter_creation(unittest.TestCase):

    def test_roman_numeral_converter_creation(self):
        test_creation = rnc.Roman_numeral_converter()


class Test_roman_numeral_converter_from_int(unittest.TestCase):

    def setUp(self):
        self.rnc = rnc.Roman_numeral_converter()

    def test_negative_input(self):
        self.assertRaises(ValueError, self.rnc.convert_int, -1)

    def test_zero_input(self):
        self.assertRaises(ValueError, self.rnc.convert_int, 0)

    def test_max_input(self):
        self.assertRaises(ValueError, self.rnc.convert_int, 4000)

    def test_is_input_integer(self):
        self.assertRaises(TypeError, self.rnc.convert_int, 1.1)
        self.assertRaises(TypeError, self.rnc.convert_int, 'a')
        self.assertRaises(TypeError, self.rnc.convert_int, None)
        self.assertRaises(TypeError, self.rnc.convert_int, [])
        self.assertRaises(TypeError, self.rnc.convert_int, {})

    def test_input_one(self):
        self.assertEqual(self.rnc.convert_int(1), 'I')

    def test_input_two(self):
        self.assertEqual(self.rnc.convert_int(2), 'II')

    def test_input_three(self):
        self.assertEqual(self.rnc.convert_int(3), 'III')

    def test_input_four(self):
        self.assertEqual(self.rnc.convert_int(4), 'IV')

    def test_input_five(self):
        self.assertEqual(self.rnc.convert_int(5), 'V')

    def test_input_six(self):
        self.assertEqual(self.rnc.convert_int(6), 'VI')

    def test_input_nine(self):
        self.assertEqual(self.rnc.convert_int(9), 'IX')

    def test_input_ten(self):
        self.assertEqual(self.rnc.convert_int(10), 'X')

    def test_input_eleven(self):
        self.assertEqual(self.rnc.convert_int(11), 'XI')

    def test_input_fiftynine(self):
        self.assertEqual(self.rnc.convert_int(59), 'LIX')

    def test_input_forthynine(self):
        self.assertEqual(self.rnc.convert_int(49), 'XLIX')

    def test_input_nintynine(self):
        self.assertEqual(self.rnc.convert_int(99), 'XCIX')

    def test_input_50(self):
        self.assertEqual(self.rnc.convert_int(50), 'L')

    def test_input_100(self):
        self.assertEqual(self.rnc.convert_int(100), 'C')

    def test_input_500(self):
        self.assertEqual(self.rnc.convert_int(500), 'D')

    def test_input_1000(self):
        self.assertEqual(self.rnc.convert_int(1000), 'M')

    def test_input_258(self):
        self.assertEqual(self.rnc.convert_int(258), 'CCLVIII')

    def test_input_onethousendninehoundredsixtyfour(self):
        self.assertEqual(self.rnc.convert_int(1964), 'MCMLXIV')

    def test_input_3500(self):
        self.assertEqual(self.rnc.convert_int(3500), 'MMMD')

    def test_input_140(self):
        self.assertEqual(self.rnc.convert_int(140), 'CXL')

    def test_input_1337(self):
        self.assertEqual(self.rnc.convert_int(1337), 'MCCCXXXVII')

    def test_max_input(self):
        self.assertEqual(self.rnc.convert_int(3999), 'MMMCMXCIX')


class Test_roman_numeral_converter_from_roman(unittest.TestCase):

    def setUp(self):
        self.rnc = rnc.Roman_numeral_converter()

    def test_is_input_string(self):
        self.assertRaises(TypeError, self.rnc.convert_roman, 1)
        self.assertRaises(TypeError, self.rnc.convert_roman, 1.1)
        self.assertRaises(TypeError, self.rnc.convert_roman, [])
        self.assertRaises(TypeError, self.rnc.convert_roman, {})
        self.assertRaises(TypeError, self.rnc.convert_roman, None)

    def test_is_input_string_empty(self):
        self.assertRaises(ValueError, self.rnc.convert_roman, '')

    def test_accept_lower_and_upper_case(self):
        self.assertEqual(self.rnc.convert_roman('i'), 1)

    def test_has_input_string_invalid_characters(self):
        self.assertRaises(ValueError, self.rnc.convert_roman, 'XVCASD')

    def test_input_i(self):
        self.assertEqual(self.rnc.convert_roman('I'), 1)

    def test_input_ii(self):
        self.assertEqual(self.rnc.convert_roman('II'), 2)

    def test_input_iv(self):
        self.assertEqual(self.rnc.convert_roman('IV'), 4)

    def test_input_v(self):
        self.assertEqual(self.rnc.convert_roman('V'), 5)

    def test_input_vi(self):
        self.assertEqual(self.rnc.convert_roman('VI'), 6)

    def test_input_vii(self):
        self.assertEqual(self.rnc.convert_roman('VII'), 7)

    def test_input_viii(self):
        self.assertEqual(self.rnc.convert_roman('VIII'), 8)

    def test_input_ix(self):
        self.assertEqual(self.rnc.convert_roman('IX'), 9)

    def test_input_up_to_3999(self):
        for i in range(1, 4000):
            roman = self.rnc.convert_int(i)
            self.assertEqual(self.rnc.convert_roman(roman), i)

    def test_invalid_roman_input(self):
        self.assertRaises(ValueError, self.rnc.convert_roman, 'IIIV')
        self.assertRaises(ValueError, self.rnc.convert_roman, 'IIV')
        self.assertRaises(ValueError, self.rnc.convert_roman, 'VXX')
        self.assertRaises(ValueError, self.rnc.convert_roman, 'VIIII')
        self.assertRaises(ValueError, self.rnc.convert_roman, 'IICIIMXCV')
        self.assertRaises(ValueError, self.rnc.convert_roman, 'DCCCXLVV')
        self.assertRaises(ValueError, self.rnc.convert_roman, 'XXLCMV')

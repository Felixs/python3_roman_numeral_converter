class Roman_numeral_converter:

    INTEGER_VALUES = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }

    ROMAN_VALUES = {y: x for x, y in INTEGER_VALUES.items()}

    SUBSTRACTION_INTEGER_VALUES = {
        1000: 100,
        500: 100,
        100: 10,
        50: 10,
        10: 1,
        5: 1
    }

    def convert_int(self, integer: int) -> str:
        self.check_int_input_parameter(integer)

        if integer in self.INTEGER_VALUES:
            return self.INTEGER_VALUES[integer]

        for integer_value in self.INTEGER_VALUES.keys():

            # suffix path
            if integer > integer_value:
                return self.create_suffix_value(integer, integer_value)

            # prefix path
            elif integer >= integer_value - self.SUBSTRACTION_INTEGER_VALUES[integer_value]:
                return self.create_prefix_value(integer, integer_value)

    def convert_roman(self, string: str) -> int:
        self.check_roman_input_parameter(string)
        string = self.convert_lower_to_uppercase(string)
        integer_list = self.convert_roman_list_to_integer_list(string)

        substraction_total = 0
        for index, integer in enumerate(integer_list):
            if index >= 1:
                substraction_total += self.check_for_substraction_value(
                    integer_list, index, integer)

            if index >= 2:
                self.raise_error_if_last_2_numerals_smaler_then_current(
                    integer, integer_list, index)

            if index >= 3:
                self.raise_error_if_last_4_numerals_are_equal(
                    integer, integer_list, index)

        return sum(integer_list) - substraction_total

    def check_for_substraction_value(self, integer_list, index, integer):
        substraction = 0
        previous_integer = integer_list[index - 1]
        if integer > previous_integer:
            if self.SUBSTRACTION_INTEGER_VALUES[integer] == previous_integer:
                substraction += 2 * integer_list[index - 1]
            else:
                raise ValueError('Wrong order in roman numeral')

        if (integer + previous_integer) in self.INTEGER_VALUES:
            raise ValueError('Wrong order in roman numeral')

        return substraction

    def raise_error_if_last_4_numerals_are_equal(self, integer, integer_list, index):
        if integer == integer_list[index - 1] == integer_list[index - 2] == integer_list[index - 3]:
            raise ValueError('Wrong order in roman numeral')

    def raise_error_if_last_2_numerals_smaler_then_current(self, integer, integer_list, index):
        if integer > integer_list[index - 1] and integer > integer_list[index - 2]:
            raise ValueError('Wrong order in roman numeral')

    def convert_roman_list_to_integer_list(self, string):
        try:
            integer_list = [self.ROMAN_VALUES[char] for char in string]
        except:
            raise ValueError('Wrong character in roman numeral')
        return integer_list

    def convert_lower_to_uppercase(self, string):
        string = string.upper()
        return string

    def check_roman_input_parameter(self, string):
        if type(string) != str:
            raise TypeError(
                f'{type(string)} not supported, expected str')

        if string == '':
            raise ValueError('No empty allowed!')

    def create_prefix_value(self, integer, integer_value):
        try:
            return self.create_substraction_value(integer_value) + self.convert_int(integer -
                                                                                    (integer_value - self.SUBSTRACTION_INTEGER_VALUES[integer_value]))
        except ValueError:
            return self.create_substraction_value(integer_value)

    def create_suffix_value(self, integer, integer_value):
        return self.INTEGER_VALUES[integer_value] + self.convert_int(integer - integer_value)

    def create_substraction_value(self, integer_value):
        return self.INTEGER_VALUES[self.SUBSTRACTION_INTEGER_VALUES[integer_value]] + self.INTEGER_VALUES[integer_value]

    def check_int_input_parameter(self, integer_value):
        if type(integer_value) != int:
            raise TypeError(
                f'{type(integer_value)} not supported, expected int')

        if integer_value <= 0:
            raise ValueError('No negative or zero value allowed!')

        if integer_value >= 4000:
            raise ValueError(f'{integer_value} exceeds maximum number of 3999')

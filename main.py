# Examples to test the converter

from src import roman_numeral_converter as rnc
import random
converter = rnc.Roman_numeral_converter()


def find_longest_roman_numeral():
    longest = ''
    for i in range(1, 4000):
        numeral = converter.convert_int(i)
        if len(numeral) > len(longest):
            longest = numeral

    return longest


ROMAN_CHARS = 'IVXLCDM'
ROMAN_MAX_LENGTH = 15


def generate_random_roman_numeral():
    output = ''
    for _ in range(1, random.randint(2, 15)):
        output += ROMAN_CHARS[random.randint(0, 6)]

    return output


if __name__ == '__main__':
    all_roman_numerals = [converter.convert_int(x) for x in range(1, 4000)]
    hit_counter = 0
    for z in range(10_000_000):
        roman = generate_random_roman_numeral()
        raised_exception = False
        try:
            integer = converter.convert_roman(roman)
        except:
            raised_exception = True
        finally:
            if raised_exception:
                if roman in all_roman_numerals:
                    print(
                        f'Found an error: {roman} exists but raised an exception!')
            else:
                hit_counter += 1

        if z % 100000 == 0:
            print(z)

    print(f'Hit a total of {hit_counter} roman numerals by random')

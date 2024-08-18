"""https://www.codewars.com/kata/54b724efac3d5402db00065e"""

from solution_decode_the_morse_code import *


def test_fixed_tests__should_obtain_correct_decoding_of_morse_code_from_the_description():
    assert decode_morse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE'


def test_fixed_tests__should_obtain_correct_decoding_of_morse_code_for_basic_examples():
    assert decode_morse('.-') == 'A'
    assert decode_morse('--...') == '7'
    assert decode_morse('...-..-') == '$'
    assert decode_morse('.') == 'E'
    assert decode_morse('..') == 'I'
    assert decode_morse('. .') == 'EE'
    assert decode_morse('.   .') == 'E E'
    assert decode_morse('...-..- ...-..- ...-..-') == '$$$'
    assert decode_morse('----- .---- ..--- ---.. ----.') == '01289'
    assert decode_morse('.-... ---...   -..-. --...') == '&: /7'
    assert decode_morse('...---...') == 'SOS'
    assert decode_morse('... --- ...') == 'SOS'
    assert decode_morse('...   ---   ...') == 'S O S'


def test_fixed_tests__should_obtain_correct_decoding_of_morse_code_for_examples_with_extra_spaces():
    assert decode_morse(' . ') == 'E'
    assert decode_morse('   .   . ') == 'E E'


def test_fixed_tests__should_obtain_correct_decoding_of_morse_code_for_a_complex_example_and_should_ignore_leading_and_trailing_whitespace():
    assert decode_morse(
        '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  ') == 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'

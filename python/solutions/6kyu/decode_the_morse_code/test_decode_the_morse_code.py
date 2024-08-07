"""https://www.codewars.com/kata/54b724efac3d5402db00065e"""

import unittest

from solution_decode_the_morse_code import decode_morse


class FixedTests(unittest.TestCase):
    def test_should_obtain_correct_decoding_of_morse_code_from_the_description(self):
        self.assertEqual(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

    def test_should_obtain_correct_decoding_of_morse_code_for_basic_examples(self):
        self.assertEqual(decode_morse('.-'), 'A')
        self.assertEqual(decode_morse('--...'), '7')
        self.assertEqual(decode_morse('...-..-'), '$')
        self.assertEqual(decode_morse('.'), 'E')
        self.assertEqual(decode_morse('..'), 'I')
        self.assertEqual(decode_morse('. .'), 'EE')
        self.assertEqual(decode_morse('.   .'), 'E E')
        self.assertEqual(decode_morse('...-..- ...-..- ...-..-'), '$$$')
        self.assertEqual(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
        self.assertEqual(decode_morse('.-... ---...   -..-. --...'), '&: /7')
        self.assertEqual(decode_morse('...---...'), 'SOS')
        self.assertEqual(decode_morse('... --- ...'), 'SOS')
        self.assertEqual(decode_morse('...   ---   ...'), 'S O S')

    def test_should_obtain_correct_decoding_of_morse_code_for_examples_with_extra_spaces(self):
        self.assertEqual(decode_morse(' . '), 'E')
        self.assertEqual(decode_morse('   .   . '), 'E E')

    def test_morse_complex_example(self):
        self.assertEqual(decode_morse(
            '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
                         'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

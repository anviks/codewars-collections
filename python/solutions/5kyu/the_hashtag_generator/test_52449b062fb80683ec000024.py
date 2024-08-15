"""https://www.codewars.com/kata/52449b062fb80683ec000024"""

import unittest

from solution_52449b062fb80683ec000024 import generate_hashtag


class FixedTests(unittest.TestCase):
    def test_should_generate_the_correct_hashtag_in_fixed_tests(self):
        self.assertEqual(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
        self.assertEqual(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
        self.assertEqual(generate_hashtag('      Codewars'), '#Codewars', 'Should handle leading whitespace.')
        self.assertEqual(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
        self.assertEqual(generate_hashtag('codewars is nice'), '#CodewarsIsNice',
                         'Should capitalize first letters of words.')
        self.assertEqual(generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice',
                         'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.')
        self.assertEqual(generate_hashtag('c i n'), '#CIN',
                         'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.')
        self.assertEqual(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice',
                         'Should deal with unnecessary middle spaces.')

    def test_should_return_false_if_the_input_is_empty_or_result_is_longer_than_140_chars(self):
        self.assertEqual(generate_hashtag(''), False, 'Expected an empty string to return False')
        self.assertEqual(generate_hashtag(
            'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'),
                         False, 'Should return False if the final string is longer than 140 chars.')

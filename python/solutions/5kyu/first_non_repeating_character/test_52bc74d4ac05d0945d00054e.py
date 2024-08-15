"""https://www.codewars.com/kata/52bc74d4ac05d0945d00054e"""

import unittest

from solution import first_non_repeating_letter


class SampleTests(unittest.TestCase):
    def test_should_handle_simple_cases(self):
        self.assertEqual(first_non_repeating_letter('a'), 'a')
        self.assertEqual(first_non_repeating_letter('stress'), 't')
        self.assertEqual(first_non_repeating_letter('moonmen'), 'e')

    def test_should_handle_empty_strings(self):
        self.assertEqual(first_non_repeating_letter(''), '')

    def test_should_handle_strings_without_unique_characters(self):
        self.assertEqual(first_non_repeating_letter('abba'), '')
        self.assertEqual(first_non_repeating_letter('aa'), '')

    def test_should_handle_exotic_characters(self):
        self.assertEqual(first_non_repeating_letter('~><#~><'), '#')
        self.assertEqual(first_non_repeating_letter('hello world, eh?'), 'w')

    def test_should_handle_letter_case_correctly(self):
        self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')
        self.assertEqual(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')

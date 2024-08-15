"""https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c"""

import unittest

from solution_54521e9ec8e60bc4de000d6c import max_sequence


class FixedTests(unittest.TestCase):
    def test_should_work_on_an_empty_array(self):
        self.assertEqual(max_sequence([]), 0)

    def test_should_obtain_correct_maximum_subarray_sum_in_the_array_from_the_kata_description_example(self):
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_should_obtain_correct_maximum_subarray_sum_in_an_example_with_negative_numbers(self):
        self.assertEqual(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)

    def test_should_obtain_correct_maximum_subarray_sum_in_a_complex_example(self):
        self.assertEqual(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)

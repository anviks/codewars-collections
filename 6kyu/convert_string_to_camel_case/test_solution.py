"""https://www.codewars.com/kata/517abf86da9663f1d2000003"""

import unittest

from solution import to_camel_case


class SampleTests(unittest.TestCase):
    def test_tests(self):
        self.assertEqual(to_camel_case(""), "", "An empty string was provided but not returned")
        self.assertEqual(to_camel_case("the_stealth_warrior"), "theStealthWarrior",
                         "to_camel_case('the_stealth_warrior') did not return correct value")
        self.assertEqual(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior",
                         "to_camel_case('The-Stealth-Warrior') did not return correct value")
        self.assertEqual(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")

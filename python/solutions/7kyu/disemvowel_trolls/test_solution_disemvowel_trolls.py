"""https://www.codewars.com/kata/52fba66badcd10859f00097e"""

import unittest

from solution_disemvowel_trolls import disemvowel


class FixedTests(unittest.TestCase):
    def test_first_fixed_test(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!",
                         'Incorrect answer for input="This website is for losers LOL!"\n')

    def test_second_fixed_test(self):
        self.assertEqual(disemvowel("No offense but,\nYour writing is among the worst I've ever read"),
                         "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd",
                         'Incorrect answer for input="No offense but,\nYour writing is among the worst I\'ve ever read"\n')

    def test_third_fixed_test(self):
        self.assertEqual(disemvowel("What are you, a communist?"), "Wht r y,  cmmnst?",
                         'Incorrect answer for input="What are you, a communist?"\n')

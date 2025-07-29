"""https://www.codewars.com/kata/55905b7597175ffc1a00005a"""

import pytest

from solution_paginating_a_huge_book import *

def test_sample_tests__tests():
    assert page_digits(4) == 4
    assert page_digits(12) == 15
    assert page_digits(100) == 192

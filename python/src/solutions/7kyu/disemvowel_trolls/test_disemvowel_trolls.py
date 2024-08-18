"""https://www.codewars.com/kata/52fba66badcd10859f00097e"""

from solution_disemvowel_trolls import disemvowel


def test_fixed_tests__first_fixed_test():
    assert disemvowel(
        'This website is for losers LOL!') == 'Ths wbst s fr lsrs LL!', 'Incorrect answer for input="This website is for losers LOL!"\n'


def test_fixed_tests__second_fixed_test():
    assert disemvowel(
        "No offense but,\nYour writing is among the worst I've ever read") == "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd", 'Incorrect answer for input="No offense but,\nYour writing is among the worst I\'ve ever read"\n'


def test_fixed_tests__third_fixed_test():
    assert disemvowel(
        'What are you, a communist?') == 'Wht r y,  cmmnst?', 'Incorrect answer for input="What are you, a communist?"\n'

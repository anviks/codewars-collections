"""https://www.codewars.com/kata/51e056fe544cf36c410000fb"""

from solution_most_frequently_used_words_in_a_text import *


def test_top_3_words__sample_tests():
    assert top_3_words('a a a  b  c c  d d d d  e e e e e') == ['e', 'd', 'a']
    assert top_3_words('e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e') == ['e', 'ddd', 'aa']
    assert top_3_words("  //wont won't won't ") == ["won't", 'wont']
    assert top_3_words('  , e   .. ') == ['e']
    assert top_3_words('  ...  ') == []
    assert top_3_words("  '  ") == []
    assert top_3_words("  '''  ") == []
    assert top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
    mind, there lived not long since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income.""") == ['a', 'of', 'on']

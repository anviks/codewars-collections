"""https://www.codewars.com/kata/52449b062fb80683ec000024"""

from solution_the_hashtag_generator import *


def test_fixed_tests__should_generate_the_correct_hashtag_in_fixed_tests():
    assert generate_hashtag('Codewars') == '#Codewars', 'Should handle a single word.'
    assert generate_hashtag('Codewars      ') == '#Codewars', 'Should handle trailing whitespace.'
    assert generate_hashtag('      Codewars') == '#Codewars', 'Should handle leading whitespace.'
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice', 'Should remove spaces.'
    assert generate_hashtag('codewars is nice') == '#CodewarsIsNice', 'Should capitalize first letters of words.'
    assert generate_hashtag(
        'CoDeWaRs is niCe') == '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.'
    assert generate_hashtag(
        'c i n') == '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.'
    assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.'


def test_fixed_tests__should_return_false_if_the_input_is_empty_or_result_is_longer_than_140_chars():
    assert generate_hashtag('') is False, 'Expected an empty string to return False'
    assert generate_hashtag(
        'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') is False, 'Should return False if the final string is longer than 140 chars.'

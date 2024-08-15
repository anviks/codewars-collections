"""https://www.codewars.com/kata/52fba66badcd10859f00097e"""


def disemvowel(string_):
    return "".join(list(filter(lambda x: x.lower() not in ["a", "e", "i", "o", "u"], list(string_))))

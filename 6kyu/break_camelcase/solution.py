"""https://www.codewars.com/kata/5208f99aee097e6552000148"""


def solution(s):
    return __import__('re').sub(r'(?=[A-Z])', ' ', s)

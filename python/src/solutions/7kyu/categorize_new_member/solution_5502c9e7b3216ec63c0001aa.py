"""https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa"""


def open_or_senior(data):
    return ["Senior" if pair[0] >= 55 and pair[1] > 7 else "Open" for pair in data]

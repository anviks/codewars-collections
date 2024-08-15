"""https://www.codewars.com/kata/52449b062fb80683ec000024"""


def generate_hashtag(s):
    return "#" + s.title().replace(" ", "") if 0 < len(s) < 140 else False

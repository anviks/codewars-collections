"""https://www.codewars.com/kata/578aa45ee9fd15ff4600090d"""


def sort_array(source_array: list[int]):
    odds = sorted(n for n in source_array if n % 2)
    odds_index = 0
    new_arr = []

    for n in source_array:
        if n % 2:
            new_arr.append(odds[odds_index])
            odds_index += 1
        else:
            new_arr.append(n)

    return new_arr

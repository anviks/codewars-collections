"""https://www.codewars.com/kata/5826773bfad36332bf0002f9"""

from collections import Counter


def count_and_print_graph(text, max_units_on_screen):
    counter = Counter([c for c in text.lower() if c.isalpha()])
    multiplier = max_units_on_screen / counter.most_common(1)[0][1]
    result = []

    for char, occur in sorted(counter.items(), key=lambda pair: (-pair[1], pair[0])):
        result.append(f"{char}:{'#' * int(occur * multiplier)}")

    return '\n'.join(result)

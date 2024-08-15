"""https://www.codewars.com/kata/520446778469526ec0000001"""


def same_structure_as(original: list, other: list) -> bool:
    if isinstance(original, list) != isinstance(other, list):
        return False
    if isinstance(original, list):
        if len(original) != len(other):
            return False
        return all(same_structure_as(a, b) for a, b in zip(original, other))

    return True

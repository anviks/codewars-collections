"""https://www.codewars.com/kata/520446778469526ec0000001"""


def same_structure_as(original: list, other: list) -> bool:
    if isinstance(original, list) != isinstance(other, list):
        return False
    if isinstance(original, list):
        if len(original) != len(other):
            return False
        return all(same_structure_as(a, b) for a, b in zip(original, other))

    return True


def main():
    from util_funcs import pretty_compare

    pretty_compare(same_structure_as([1, [1, 1]], [2, [2, 2]]), True)
    pretty_compare(same_structure_as([1, [1, 1]], [[2, 2], 2]), False)
    pretty_compare(same_structure_as([1, [1, 1]], [2, [2]]), False)
    pretty_compare(same_structure_as([1, '[', ']'], ['[', ']', 1]), True)


if __name__ == '__main__':
    main()

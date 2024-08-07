"""https://www.codewars.com/kata/57ea70aa5500adfe8a000110"""


def fold_array(array, runs):
    for _ in range(runs):
        length = len(array)
        new_array = []

        for pair in zip(array[:length // 2], array[:length // 2 - 1:-1]):
            new_array.append(sum(pair))

        if length % 2:
            new_array.append(array[length // 2])

        array = new_array

    return array

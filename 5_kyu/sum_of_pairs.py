def sum_pairs(ints, s):
    pairs = []
    indexes = []
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            if ints[i] + ints[j] == s:
                pairs.append([ints[i], ints[j]])
                indexes.append(j)
    return None if not pairs else pairs[indexes.index(min(indexes))]


def sum_pairs_1(ints, s):
    iterated = set()
    for num in ints:
        other_num = s - num
        if other_num in iterated:
            return [other_num, num]
        iterated.add(num)
    return None


def sum_pairs_2(ints, s):
    return next(([complement, num] for i, num in enumerate(ints) if (complement := s - num) in set(ints[:i])), None)


if __name__ == '__main__':
    assert sum_pairs([11, 3, 7, 5], 10) == [3, 7]
    #                     ^--^      3 + 7 = 10

    assert sum_pairs([4, 3, 2, 3, 4], 6) == [4, 2]
    #                 ^-----^         4 + 2 = 6, indices: 0, 2 *
    #                    ^-----^      3 + 3 = 6, indices: 1, 3
    #                       ^-----^   2 + 4 = 6, indices: 2, 4
    #  * the correct answer is the pair whose second value has the smallest index

    assert sum_pairs([0, 0, -2, 3], 2) is None
    #  there are no pairs of values that can be added to produce 2.

    assert sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7]
    #                     ^-----------^   5 + 5 = 10, indices: 1, 5
    #                           ^--^      3 + 7 = 10, indices: 3, 4 *
    #  * the correct answer is the pair whose second value has the smallest index

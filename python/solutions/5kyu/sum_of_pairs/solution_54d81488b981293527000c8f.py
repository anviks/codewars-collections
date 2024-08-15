"""https://www.codewars.com/kata/54d81488b981293527000c8f"""


def sum_pairs(ints, s):
    iterated = set()
    for num in ints:
        other_num = s - num
        if other_num in iterated:
            return [other_num, num]
        iterated.add(num)
    return None


def sum_pairs_1(ints, s):
    pairs = []
    indexes = []
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            if ints[i] + ints[j] == s:
                pairs.append([ints[i], ints[j]])
                indexes.append(j)
    return None if not pairs else pairs[indexes.index(min(indexes))]


def sum_pairs_2(ints, s):
    return next(([complement, num] for i, num in enumerate(ints) if (complement := s - num) in set(ints[:i])), None)

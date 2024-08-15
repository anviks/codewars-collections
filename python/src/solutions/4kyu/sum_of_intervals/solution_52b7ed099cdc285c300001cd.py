"""https://www.codewars.com/kata/52b7ed099cdc285c300001cd"""


def sum_of_intervals(intervals):
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            in1, in2 = intervals[i], intervals[j]

            if in1[1] >= in2[0] and in1[0] <= in2[1]:
                intervals[i] = (0, 0)  # Since removing an item in for loop is bad
                intervals[j] = (min(in1[0], in2[0]), max(in1[1], in2[1]))

    return sum(pair[1] - pair[0] for pair in intervals)

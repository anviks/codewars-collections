"""https://www.codewars.com/kata/569d488d61b812a0f7000015"""


def data_reverse(data: list[int]):
    segment_pairs = len(data) // 16

    for i in range(segment_pairs):
        begin_start, begin_stop = i * 8 or None, (i + 1) * 8
        end_start, end_stop = -begin_stop, -begin_start if begin_start else None
        data[begin_start:begin_stop], data[end_start:end_stop] = data[end_start:end_stop], data[begin_start:begin_stop]

    return data

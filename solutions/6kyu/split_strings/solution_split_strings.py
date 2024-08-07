"""https://www.codewars.com/kata/515de9ae9dcfc28eb6000001"""


def solution(s):
    li = []
    if len(s) % 2:
        s += "_"
    for i in range(0, len(s), 2):
        li.append(s[i:i + 2])
    return li

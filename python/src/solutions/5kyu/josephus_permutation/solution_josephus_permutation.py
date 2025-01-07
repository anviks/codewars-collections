"""https://www.codewars.com/kata/5550d638a99ddb113e0000a2"""


def josephus(items, k):
    i = k - 1
    result = []
    while items:
        i %= len(items)
        result.append(items.pop(i))
        i += k - 1
    return result

def recover_secret(triplets):
    r = list(set([i for l in triplets for i in l]))
    for l in triplets:
        fix(r, l[1], l[2])
        fix(r, l[0], l[1])
    return ''.join(r)


def fix(l, a, b):
    """let sudoku.index(a) < sudoku.index(b)"""
    if l.index(a) > l.index(b):
        l.remove(a)
        l.insert(l.index(b), a)

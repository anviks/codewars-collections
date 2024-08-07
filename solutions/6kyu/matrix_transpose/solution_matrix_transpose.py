"""https://www.codewars.com/kata/52fba2a9adcd10b34300094c"""


def transpose(matrix):
    return [list(t) for t in zip(*matrix)]

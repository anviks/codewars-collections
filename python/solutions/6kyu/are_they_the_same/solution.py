"""https://www.codewars.com/kata/550498447451fbbd7600041c"""


def comp(array1, array2):
    return sorted(map(lambda x: x ** 2, array1)) == sorted(array2) if array1 and array2 else array1 == array2 == []

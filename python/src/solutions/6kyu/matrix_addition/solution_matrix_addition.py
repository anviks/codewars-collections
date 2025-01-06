"""https://www.codewars.com/kata/526233aefd4764272800036f"""


def matrix_addition(a, b):
    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))] 
        for i in range(len(a))
    ]

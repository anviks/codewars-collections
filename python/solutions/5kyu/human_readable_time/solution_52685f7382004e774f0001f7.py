"""https://www.codewars.com/kata/52685f7382004e774f0001f7"""


def make_readable(seconds):
    return f"{(rem := divmod(seconds, 3600))[0]:02}:{(rem := divmod(rem[1], 60))[0]:02}:{rem[1]:02}"

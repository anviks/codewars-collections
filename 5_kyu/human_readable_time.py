"""
https://www.codewars.com/kata/52685f7382004e774f0001f7

**Human Readable Time**

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    return f"{(rem := divmod(seconds, 3600))[0]:02}:{(rem := divmod(rem[1], 60))[0]:02}:{rem[1]:02}"


if __name__ == '__main__':
    print(make_readable(0))  # "00:00:00"
    print(make_readable(5))  # "00:00:05"
    print(make_readable(60))  # "00:01:00"
    print(make_readable(86399))  # "23:59:59"
    print(make_readable(359999))  # "99:59:59"

    # Other solutions from Codewars:
    # def make_readable(seconds):
    #     return '{:02}:{:02}:{:02}'.format(seconds / 3600, seconds / 60 % 60, seconds % 60)

    # def make_readable(seconds):
    #     return '{:02}:{:02}:{:02}'.format(seconds // 3600, seconds // 60 % 60, seconds % 60)

    # def make_readable(seconds):
    #     return '{:02}:{:02}:{:02}'.format(*divmod(seconds, 60 ** 2 + 60))


"""https://www.codewars.com/kata/one-line-task-squirrel-and-tree"""


def squirrel_long(h, H, S):
    round_trips = H / h
    triangle_base = round_trips * S
    hypotenuse = (triangle_base ** 2 + H ** 2) ** 0.5

    return round(hypotenuse, 4)


# @formatter:off
squirrel=lambda h,H,S:round(((H/h*S)**2+H*H)**.5,4)
# @formatter:on

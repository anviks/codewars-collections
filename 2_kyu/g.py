# from numpy import*;circleIntersection=lambda a,b,r:r*r*(lambda h:h<1and arccos(h)-h*(1-h*h)**.5)(hypot(*subtract(b,a))/r/2)//.5

from numpy import *


def calculate_arc_length(h):
    return h < 1 and arccos(h) - h * sqrt(1 - h * h)


def circleIntersection(coord1, coord2, radius):
    distance = hypot(*subtract(coord2, coord1))
    relative_distance = distance / radius / 2
    print(relative_distance)

    return radius * radius * calculate_arc_length(relative_distance) // 0.5


print(circleIntersection([0, 0], [7, 0], 5))  # 14
print(circleIntersection([0, 0], [0, 10], 10))  # 122

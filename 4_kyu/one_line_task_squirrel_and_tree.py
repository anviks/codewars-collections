"""https://www.codewars.com/kata/one-line-task-squirrel-and-tree"""


# def squirrel(h, H, S):
#     round_trips = H / h
#     triangle_base = round_trips * S
#     hypotenuse = (triangle_base ** 2 + H ** 2) ** 0.5
# 
#     return round(hypotenuse, 4)


squirrel=lambda h,H,S:round(((H/h*S)**2+H*H)**.5,4)


def main():
    print(squirrel(4, 16, 3) == 20)
    print(squirrel(4, 4, 3) == 5)
    print(squirrel(8, 9, 37) == 42.5869)
    print(squirrel(526, 682, 140) == 705.7435)
    print(squirrel(247, 857, 669) == 2474.3392)
    print(squirrel(2, 11, 47) == 258.7339)
    print(squirrel(73, 97, 244) == 338.4185)
    print(squirrel(15, 774, 948) == 48922.923)
    print(squirrel(21, 29, 60) == 87.7856)
    print(squirrel(83, 97, 86) == 139.6799)


if __name__ == '__main__':
    main()

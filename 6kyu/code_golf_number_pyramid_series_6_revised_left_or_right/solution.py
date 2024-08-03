"""https://www.codewars.com/kata/62eedcfc729041000ea082c1"""

import math


def left_righ(n):
    row = math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2)
    center_member = (row * (row + 1)) // 2
    print(n, row, center_member)
    return 'L' if n < center_member else 'R' if n > center_member else 'C'


left_right=lambda n:'L'if(g:=n-((((r:=math.ceil((-1+math.sqrt(1+8*n))/2))*(r-1))//2+1)+(r-1)/2))<0else'R'if g>0else'C'


left_right_top_answer=lambda n:'CLR'[int((8*n-4)**.5%2//-1)]

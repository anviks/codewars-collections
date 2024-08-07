"""https://www.codewars.com/kata/one-line-task-zero-or-one"""

# @formatter:off
zero_or_one=lambda n,s:[sum(c)>n/2 for c in zip(*s)]
# @formatter:on

"""https://www.codewars.com/kata/one-line-task-palindrome-string"""

# @formatter:off
palindrome=lambda n,c:c+c[-1]*(n-len(c)*2+1)+c[-2::-1]
# @formatter:on

"""https://www.codewars.com/kata/514b92a657cdc65150000006"""

solution = lambda n: sum(i for i in range(n) if not i % 3 or not i % 5)

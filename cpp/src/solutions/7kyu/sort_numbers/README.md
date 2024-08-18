# [Sort Numbers](https://www.codewars.com/kata/5174a4c0f2769dd8b1000003)

Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:







```python
solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
```










## Lambda Calculus

- Purity: LetRec
- Num encoding: BinaryScott
- For LC, there won't be `null` inputs.
- Instead of arrays, we have cons lists. Define the following, which the tests will use to construct inputs and test outputs:
  - `nil : List a` (empty list)
  - `cons : a -> List a -> List a` (add to head)
  - `foldr : (a -> b -> b) -> b -> List a -> b` (right-associative fold / reduce)

### Optional Performance Check

By default the tests are lenient with respect to performance. If you would like to demonstrate that your solution is fast, you can opt in to a stricter test suite ( more lists, longer lists, higher numbers ). Just change `perf-tests = Low` to `perf-tests = High`.
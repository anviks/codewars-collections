# [Sum of Intervals](https://www.codewars.com/kata/52b7ed099cdc285c300001cd)

Write a function called `sumIntervals`/`sum_intervals` that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

### Intervals

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: `[1, 5]` is an interval from `1` to `5`. The length of this interval is `4`.

### Overlapping Intervals

List containing overlapping intervals:



The sum of the lengths of these intervals is `7`. Since `[1, 4]` and `[3, 5]` overlap, we can treat the interval as `[1, 5]`, which has a length of `4`.

### Examples:



### Tests with large intervals

Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range `[-1000000000, 1000000000]`.


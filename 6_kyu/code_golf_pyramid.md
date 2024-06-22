_(Revised version from previous series 6)_

# Number Pyramid:

Image a number pyramid starts with `1`, and the numbers increasing by `1`. 

Today, it has total `5000` levels.

For example, the top 4 levels of the pyramid looks like:

```
    1
   2 3
  4 5 6
 7 8 9 10
```
___
# Left and Right:
Now from the center line, cut the pyramid into `Left` and `Right`.

In the above example, it will become:

```
Left: # Right:
      #
   2  # 3
  4   #  6
 7 8  # 9 10

 (The numbers of center line was cut, do not go on any side.)
```
___
# Input:

You will be given a number `n`, it will not go beyond `5000` levels.
___
# Output:

You need to return the number is locating at `Left` or `Right` part.

* Return `'L'` for Left.

* Return `'R'` for Right.

* Return `'C'` for Center/been Cut

__Examples:__
```
left_right(1) --> 'C'
left_right(2) --> 'L'
left_right(3) --> 'R'
left_right(4) --> 'L'
left_right(5) --> 'C'
left_right(6) --> 'R'
```

___
# Golfing Message:

The length of your code should be less or equal to `72`.

The length of reference solution is `65` (Python) and `67` (JS).
___
If you like this series, welcome to do [other kata](https://www.codewars.com/collections/code-golf-number-pyramid-series) of it.
# [Church Booleans](https://www.codewars.com/kata/5ac739ed3fdf73d3f0000048)

There are [a](https://www.codewars.com/kata/church-numbers-add-multiply-exponents) [few](https://www.codewars.com/kata/church-numbers-1) [Katas](https://www.codewars.com/kata/church-numbers-ii) about Church Numerals so let's talk about booleans.

In lambda calculus, the only primitive are lambdas. No numbers, no strings, and of course no booleans. Everything is reduced to anonymous functions.

Booleans are defined thusly (this definition is preloaded for you) :



```python
true  = lambda t: lambda f: t
false = lambda t: lambda f: f
```


Your task will be to implement basic operators on booleans (using only lambdas and function application) : `Not`, `And`, `Or` and `Xor`.

To help, the function `unchurch` comes preloaded, and returns the native boolean given a church boolean :

```python
unchurch(true)  # True
```

<i>Note: You should not use the following:

* native booleans
* native boolean operators</i>


# [Palindrome Counter](https://www.codewars.com/kata/64607242d3560e0043c3de25)

# Background

Palindromes are a special type of number (in this case a non-negative integer) that reads the same backwards as forwards. A number defined this way is called __palindromic__. 

* The following numbers are palindromes: `0`, `252`, `769967`, `1111111`. 

* The following numbers are __not__ palindromes: `123`, `689`, `565656`, `12345432`. 

# Problem Description

In this kata, you are required to build a function that receives two arguments, `a` and `b`, and returns the number of integer palindromes between `a` and `b` inclusive. 

# Examples

* If `a` is `6` and `b` is `11`, the function should output `5` because there are 5 palindromes between 6 and 11 inclusive: `6`, `7`, `8`, `9` and `11`. 

* If `a` is `150` and `b` is `250`, the function should output `10` because there are 10 palindromes between 150 and 250 inclusive: `151`, `161`, `171`, `181`, `191`, `202`, `212`, `222`, `232` and `242`. 

* If `a` is `1002` and `b` is `1110`, the function should output `0`: there are no palindromes between 1002 and 1110 inclusive. 

# Input Constraints

* Fixed test cases: `0` ≤ `a, b` ≤ `100` (one hundred)

* Small test cases: `0` ≤ `a, b` ≤ `10^5` (one hundred thousand)

* Medium test cases: `0` ≤ `a, b` ≤ `10^10` (ten billion)

* Large test cases: `0` ≤ `a, b` ≤ `10^15` (one quadrillion)

Ideally, a program should pass all the test cases in no more than 800 milliseconds. 

# Edge Cases

* Note that `0` is palindromic. 

* Numbers except `0` that start with `0` do __not__ count. 

* If `a` and `b` are not integers, round `a` up and `b` down. 

This is my first kata created. Hope you enjoy! <3
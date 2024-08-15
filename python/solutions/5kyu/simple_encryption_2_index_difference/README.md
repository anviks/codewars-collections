For encrypting strings this region of chars is given (in this order!):

* all letters (ascending, first all UpperCase, then all LowerCase)
* all digits (ascending)
* the following chars: `.,:;-?! '()$%&"` 

These are 77 chars! (This region is zero-based.)<br/>

Write two methods: <br/>
```python
def encrypt(text)
def decrypt(encrypted_text)
```
Prechecks:<br>
1. If the input-string has chars, that are not in the region, throw an Exception(C#, Python) or Error(JavaScript).<br>
2. If the input-string is null or empty return exactly this value!<br>

For building the encrypted string:<br>
1. For every second char do a switch of the case.<br>
2. For every char take the index from the region. Take the difference from the region-index of the char before (from the input text! Not from the fresh encrypted char before!). (Char2 = Char1-Char2)<br>
Replace the original char by the char of the difference-value from the region. In this step the first letter of the text is unchanged.<br>
3. Replace the first char by the mirror in the given region. (`'A' -> '"'`, `'B' -> '&'`, ...)

Simple example:

* Input:  `"Business"`
* Step 1: `"BUsInEsS"`
* Step 2: `"B61kujla"`
  * `B -> U`
    * `B (1) - U (20) = -19`
    * `-19 + 77 = 58`
    * `Region[58] = "6"`
  * `U -> s`
    * `U (20) - s (44) = -24`
    * `-24 + 77 = 53`
    * `Region[53] = "1"`
* Step 3: `"&61kujla"`

This kata is part of the Simple Encryption Series:<br>
<a href="https://www.codewars.com/kata/simple-encryption-number-1-alternating-split" taget=_blank>Simple Encryption #1 - Alternating Split</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-2-index-difference" taget=_blank>Simple Encryption #2 - Index-Difference</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-3-turn-the-bits-around" taget=_blank>Simple Encryption #3 - Turn The Bits Around</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-4-qwerty" taget=_blank>Simple Encryption #4 - Qwerty</a><br>

Have fun coding it and please don't forget to vote and rank this kata! :-)
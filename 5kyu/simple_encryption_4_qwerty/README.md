<p>You have to write two methods to <em>encrypt</em> and <em>decrypt</em> strings.
Both methods have two parameters:</p>
<pre><code>1. The string to encrypt/decrypt
2. The Qwerty-Encryption-Key (000-999) 
</code></pre>
<p>The rules are very easy:</p>
<pre><code>The crypting-regions are these 3 lines from your keyboard:
1. "qwertyuiop"
2. "asdfghjkl"
3. "zxcvbnm,."

If a char of the string is not in any of these regions, take the char direct in the output.
If a char of the string is in one of these regions: Move it by the part of the key in the 
region and take this char at the position from the region. 
If the movement is over the length of the region, continue at the beginning.
The encrypted char must have the same case like the decrypted char! 
So for upperCase-chars the regions are the same, but with pressed "SHIFT"!

The Encryption-Key is an integer number from 000 to 999. E.g.: 127

The first digit of the key (e.g. 1) is the movement for the first line.
The second digit of the key (e.g. 2) is the movement for the second line.
The third digit of the key (e.g. 7) is the movement for the third line.

(Consider that the key is an integer! When you got a 0 this would mean 000. A 1 would mean 001. And so on.)
</code></pre>
<p>You do not need to do any prechecks. The strings will always be not null 
and will always have a length &gt; 0. You do not have to throw any exceptions.</p>
<p>An Example:</p>
<pre><code>Encrypt "Ball" with key 134
1. "B" is in the third region line. Move per 4 places in the region. -&gt; "&gt;" (Also "upperCase"!)
2. "a" is in the second region line. Move per 3 places in the region. -&gt; "f"
3. "l" is in the second region line. Move per 3 places in the region. -&gt; "d"
4. "l" is in the second region line. Move per 3 places in the region. -&gt; "d"
--&gt; Output would be "&gt;fdd"
</code></pre>
<p><em>Hint: Don't forget: The regions are from an US-Keyboard!<br></em>
<em>In doubt google for "US Keyboard."</em>
<br><br></p>
<p>This kata is part of the Simple Encryption Series:<br>
<a href="https://www.codewars.com/kata/simple-encryption-number-1-alternating-split" data-turbolinks="false" target="_blank">Simple Encryption #1 - Alternating Split</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-2-index-difference" data-turbolinks="false" target="_blank">Simple Encryption #2 - Index-Difference</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-3-turn-the-bits-around" data-turbolinks="false" target="_blank">Simple Encryption #3 - Turn The Bits Around</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-4-qwerty" data-turbolinks="false" target="_blank">Simple Encryption #4 - Qwerty</a><br></p>
<p>Have fun coding it and please don't forget to vote and rank this kata! :-)</p>

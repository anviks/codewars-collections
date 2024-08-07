<p>Implement a pseudo-encryption algorithm which given a string <code>S</code> and an integer <code>N</code> concatenates all the odd-indexed characters of <code>S</code> with all the even-indexed characters of <code>S</code>, this process should be repeated <code>N</code> times.</p>
<p>Examples:</p>
<pre><code>encrypt("012345", 1)  =&gt;  "135024"
encrypt("012345", 2)  =&gt;  "135024"  -&gt;  "304152"
encrypt("012345", 3)  =&gt;  "135024"  -&gt;  "304152"  -&gt;  "012345"

encrypt("01234", 1)  =&gt;  "13024"
encrypt("01234", 2)  =&gt;  "13024"  -&gt;  "32104"
encrypt("01234", 3)  =&gt;  "13024"  -&gt;  "32104"  -&gt;  "20314"
</code></pre>
<p>Together with the encryption function, you should also implement a decryption function which reverses the process.</p>
<p>If the string <code>S</code> is an empty value or the integer <code>N</code> is not positive, return the first argument without changes.</p>
<hr>
<p>This kata is part of the Simple Encryption Series:</p>
<ul>
<li><a href="https://www.codewars.com/kata/simple-encryption-number-1-alternating-split" data-turbolinks="false" target="_blank">Simple Encryption #1 - Alternating Split</a></li>
<li><a href="https://www.codewars.com/kata/simple-encryption-number-2-index-difference" data-turbolinks="false" target="_blank">Simple Encryption #2 - Index-Difference</a></li>
<li><a href="https://www.codewars.com/kata/simple-encryption-number-3-turn-the-bits-around" data-turbolinks="false" target="_blank">Simple Encryption #3 - Turn The Bits Around</a></li>
<li><a href="https://www.codewars.com/kata/simple-encryption-number-4-qwerty" data-turbolinks="false" target="_blank">Simple Encryption #4 - Qwerty</a></li>
</ul>
<p>Have fun coding it and please don't forget to vote and rank this kata! :-)</p>

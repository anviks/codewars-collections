<p>You are asked to write a simple cypher that rotates every character (in range [a-zA-Z], special chars will be ignored by the cipher) by 13 chars. As an addition to the original ROT13 cipher, this cypher will also cypher numerical digits ([0-9]) with 5 chars.</p>
<p>Example:</p>
<pre><code>"The quick brown fox jumps over the 2 lazy dogs"
</code></pre>
<p>will be cyphered to:</p>
<pre><code>"Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf"
</code></pre>
<p>Your task is to write a ROT13.5 (ROT135) method that accepts a string and encrypts it.
Decrypting is performed by using the same method, but by passing the encrypted string again.</p>
<p>Note: when an empty string is passed, the result is also empty.</p>
<p>When passing your succesful algorithm, some random tests will also be applied. Have fun!</p>

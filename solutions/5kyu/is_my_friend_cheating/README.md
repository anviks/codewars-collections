<ul>
<li>A friend of mine takes the sequence of all numbers from 1 to n (where n &gt; 0).</li>
<li>Within that sequence, he chooses two numbers, a and b.</li>
<li>He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.</li>
<li>Given a number n, could you tell me the numbers he excluded from the sequence?</li>
</ul>
<p>The function takes the parameter: <code>n</code> 
(n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form: </p>
<pre><code>[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
</code></pre>
<p>with <strong>all</strong> <code>(a, b)</code> which are the possible removed numbers in the sequence <code>1 to n</code>.</p>
<p><code>[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ... </code>will be sorted in increasing order of the "a".</p>
<p>It happens that there are several possible (a, b).
The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return <code>nil</code>).</p>
<h4 id="examples">Examples:</h4>
<pre><code>removNb(26) should return [(15, 21), (21, 15)]
or
removNb(26) should return { {15, 21}, {21, 15} }
or
removeNb(26) should return [[15, 21], [21, 15]]
or
removNb(26) should return [ {15, 21}, {21, 15} ]
or
removNb(26) should return "15 21, 21 15"
</code></pre>
<p>or</p>
<pre><code>in C:
removNb(26) should return  {{15, 21}{21, 15}} tested by way of strings.
Function removNb should return a pointer to an allocated array of Pair pointers, each one also allocated. 
</code></pre>
<h4 id="note">Note</h4>
<p>See examples of returns for each language in "RUN SAMPLE TESTS"</p>

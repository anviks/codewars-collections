<p>Given an array of integers of any length, return an array that has 1 added to the value represented by the array.</p>
<ul>
<li>the array can't be empty</li>
<li>only non-negative, single digit integers are allowed</li>
</ul>
<p>Return <code>nil</code> (or your language's equivalent) for invalid inputs.</p>
<h3 id="examples">Examples</h3>
<p><strong>Valid arrays</strong></p>
<p><code>[4, 3, 2, 5]</code> would return <code>[4, 3, 2, 6]</code><br><code>[1, 2, 3, 9]</code> would return <code>[1, 2, 4, 0]</code><br><code>[9, 9, 9, 9]</code> would return <code>[1, 0, 0, 0, 0]</code><br><code>[0, 1, 3, 7]</code> would return <code>[0, 1, 3, 8]</code></p>
<p><strong>Invalid arrays</strong></p>
<p><code>[1, -9]</code> is invalid because <code>-9</code> is <strong>not a non-negative integer</strong></p>
<p><code>[1, 2, 33]</code> is invalid because <code>33</code> is <strong>not a single-digit integer</strong></p>

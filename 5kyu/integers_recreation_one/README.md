<p><code>1, 246, 2, 123, 3, 82, 6, 41</code> are the divisors of number <code>246</code>. Squaring these divisors we get: <code>1, 60516, 4, 15129, 9, 6724, 36, 1681</code>. The sum of these squares is <code>84100</code> which is <code>290 * 290</code>.</p>
<h4 id="task">Task</h4>
<p>Find all integers between <code>m</code> and <code>n</code> (m and n integers with 1 &lt;= m &lt;= n) such that the sum of their squared divisors is itself a square. </p>
<p>We will return an array of subarrays or of tuples (in C an array of Pair) or a string. 
The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.</p>
<h4 id="example">Example:</h4>
<pre><code>list_squared(1, 250) --&gt; [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --&gt; [[42, 2500], [246, 84100]]
</code></pre>
<p>The form of the examples may change according to the language, see "Sample Tests".</p>
<h4 id="note">Note</h4>
<p>In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.</p>

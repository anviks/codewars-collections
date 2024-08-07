<p>The Collatz conjecture states that repeated application of the function</p>
<pre><code>f(n) = n / 2 if n is even, 3 * n + 1 if n is odd
</code></pre>
<p>will eventually reach the value <code>1</code> from all positive integer starting values <code>n</code>. Because <code>3 * n + 1</code> is always even for odd values of <code>n</code>, we often use the "shortcut" form of the function instead, defined as</p>
<pre><code>g(n) = n / 2 if n is even, (3 * n + 1) / 2 if n is odd.
</code></pre>
<p>Calculate function <code>g(n)</code> in <code>&lt;= 26</code> characters, where <code>1 &lt;= n &lt;= 80_000</code>.</p>

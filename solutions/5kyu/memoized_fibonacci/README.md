<h3 id="problem-context">Problem Context</h3>
<p>The <a href="http://en.wikipedia.org/wiki/Fibonacci_number" data-turbolinks="false" target="_blank">Fibonacci</a> sequence is traditionally used to explain tree recursion.  </p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">fibonacci</span>(<span class="cm-def">n</span>) {
    <span class="cm-keyword">if</span>(<span class="cm-variable-2">n</span><span class="cm-operator">==</span><span class="cm-number">0</span> <span class="cm-operator">||</span> <span class="cm-variable-2">n</span> <span class="cm-operator">==</span> <span class="cm-number">1</span>)
        <span class="cm-keyword">return</span> <span class="cm-variable-2">n</span>;
    <span class="cm-keyword">return</span> <span class="cm-variable">fibonacci</span>(<span class="cm-variable-2">n</span><span class="cm-operator">-</span><span class="cm-number">1</span>) <span class="cm-operator">+</span> <span class="cm-variable">fibonacci</span>(<span class="cm-variable-2">n</span><span class="cm-operator">-</span><span class="cm-number">2</span>);
}
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-keyword">def</span> <span class="cm-def">fibonacci</span>(<span class="cm-variable">n</span>)
  <span class="cm-keyword">return</span> <span class="cm-variable">n</span> <span class="cm-keyword">if</span> (<span class="cm-number">0</span><span class="cm-operator">..</span><span class="cm-number">1</span>)<span class="cm-operator">.</span><span class="cm-property">include?</span> <span class="cm-variable">n</span>
  <span class="cm-variable">fibonacci</span>(<span class="cm-variable">n</span> <span class="cm-operator">-</span> <span class="cm-number">1</span>) <span class="cm-operator">+</span> <span class="cm-variable">fibonacci</span>(<span class="cm-variable">n</span> <span class="cm-operator">-</span> <span class="cm-number">2</span>)
<span class="cm-keyword">end</span>
</code></pre>
<pre><code class="language-python"><span class="cm-keyword">def</span> <span class="cm-def">fibonacci</span>(<span class="cm-variable">n</span>):
    <span class="cm-keyword">if</span> <span class="cm-variable">n</span> <span class="cm-keyword">in</span> [<span class="cm-number">0</span>, <span class="cm-number">1</span>]:
        <span class="cm-keyword">return</span> <span class="cm-variable">n</span>
    <span class="cm-keyword">return</span> <span class="cm-variable">fibonacci</span>(<span class="cm-variable">n</span> <span class="cm-operator">-</span> <span class="cm-number">1</span>) <span class="cm-operator">+</span> <span class="cm-variable">fibonacci</span>(<span class="cm-variable">n</span> <span class="cm-operator">-</span> <span class="cm-number">2</span>)
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">fibonacci</span> <span class="cm-number">0</span> <span class="cm-keyword">=</span> <span class="cm-number">0</span>
<span class="cm-variable">fibonacci</span> <span class="cm-number">1</span> <span class="cm-keyword">=</span> <span class="cm-number">1</span>
<span class="cm-variable">fibonacci</span> <span class="cm-variable">n</span> <span class="cm-keyword">=</span> <span class="cm-variable">fibonacci</span> (<span class="cm-variable">n</span><span class="cm-builtin">-</span><span class="cm-number">1</span>) <span class="cm-builtin">+</span> <span class="cm-variable">fibonacci</span> (<span class="cm-variable">n</span><span class="cm-builtin">-</span><span class="cm-number">2</span>)
</code></pre>
<pre style="display: none;"><code class="language-lambdacalc"><span class="cm-variable-2">fibonacci</span> <span class="cm-text">=</span> <span class="cm-keyword">\</span> <span class="cm-def">n</span> <span class="cm-keyword">.</span> <span class="cm-text">if</span> <span class="cm-bracket">(</span><span class="cm-text">is-zero</span> <span class="cm-text">n</span><span class="cm-bracket">)</span>
                    <span class="cm-number">0</span>
                  <span class="cm-bracket">(</span><span class="cm-text">if</span> <span class="cm-bracket">(</span><span class="cm-text">is-zero</span> <span class="cm-bracket">(</span><span class="cm-text">pred</span> <span class="cm-text">n</span><span class="cm-bracket">)</span><span class="cm-bracket">)</span>
                    <span class="cm-number">1</span>
                  <span class="cm-comment"># else</span>
                    <span class="cm-bracket">(</span><span class="cm-text">add</span> <span class="cm-bracket">(</span><span class="cm-text">fibonacci</span> <span class="cm-bracket">(</span><span class="cm-text">pred</span> <span class="cm-text">n</span><span class="cm-bracket">)</span><span class="cm-bracket">)</span> <span class="cm-bracket">(</span><span class="cm-text">fibonacci</span> <span class="cm-bracket">(</span><span class="cm-text">pred</span> <span class="cm-bracket">(</span><span class="cm-text">pred</span> <span class="cm-text">n</span><span class="cm-bracket">)</span><span class="cm-bracket">)</span><span class="cm-bracket">)</span>
                  <span class="cm-bracket">)</span><span class="cm-bracket">)</span>
</code></pre>
<pre style="display: none;"><code class="language-scala"><span class="cm-keyword">def</span> <span class="cm-def">fibonacci</span>(<span class="cm-variable">n</span>: <span class="cm-type">Int</span>): <span class="cm-type">Int</span> <span class="cm-operator">=</span> <span class="cm-variable">n</span> <span class="cm-keyword">match</span> {
   <span class="cm-keyword">case</span> <span class="cm-number">0</span> <span class="cm-operator">|</span> <span class="cm-number">1</span> <span class="cm-operator">=&gt;</span> <span class="cm-variable">n</span>
   <span class="cm-keyword">case</span> <span class="cm-keyword">_</span> <span class="cm-operator">=&gt;</span> <span class="cm-variable">fibonacci</span>(<span class="cm-variable">n</span> <span class="cm-operator">-</span> <span class="cm-number">1</span>) <span class="cm-operator">+</span> <span class="cm-variable">fibonacci</span>(<span class="cm-variable">n</span> <span class="cm-operator">-</span> <span class="cm-number">2</span>)
}
</code></pre>
<p>This algorithm serves welll its educative purpose but it's <a href="https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.2" data-turbolinks="false" target="_blank">tremendously inefficient</a>, not only because of recursion, but because we invoke the fibonacci function twice, and the right branch of recursion (i.e. <code>fibonacci(n-2)</code>) recalculates all the Fibonacci numbers already calculated by the left branch (i.e. <code>fibonacci(n-1)</code>).</p>
<p>This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much. You may go for a cup of coffee or go take a nap while you wait for the answer. But if you try it here in Code Wars you will most likely get a code timeout before any answers.</p>
<p>For this particular Kata we want to <strong>implement the memoization solution</strong>. This will be cool because it will let us <em>keep using the tree recursion</em> algorithm while still keeping it sufficiently optimized to get an answer very rapidly.</p>
<p>The trick of the memoized version is that we will keep a cache data structure (most likely an associative array) where we will store the Fibonacci numbers as we calculate them. When a Fibonacci number is calculated, we first look it up in the cache, if it's not there, we calculate it and put it in the cache, otherwise we returned the cached number.</p>
<p>Refactor the function into a recursive Fibonacci function that using a memoized data structure avoids the deficiencies of tree recursion. Can you make it so the memoization cache is private to this function?</p>

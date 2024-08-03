<p>Write a function </p>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">TripleDouble</span>(<span class="cm-type">long</span> <span class="cm-variable">num1</span>, <span class="cm-type">long</span> <span class="cm-variable">num2</span>)
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">TripleDouble</span>(<span class="cm-type">long</span> <span class="cm-variable">num1</span>, <span class="cm-type">long</span> <span class="cm-variable">num2</span>)
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">tripledouble</span>(<span class="cm-variable">num1</span>,<span class="cm-variable">num2</span>)
</code></pre>
<pre><code class="language-python"><span class="cm-variable">triple_double</span>(<span class="cm-variable">num1</span>, <span class="cm-variable">num2</span>)
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">triple_double</span>(<span class="cm-variable">num1</span>, <span class="cm-variable">num2</span>)
</code></pre>
<pre style="display: none;"><code class="language-scala"><span class="cm-variable">tripleDouble</span>(<span class="cm-variable">num1</span>: <span class="cm-type">Long</span>, <span class="cm-variable">num2</span>: <span class="cm-type">Long</span>): <span class="cm-type">Int</span>
</code></pre>
<p>which takes numbers <code>num1</code> and <code>num2</code> and returns <code>1</code> if there is a straight triple of a number at any place in <code>num1</code> and also a straight double of the <strong>same</strong> number in <code>num2</code>.</p>
<p>If this isn't the case, return <code>0</code></p>
<h2 id="examples">Examples</h2>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">tripledouble</span>(<span class="cm-number">451999277</span>, <span class="cm-number">41177722899</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span> <span class="cm-comment">// num1 has straight triple 999s and </span>
                                          <span class="cm-comment">// num2 has straight double 99s</span>

<span class="cm-variable">tripledouble</span>(<span class="cm-number">1222345</span>, <span class="cm-number">
12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span> <span class="cm-comment">// num1 has
straight triple 2s but num2 has only a single 2</span>

<span class="cm-variable">tripledouble</span>(<span class="cm-number">12345</span>, <span class="cm-number">
12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>

<span class="cm-variable">tripledouble</span>(<span class="cm-number">666789</span>, <span class="cm-number">
12345667</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">TripleDouble</span>(<span class="cm-number">451999277</span>, <span class="cm-number">41177722899</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span> <span class="cm-comment">// num1 has straight triple 999s and </span>
                                          <span class="cm-comment">// num2 has straight double 99s</span>

<span class="cm-variable">TripleDouble</span>(<span class="cm-number">1222345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span> <span class="cm-comment">// num1 has straight triple 2s but num2 has only a single 2</span>

<span class="cm-variable">TripleDouble</span>(<span class="cm-number">12345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>

<span class="cm-variable">TripleDouble</span>(<span class="cm-number">666789</span>, <span class="cm-number">12345667</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">TripleDouble</span>(<span class="cm-number">451999277</span>, <span class="cm-number">41177722899</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span> <span class="cm-comment">// num1 has straight triple 999s and </span>
                                          <span class="cm-comment">// num2 has straight double 99s</span>

<span class="cm-variable">TripleDouble</span>(<span class="cm-number">1222345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span> <span class="cm-comment">// num1 has straight triple 2s but num2 has only a single 2</span>

<span class="cm-variable">TripleDouble</span>(<span class="cm-number">12345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>

<span class="cm-variable">TripleDouble</span>(<span class="cm-number">666789</span>, <span class="cm-number">12345667</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">triple_double</span>(<span class="cm-number">451999277</span>, <span class="cm-number">41177722899</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>
<span class="cm-comment"># num1 has straight triple 999s and num2 has straight double 99s</span>

<span class="cm-variable">triple_double</span>(<span class="cm-number">1222345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>
<span class="cm-comment"># num1 has straight triple 2s but num2 has only a single 2</span>

<span class="cm-variable">triple_double</span>(<span class="cm-number">12345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>

<span class="cm-variable">triple_double</span>(<span class="cm-number">666789</span>, <span class="cm-number">12345667</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">triple_double</span>(<span class="cm-number">451999277</span>, <span class="cm-number">41177722899</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>
<span class="cm-comment"># num1 has straight triple 999s and  num2 has straight double 99s</span>

<span class="cm-variable">triple_double</span>(<span class="cm-number">1222345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>
<span class="cm-comment"># num1 has straight triple 2s but num2 has only a single 2</span>

<span class="cm-variable">triple_double</span>(<span class="cm-number">12345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>

<span class="cm-variable">triple_double</span>(<span class="cm-number">666789</span>, <span class="cm-number">12345667</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>
</code></pre>
<pre style="display: none;"><code class="language-scala"><span class="cm-comment">// num1 has straight triple 999s and num2 has straight double 99s</span>
<span class="cm-variable">tripleDouble</span>(<span class="cm-number">451999277</span>, <span class="cm-number">41177722899</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>

<span class="cm-comment">// num1 has straight triple 2s but num2 has only a single 2:</span>
<span class="cm-variable">tripleDouble</span>(<span class="cm-number">1222345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>

<span class="cm-variable">tripleDouble</span>(<span class="cm-number">12345</span>, <span class="cm-number">12345</span>) <span class="cm-operator">==</span> <span class="cm-number">0</span>

<span class="cm-variable">tripleDouble</span>(<span class="cm-number">666789</span>, <span class="cm-number">12345667</span>) <span class="cm-operator">==</span> <span class="cm-number">1</span>
</code></pre>

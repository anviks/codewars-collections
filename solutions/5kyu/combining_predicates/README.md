<h1 id="task">Task</h1>
<p>Create a decorator <code>@predicate</code> which allows boolean functions to be conveniently combined using <code>&amp;</code>, <code>|</code> and <code>~</code> operators:</p>
<pre><code class="language-python"><span class="cm-meta">@</span><span class="cm-meta">predicate</span>
<span class="cm-keyword">def</span> <span class="cm-def">is_even</span>(<span class="cm-variable">num</span>):
    <span class="cm-keyword">return</span> <span class="cm-variable">num</span> <span class="cm-operator">%</span> <span class="cm-number">2</span> <span class="cm-operator">==</span> <span class="cm-number">0</span>

<span class="cm-meta">@</span><span class="cm-meta">predicate</span>
<span class="cm-keyword">def</span> <span class="cm-def">is_positive</span>(<span class="cm-variable">num</span>):
    <span class="cm-keyword">return</span> <span class="cm-variable">num</span> <span class="cm-operator">&gt;</span> <span class="cm-number">0</span>

(<span class="cm-variable">is_even</span> <span class="cm-operator">&amp;</span> <span class="cm-variable">is_positive</span>)(<span class="cm-number">4</span>)   <span class="cm-comment"># True</span>
(<span class="cm-variable">is_even</span> <span class="cm-operator">&amp;</span> <span class="cm-variable">is_positive</span>)(<span class="cm-number">3</span>)   <span class="cm-comment"># False</span>
(<span class="cm-variable">is_even</span> <span class="cm-operator">|</span> <span class="cm-variable">is_positive</span>)(<span class="cm-number">3</span>)   <span class="cm-comment"># True</span>
(<span class="cm-operator">~</span><span class="cm-variable">is_even</span> <span class="cm-operator">&amp;</span> <span class="cm-variable">is_positive</span>)(<span class="cm-number">3</span>)  <span class="cm-comment"># True</span>
</code></pre>
<p>It should work with all functions, regardless of how many arguments they accept:</p>
<pre><code class="language-python"><span class="cm-meta">@</span><span class="cm-meta">predicate</span>
<span class="cm-keyword">def</span> <span class="cm-def">to_be</span>():
    <span class="cm-keyword">return</span> <span class="cm-keyword">True</span>

(<span class="cm-variable">to_be</span> <span class="cm-operator">|</span> <span class="cm-operator">~</span><span class="cm-variable">to_be</span>)()  <span class="cm-comment"># True</span>

<span class="cm-meta">@</span><span class="cm-meta">predicate</span>
<span class="cm-keyword">def</span> <span class="cm-def">is_equal</span>(<span class="cm-variable">a</span>, <span class="cm-variable">b</span>):
    <span class="cm-keyword">return</span> <span class="cm-variable">a</span> <span class="cm-operator">==</span> <span class="cm-variable">b</span>

<span class="cm-meta">@</span><span class="cm-meta">predicate</span>
<span class="cm-keyword">def</span> <span class="cm-def">is_less_than</span>(<span class="cm-variable">a</span>, <span class="cm-variable">b</span>):
    <span class="cm-keyword">return</span> <span class="cm-variable">a</span> <span class="cm-operator">&lt;</span> <span class="cm-variable">b</span>

(<span class="cm-variable">is_less_than</span> <span class="cm-operator">|</span> <span class="cm-variable">is_equal</span>)(<span class="cm-number">1</span>, <span class="cm-number">2</span>)      <span class="cm-comment"># True</span>
</code></pre>
<p>Keyword arguments should work as well:</p>
<pre><code class="language-python">(<span class="cm-variable">is_less_than</span> <span class="cm-operator">|</span> <span class="cm-variable">is_equal</span>)(<span class="cm-number">2</span>, <span class="cm-variable">b</span><span class="cm-operator">=</span><span class="cm-number">2</span>)    <span class="cm-comment"># True</span>
(<span class="cm-variable">is_less_than</span> <span class="cm-operator">|</span> <span class="cm-variable">is_equal</span>)(<span class="cm-variable">a</span><span class="cm-operator">=</span><span class="cm-number">3</span>, <span class="cm-variable">b</span><span class="cm-operator">=</span><span class="cm-number">2</span>)  <span class="cm-comment"># False</span>
</code></pre>
<p>Combinations of functions with incompatible signatures (e.g. <code>is_positive &amp; is_less_than</code>) will not be tested.</p>
<p>A decorated function should be callable by itself (without combining with other predicates) and behave like the original function:</p>
<pre><code class="language-python"><span class="cm-meta">@</span><span class="cm-meta">predicate</span>
<span class="cm-keyword">def</span> <span class="cm-def">is_less_than</span>(<span class="cm-variable">a</span>, <span class="cm-variable">b</span>):
    <span class="cm-keyword">return</span> <span class="cm-variable">a</span> <span class="cm-operator">&lt;</span> <span class="cm-variable">b</span>

<span class="cm-variable">is_less_than</span>(<span class="cm-number">1</span>, <span class="cm-number">2</span>)  <span class="cm-comment"># True</span>
<span class="cm-variable">is_less_than</span>(<span class="cm-number">2</span>, <span class="cm-number">2</span>)  <span class="cm-comment"># False</span>
<span class="cm-variable">is_less_than</span>(<span class="cm-number">3</span>, <span class="cm-number">2</span>)  <span class="cm-comment"># False</span>
</code></pre>
<p>Good luck!</p>
<p>This kata is heavily inspired by <a href="https://www.codewars.com/users/FArekkusu" data-turbolinks="false" target="_blank">FArekkusu</a>'s <a href="https://www.codewars.com/kata/5dc424122c135e001499d0e5" data-turbolinks="false" target="_blank">Readable Specification Pattern</a>, but should be a bit easier. You should try his kata as well!</p>

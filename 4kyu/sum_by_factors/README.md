<p>Given an array of positive or negative integers </p>
<p><code> I= [i<sub>1</sub>,..,i<sub>n</sub>]</code></p>
<p>you have to produce a sorted array P of the form </p>
<p><code>[ [p, sum of all i<sub>j</sub> of I for which p is a prime factor (p positive) of i<sub>j</sub>] ...]</code></p>
<p>P will be sorted by increasing order of the prime numbers.
The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.</p>
<h4 id="example">Example:</h4>
<pre style="display: none;"><code class="language-fortran"><span class="cm-variable">I</span> <span class="cm-operator">=</span> (<span class="cm-operator">/</span><span class="cm-number">12</span>, <span class="cm-number">15</span><span class="cm-operator">/</span>)<span class="cm-variable">;</span> <span class="cm-operator">//</span> <span class="cm-keyword">result</span> <span class="cm-operator">=</span> <span class="cm-string">"(2 12)(3 27)(5 15)"</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">I</span> <span class="cm-operator">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>] <span class="cm-comment"># result = [[2, 12], [3, 27], [5, 15]]</span>
</code></pre>
<pre style="display: none;"><code class="language-elixir"><span class="cm-tag">I</span> <span class="cm-operator">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>] <span class="cm-comment"># result = [{2, 12}, {3, 27}, {5, 15}]</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable">I</span> <span class="cm-operator">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>] # <span class="cm-variable">result</span> <span class="cm-operator">=</span> [(<span class="cm-number">2</span>, <span class="cm-number">12</span>), (<span class="cm-number">3</span>, <span class="cm-number">27</span>), (<span class="cm-number">5</span>, <span class="cm-number">15</span>)]
</code></pre>
<pre style="display: none;"><code class="language-swift"><span class="cm-variable">I</span> <span class="cm-operator">=</span> <span class="cm-punctuation">[</span><span class="cm-number">12</span><span class="cm-punctuation">,</span> <span class="cm-number">15</span><span class="cm-punctuation">]</span> # <span class="cm-variable">result</span> <span class="cm-operator">=</span> <span class="cm-punctuation">[</span><span class="cm-punctuation">(</span><span class="cm-number">2</span><span class="cm-punctuation">,</span> <span class="cm-number">12</span><span class="cm-punctuation">)</span><span class="cm-punctuation">,</span> <span class="cm-punctuation">(</span><span class="cm-number">3</span><span class="cm-punctuation">,</span> <span class="cm-number">27</span><span class="cm-punctuation">)</span><span class="cm-punctuation">,</span> <span class="cm-punctuation">(</span><span class="cm-number">5</span><span class="cm-punctuation">,</span> <span class="cm-number">15</span><span class="cm-punctuation">)</span><span class="cm-punctuation">]</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-tag">I</span> <span class="cm-operator">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>] <span class="cm-comment"># result = [[2, 12], [3, 27], [5, 15]]</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">I</span> <span class="cm-operator">=</span> {<span class="cm-number">12</span>, <span class="cm-number">15</span>}; <span class="cm-comment">// result = "(2 12)(3 27)(5 15)"</span>
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-variable">I</span> <span class="cm-operator">=</span> {<span class="cm-number">12</span>, <span class="cm-number">15</span>}; <span class="cm-comment">// result = "(2 12)(3 27)(5 15)"</span>
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-variable">I</span> <span class="cm-operator">=</span> {<span class="cm-number">12</span>, <span class="cm-number">15</span>}; <span class="cm-comment">// result = "(2 12)(3 27)(5 15)"</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">I</span> <span class="cm-operator">=</span> {<span class="cm-number">12</span>, <span class="cm-number">15</span>}; <span class="cm-comment">// result = "(2 12)(3 27)(5 15)"</span>
</code></pre>
<pre style="display: none;"><code class="language-clojure"><span class="cm-variable">I</span> <span class="cm-keyword">=</span> <span class="cm-bracket">[</span><span class="cm-number">12</span>, <span class="cm-number">15</span><span class="cm-bracket">]</span> <span class="cm-comment">; result = [[2, 12], [3, 27], [5, 15]]</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable-2">I</span> <span class="cm-keyword">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>] <span class="cm-comment">-- result = [(2,12),(3,27),(5,15)]</span>
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">I</span> <span class="cm-operator">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>]; <span class="cm-comment">//result = [[2, 12], [3, 27], [5, 15]]</span>
</code></pre>
<pre style="display: none;"><code class="language-coffeescript"><span class="cm-variable">I</span> <span class="cm-punctuation">=</span> <span class="cm-punctuation">[</span><span class="cm-number">12</span><span class="cm-punctuation">,</span> <span class="cm-number">15</span><span class="cm-punctuation">]</span> <span class="cm-comment"># result = [[2, 12], [3, 27], [5, 15]]</span>
</code></pre>
<pre style="display: none;"><code class="language-typescript"><span class="cm-variable">I</span> <span class="cm-operator">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>]; <span class="cm-comment">//result = [[2, 12], [3, 27], [5, 15]]</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">I</span> <span class="cm-operator">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>]; <span class="cm-comment">//result = [[2, 12], [3, 27], [5, 15]]</span>
</code></pre>
<pre style="display: none;"><code class="language-cobol">       I <span class="cm-builtin">=</span> [<span class="cm-number">12</span>, <span class="cm-number">15</span>]
      <span class="cm-comment">* result = [[2, 12], [3, 27], [5, 15]]</span>
</code></pre>
<p>[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>It can happen that a sum is 0 if some numbers are negative!</li>
</ul>
<p>Example: I = [15, 30, -45]
5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others. </p>
<ul>
<li>In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.</li>
</ul>

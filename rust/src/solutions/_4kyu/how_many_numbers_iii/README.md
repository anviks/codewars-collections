<p>We want to generate all the numbers of three digits where:</p>
<ul>
<li>the sum of their digits is equal to <code>10</code></li>
<li>their digits are in increasing order (the numbers may have two or more equal contiguous digits)</li>
</ul>
<p>The numbers that fulfill these constraints are: <code>[118, 127, 136, 145, 226, 235, 244, 334]</code>. There're <code>8</code> numbers in total with <code>118</code> being the lowest and <code>334</code> being the greatest.</p>
<hr>
<h2 id="task">Task</h2>
<p>Implement a function which receives two arguments:</p>
<ol>
<li>the sum of digits (<code>sum</code>)</li>
<li>the number of digits (<code>count</code>)</li>
</ol>
<p>This function should return three values:</p>
<ol>
<li>the total number of values which have <code>count</code> digits that add up to <code>sum</code> and are in increasing order</li>
<li>the lowest such value</li>
<li>the greatest such value</li>
</ol>
<p><strong>Note</strong>: if there're no values which satisfy these constaints, you should return an empty value (refer to the examples to see what exactly is expected).</p>
<h2 id="examples">Examples</h2>
<pre><code class="language-python"><span class="cm-variable">find_all</span>(<span class="cm-number">10</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-number">118</span>, <span class="cm-number">334</span>]
<span class="cm-variable">find_all</span>(<span class="cm-number">27</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">1</span>, <span class="cm-number">999</span>, <span class="cm-number">999</span>]
<span class="cm-variable">find_all</span>(<span class="cm-number">84</span>, <span class="cm-number">4</span>)  <span class="cm-operator">=&gt;</span>  []
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">find_all</span>(<span class="cm-number">10</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-number">118</span>, <span class="cm-number">334</span>]
<span class="cm-variable">find_all</span>(<span class="cm-number">27</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">1</span>, <span class="cm-number">999</span>, <span class="cm-number">999</span>]
<span class="cm-variable">find_all</span>(<span class="cm-number">84</span>, <span class="cm-number">4</span>)  <span class="cm-operator">=&gt;</span>  []
</code></pre>
<pre style="display: none;"><code class="language-crystal"><span class="cm-variable">find_all</span>(<span class="cm-number">10</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=</span><span class="cm-operator">&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-number">118</span>, <span class="cm-number">334</span>]
<span class="cm-variable">find_all</span>(<span class="cm-number">27</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=</span><span class="cm-operator">&gt;</span>  [<span class="cm-number">1</span>, <span class="cm-number">999</span>, <span class="cm-number">999</span>]
<span class="cm-variable">find_all</span>(<span class="cm-number">84</span>, <span class="cm-number">4</span>)  <span class="cm-operator">=</span><span class="cm-operator">&gt;</span>  []
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">findAll</span>(<span class="cm-number">10</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-string">"118"</span>, <span class="cm-string">"334"</span>]
<span class="cm-variable">findAll</span>(<span class="cm-number">27</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">1</span>, <span class="cm-string">"999"</span>, <span class="cm-string">"999"</span>]
<span class="cm-variable">findAll</span>(<span class="cm-number">84</span>, <span class="cm-number">4</span>)  <span class="cm-operator">=&gt;</span>  []
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">findAll</span> <span class="cm-number">10</span> <span class="cm-number">3</span>  <span class="cm-keyword">=&gt;</span>  ( <span class="cm-number">8</span>, <span class="cm-builtin">Just</span> <span class="cm-number">118</span>, <span class="cm-builtin">Just</span> <span class="cm-number">334</span> )
<span class="cm-variable">findAll</span> <span class="cm-number">27</span> <span class="cm-number">3</span>  <span class="cm-keyword">=&gt;</span>  ( <span class="cm-number">1</span>, <span class="cm-builtin">Just</span> <span class="cm-number">999</span>, <span class="cm-builtin">Just</span> <span class="cm-number">999</span> )
<span class="cm-variable">findAll</span> <span class="cm-number">84</span> <span class="cm-number">4</span>  <span class="cm-keyword">=&gt;</span>  ( <span class="cm-number">0</span>, <span class="cm-builtin">Nothing</span>, <span class="cm-builtin">Nothing</span> )
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-comment">// The output type is List&lt;Long&gt;</span>
<span class="cm-variable">HowManyNumbers</span>.<span class="cm-variable">findAll</span>(<span class="cm-number">10</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-number">118</span>, <span class="cm-number">334</span>]
<span class="cm-variable">HowManyNumbers</span>.<span class="cm-variable">findAll</span>(<span class="cm-number">27</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">1</span>, <span class="cm-number">999</span>, <span class="cm-number">999</span>]
<span class="cm-variable">HowManyNumbers</span>.<span class="cm-variable">findAll</span>(<span class="cm-number">84</span>, <span class="cm-number">4</span>)  <span class="cm-operator">=&gt;</span>  []
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-comment">// The output type is List&lt;long&gt;</span>
<span class="cm-variable">HowManyNumbers</span>.<span class="cm-variable">FindAll</span>(<span class="cm-number">10</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-number">118</span>, <span class="cm-number">334</span>]
<span class="cm-variable">HowManyNumbers</span>.<span class="cm-variable">FindAll</span>(<span class="cm-number">27</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  [<span class="cm-number">1</span>, <span class="cm-number">999</span>, <span class="cm-number">999</span>]
<span class="cm-variable">HowManyNumbers</span>.<span class="cm-variable">FindAll</span>(<span class="cm-number">84</span>, <span class="cm-number">4</span>)  <span class="cm-operator">=&gt;</span>  []
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-comment">// The output type is optional&lt;tuple&lt;uint32_t, uint64_t, uint64_t&gt;&gt;</span>
<span class="cm-variable">find_all</span>(<span class="cm-number">10</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  (<span class="cm-number">8</span>, <span class="cm-number">118</span>, <span class="cm-number">334</span>)
<span class="cm-variable">find_all</span>(<span class="cm-number">27</span>, <span class="cm-number">3</span>)  <span class="cm-operator">=&gt;</span>  (<span class="cm-number">1</span>, <span class="cm-number">999</span>, <span class="cm-number">999</span>)
<span class="cm-variable">find_all</span>(<span class="cm-number">84</span>, <span class="cm-number">4</span>)  <span class="cm-operator">=&gt;</span>  <span class="cm-variable">nullopt</span>
</code></pre>
<hr>
<p>Features of the random tests:</p>
<ul>
<li>Number of tests: <code>112</code></li>
<li>Sum of digits value between <code>20</code> and <code>65</code></li>
<li>Amount of digits between <code>2</code> and <code>17</code></li>
</ul>

<p>We want to create a function that will add numbers together when called in succession.</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">add</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>); <span class="cm-comment">// == 3</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">add</span>(<span class="cm-number">1</span>)<span class="cm-operator">.</span>(<span class="cm-number">2</span>); <span class="cm-comment"># equals 3</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">add</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>) <span class="cm-comment"># equals 3</span>
</code></pre>
<p>We also want to be able to continue to add numbers to our chain.</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">add</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">// == 6</span>
<span class="cm-variable">add</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>)(<span class="cm-number">4</span>); <span class="cm-comment">//  == 10</span>
<span class="cm-variable">add</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>)(<span class="cm-number">4</span>)(<span class="cm-number">5</span>); <span class="cm-comment">// == 15</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">add</span>(<span class="cm-number">1</span>)<span class="cm-operator">.</span>(<span class="cm-number">2</span>)<span class="cm-operator">.</span>(<span class="cm-number">3</span>); <span class="cm-comment"># 6</span>
<span class="cm-variable">add</span>(<span class="cm-number">1</span>)<span class="cm-operator">.</span>(<span class="cm-number">2</span>)<span class="cm-operator">.</span>(<span class="cm-number">3</span>)<span class="cm-operator">.</span>(<span class="cm-number">4</span>); <span class="cm-comment"># 10</span>
<span class="cm-variable">add</span>(<span class="cm-number">1</span>)<span class="cm-operator">.</span>(<span class="cm-number">2</span>)<span class="cm-operator">.</span>(<span class="cm-number">3</span>)<span class="cm-operator">.</span>(<span class="cm-number">4</span>)<span class="cm-operator">.</span>(<span class="cm-number">5</span>); <span class="cm-comment"># 15</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">add</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># 6</span>
<span class="cm-variable">add</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>)(<span class="cm-number">4</span>); <span class="cm-comment"># 10</span>
<span class="cm-variable">add</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>)(<span class="cm-number">4</span>)(<span class="cm-number">5</span>) <span class="cm-comment"># 15</span>
</code></pre>
<p>and so on.</p>
<p>A single call should be equal to the number passed in.</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">add</span>(<span class="cm-number">1</span>); <span class="cm-comment">// == 1</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">add</span>(<span class="cm-number">1</span>); <span class="cm-comment"># 1</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">add</span>(<span class="cm-number">1</span>) <span class="cm-comment"># 1</span>
</code></pre>
<p>We should be able to store the returned values and reuse them.</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">addTwo</span> <span class="cm-operator">=</span> <span class="cm-variable">add</span>(<span class="cm-number">2</span>);
<span class="cm-variable">addTwo</span>; <span class="cm-comment">// == 2</span>
<span class="cm-variable">addTwo</span> <span class="cm-operator">+</span> <span class="cm-number">5</span>; <span class="cm-comment">// == 7</span>
<span class="cm-variable">addTwo</span>(<span class="cm-number">3</span>); <span class="cm-comment">// == 5</span>
<span class="cm-variable">addTwo</span>(<span class="cm-number">3</span>)(<span class="cm-number">5</span>); <span class="cm-comment">// == 10</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">var</span> <span class="cm-variable">addTwo</span> <span class="cm-operator">=</span> <span class="cm-variable">add</span>(<span class="cm-number">2</span>);
<span class="cm-variable">addTwo</span>; <span class="cm-comment"># 2</span>
<span class="cm-variable">addTwo</span> <span class="cm-operator">+</span> <span class="cm-number">5</span>; <span class="cm-comment"># 7</span>
<span class="cm-variable">addTwo</span>(<span class="cm-number">3</span>); <span class="cm-comment"># 5</span>
<span class="cm-variable">addTwo</span>(<span class="cm-number">3</span>)<span class="cm-operator">.</span>(<span class="cm-number">5</span>); <span class="cm-comment"># 10</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">addTwo</span> <span class="cm-operator">=</span> <span class="cm-variable">add</span>(<span class="cm-number">2</span>)
<span class="cm-variable">addTwo</span> <span class="cm-comment"># 2</span>
<span class="cm-variable">addTwo</span> <span class="cm-operator">+</span> <span class="cm-number">5</span> <span class="cm-comment"># 7</span>
<span class="cm-variable">addTwo</span>(<span class="cm-number">3</span>) <span class="cm-comment"># 5</span>
<span class="cm-variable">addTwo</span>(<span class="cm-number">3</span>)(<span class="cm-number">5</span>) <span class="cm-comment"># 10</span>
</code></pre>
<p>We can assume any number being passed in will be valid whole number. </p>

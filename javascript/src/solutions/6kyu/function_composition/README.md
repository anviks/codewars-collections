<p>Javascript functions can be combined to form new functions. For example the functions addOne and multTwo can be combined to form a new function which first adds one and then multiplies by two, as follows:</p>
<pre><code class="language-javascript"><span class="cm-keyword">const</span> <span class="cm-def">addOne</span> <span class="cm-operator">=</span> (<span class="cm-def">a</span>) <span class="cm-operator">=&gt;</span> <span class="cm-variable-2">a</span> <span class="cm-operator">+</span> <span class="cm-number">1</span>
<span class="cm-keyword">const</span> <span class="cm-def">multTwo</span> <span class="cm-operator">=</span> (<span class="cm-def">b</span>) <span class="cm-operator">=&gt;</span> <span class="cm-variable-2">b</span> <span class="cm-operator">*</span> <span class="cm-number">2</span>
<span class="cm-keyword">const</span> <span class="cm-def">addOneMultTwo</span> <span class="cm-operator">=</span> (<span class="cm-def">c</span>) <span class="cm-operator">=&gt;</span> <span class="cm-variable">multTwo</span>(<span class="cm-variable">addOne</span>(<span class="cm-variable-2">c</span>))

<span class="cm-variable">addOneMultTwo</span>(<span class="cm-number">5</span>) <span class="cm-comment">// returns 12</span>
</code></pre>
<p>Combining functions like this is called function composition. Functional programming libraries in Javascript such as Ramda include a generic compose function which does the heavy lifting of combining functions for you. So you could implement addOneMultTwo as follows:</p>
<pre><code class="language-javascript"><span class="cm-keyword">const</span> <span class="cm-def">addOneMultTwo</span> <span class="cm-operator">=</span> <span class="cm-variable">compose</span>(<span class="cm-variable">multTwo</span>, <span class="cm-variable">addOne</span>)

<span class="cm-variable">addOneMultTwo</span>(<span class="cm-number">5</span>) <span class="cm-comment">// returns 12</span>
</code></pre>
<p>A simple implementation of compose, could work as follows:</p>
<pre><code class="language-javascript"><span class="cm-keyword">const</span> <span class="cm-def">compose</span> <span class="cm-operator">=</span> (<span class="cm-def">f</span>, <span class="cm-def">g</span>) <span class="cm-operator">=&gt;</span> (<span class="cm-def">a</span>) <span class="cm-operator">=&gt;</span> <span class="cm-variable-2">f</span>(<span class="cm-variable-2">g</span>(<span class="cm-variable-2">a</span>))
</code></pre>
<p>The arguments f and g are unary functions (i.e. functions which take one argument). The problem with this compose function is that it only composes two functions. Your task is to write a compose function which can compose any number of functions together.</p>

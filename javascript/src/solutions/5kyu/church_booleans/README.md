<p>There are <a href="https://www.codewars.com/kata/church-numbers-add-multiply-exponents" data-turbolinks="false" target="_blank">a</a> <a href="https://www.codewars.com/kata/church-numbers-1" data-turbolinks="false" target="_blank">few</a> <a href="https://www.codewars.com/kata/church-numbers-ii" data-turbolinks="false" target="_blank">Katas</a> about Church Numerals so let's talk about booleans.</p>
<p>In lambda calculus, the only primitive are lambdas. No numbers, no strings, and of course no booleans. Everything is reduced to anonymous functions.</p>
<p>Booleans are defined thusly (this definition is preloaded for you) :</p>
<pre><code class="language-javascript"><span class="cm-keyword">const</span> <span class="cm-def">True</span> <span class="cm-operator">=</span> <span class="cm-def">T</span> <span class="cm-operator">=&gt;</span> <span class="cm-def">F</span> <span class="cm-operator">=&gt;</span> <span class="cm-variable-2">T</span>;
<span class="cm-keyword">const</span> <span class="cm-def">False</span> <span class="cm-operator">=</span> <span class="cm-def">T</span> <span class="cm-operator">=&gt;</span> <span class="cm-def">F</span> <span class="cm-operator">=&gt;</span> <span class="cm-variable-2">F</span>;
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-keyword">type</span> <span class="cm-variable-2">Boolean</span> <span class="cm-keyword">=</span> <span class="cm-variable">forall</span> <span class="cm-variable">a</span><span class="cm-builtin">.</span> <span class="cm-variable">a</span> <span class="cm-keyword">-&gt;</span> <span class="cm-variable">a</span> <span class="cm-keyword">-&gt;</span> <span class="cm-variable">a</span> <span class="cm-comment">-- this requires RankNTypes</span>

<span class="cm-variable">false</span>,<span class="cm-variable">true</span> <span class="cm-keyword">::</span> <span class="cm-variable-2">Boolean</span>
<span class="cm-variable">false</span> <span class="cm-keyword">=</span> <span class="cm-keyword">\</span> <span class="cm-variable">t</span> <span class="cm-variable">f</span> <span class="cm-keyword">-&gt;</span> <span class="cm-variable">f</span>
<span class="cm-variable">true</span>  <span class="cm-keyword">=</span> <span class="cm-keyword">\</span> <span class="cm-variable">t</span> <span class="cm-variable">f</span> <span class="cm-keyword">-&gt;</span> <span class="cm-variable">t</span>
</code></pre>
<pre style="display: none;"><code class="language-python"><span class="cm-variable">true</span>  <span class="cm-operator">=</span> <span class="cm-keyword">lambda</span> <span class="cm-variable">t</span>: <span class="cm-keyword">lambda</span> <span class="cm-variable">f</span>: <span class="cm-variable">t</span>
<span class="cm-variable">false</span> <span class="cm-operator">=</span> <span class="cm-keyword">lambda</span> <span class="cm-variable">t</span>: <span class="cm-keyword">lambda</span> <span class="cm-variable">f</span>: <span class="cm-variable">f</span>
</code></pre>
<pre style="display: none;"><code class="language-lambdacalc"><span class="cm-variable-2">True</span>  <span class="cm-text">=</span> <span class="cm-keyword">\</span> <span class="cm-def">t</span> <span class="cm-def">f</span> <span class="cm-keyword">.</span> <span class="cm-text">t</span>
<span class="cm-variable-2">False</span> <span class="cm-text">=</span> <span class="cm-keyword">\</span> <span class="cm-def">t</span> <span class="cm-def">f</span> <span class="cm-keyword">.</span> <span class="cm-text">f</span>
</code></pre>
<p>Your task will be to implement basic operators on booleans (using only lambdas and function application) : <code>Not</code>, <code>And</code>, <code>Or</code> and <code>Xor</code>.</p>
<p>To help, the function <code>unchurch</code> comes preloaded, and returns the native boolean given a church boolean :</p>
<pre><code class="language-javascript"><span class="cm-variable">unchurch</span>(<span class="cm-variable">True</span>); <span class="cm-comment">//true;</span>
</code></pre>
<p><i>Note: You should not use the following:</i></p><i>
</i><ul><i>
<li>numbers</li>
<li>strings</li>
<li>booleans</li>
<li>boolean operators</li>
<li>objects (curly brackets) or arrays (square brackets)</li>
<li>regexp</li>
</i><li><i>"new"</i></li>
</ul>

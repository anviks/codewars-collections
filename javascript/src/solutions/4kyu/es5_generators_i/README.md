<p>This is the first part of three (<a href="http://www.codewars.com/kata/es5-generators-ii" data-turbolinks="false" target="_blank">part2</a>, <a href="http://www.codewars.com/kata/es5-generators-iii" data-turbolinks="false" target="_blank">part3</a>).</p>
<p>Generators and Iterators are ES6 features that allow things like this:</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span><span class="cm-keyword">*</span> <span class="cm-def">fibonacci</span>() {
  <span class="cm-keyword">let</span> [<span class="cm-def">prev</span>, <span class="cm-def">curr</span>] <span class="cm-operator">=</span> [<span class="cm-number">0</span>, <span class="cm-number">1</span>];
  <span class="cm-keyword">for</span> (;;) {
    [<span class="cm-variable-2">prev</span>, <span class="cm-variable-2">curr</span>] <span class="cm-operator">=</span> [<span class="cm-variable-2">curr</span>, <span class="cm-variable-2">prev</span> <span class="cm-operator">+</span> <span class="cm-variable-2">curr</span>];
    <span class="cm-keyword">yield</span> <span class="cm-variable-2">curr</span>;
  }
}
</code></pre>
<p>Using them in this way, we can do amazing things:</p>
<pre><code class="language-javascript"><span class="cm-keyword">let</span> <span class="cm-def">seq</span> <span class="cm-operator">=</span> <span class="cm-variable">fibonacci</span>();
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">1</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">2</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">3</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">5</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">8</span>
</code></pre>
<p>The goal of this kata is to implement pseudo-generators with ES5.</p>
<p>The first thing to do is to implement the generator function:</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">generator</span>(<span class="cm-def">sequencer</span>) {
   <span class="cm-meta">...</span>
}
</code></pre>
<p><code>generator(sequencer[, arg1, arg2, ...])</code> receives a <em>sequencer</em> function to generate the sequence and returns an object with a <code>next()</code> method. When the <code>next()</code> method is invoked, the next value is generated. The method could receive as well optional arguments to be passed to the <em>sequencer</em> function.</p>
<p>This is an example of a dummy sequencer:</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">dummySeq</span>() {
  <span class="cm-keyword">return</span> <span class="cm-keyword">function</span>() {
    <span class="cm-keyword">return</span> <span class="cm-string">"dummy"</span>;
  };
}
</code></pre>
<p>To test <code>generator()</code>, you could use <code>dummySeq()</code> in this way:</p>
<pre><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">seq</span> <span class="cm-operator">=</span> <span class="cm-variable">generator</span>(<span class="cm-variable">dummySeq</span>);
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-string">'dummy'</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-string">'dummy'</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-string">'dummy'</span>
<span class="cm-meta">...</span>.
</code></pre>
<p>When you're done, you should implement the following generators (I think the functions are self explanatory):</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">factorialSeq</span>() {<span class="cm-meta">...</span>} <span class="cm-comment">// 1, 1, 2, 6, 24, ...</span>
<span class="cm-keyword">function</span> <span class="cm-def">fibonacciSeq</span>() {<span class="cm-meta">...</span>} <span class="cm-comment">// 1, 1, 2, 3, 5, 8, 13, ...</span>
<span class="cm-keyword">function</span> <span class="cm-def">rangeSeq</span>(<span class="cm-def">start</span>, <span class="cm-def">step</span>) {<span class="cm-meta">...</span>} <span class="cm-comment">// rangeSeq(1, 2)  -&gt; 1, 3, 5, 7, ...</span>
<span class="cm-keyword">function</span> <span class="cm-def">primeSeq</span>() {<span class="cm-meta">...</span>} <span class="cm-comment">// 2, 3, 5, 7, 11, 13, ...</span>
<span class="cm-keyword">function</span> <span class="cm-def">partialSumSeq</span>(<span class="cm-number">1</span>, <span class="cm-number">3</span>, <span class="cm-number">7</span>, <span class="cm-number">2</span>, <span class="cm-number">0</span>) {<span class="cm-meta">...</span>} <span class="cm-comment">// 1, 4, 11, 13, 13, end</span>
</code></pre>
<p>You can use any of them in the same way:</p>
<pre><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">seq</span> <span class="cm-operator">=</span> <span class="cm-variable">generator</span>(<span class="cm-variable">factorialSeq</span>);
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">1</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">1</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">2</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">6</span>
<span class="cm-variable">seq</span>.<span class="cm-property">next</span>() <span class="cm-operator">==</span><span class="cm-operator">&gt;</span> <span class="cm-number">24</span>
<span class="cm-meta">...</span>
</code></pre>
<p>There are some sequences which are infinite and others are not. For example:</p>
<ul>
<li>primeSeq: Is infinite</li>
<li>partialSumSeq: Is limited to the passed values.</li>
</ul>
<p>When the sequence is done (in finite sequences), if you call <code>seq.next()</code> again, it should produce an error.</p>
<p>Good luck!</p>

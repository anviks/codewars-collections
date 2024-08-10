<p>Function composition is a powerful technique. For example:</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">sum</span>(<span class="cm-def">x</span>, <span class="cm-def">y</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable-2">x</span> <span class="cm-operator">+</span> <span class="cm-variable-2">y</span>;
}

<span class="cm-keyword">function</span> <span class="cm-def">double</span>(<span class="cm-def">x</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable">sum</span>(<span class="cm-variable-2">x</span>, <span class="cm-variable-2">x</span>);
}

<span class="cm-keyword">function</span> <span class="cm-def">minus</span> (<span class="cm-def">x</span>, <span class="cm-def">y</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable-2">x</span> <span class="cm-operator">-</span> <span class="cm-variable-2">y</span>;
}

<span class="cm-keyword">function</span> <span class="cm-def">addOne</span>(<span class="cm-def">x</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable">sum</span>(<span class="cm-variable-2">x</span>, <span class="cm-number">1</span>);
}

<span class="cm-variable">double</span>(<span class="cm-variable">sum</span>(<span class="cm-number">2</span>, <span class="cm-number">3</span>)); <span class="cm-comment">// 10</span>
</code></pre>
<p>But in complex expressions, composition may be difficult to understand. For example:</p>
<pre><code class="language-javascript"><span class="cm-variable">double</span>(<span class="cm-variable">double</span>(<span class="cm-variable">addOne</span>(<span class="cm-variable">sum</span>(<span class="cm-number">7</span>, <span class="cm-variable">minus</span>(<span class="cm-variable">sum</span>(<span class="cm-number">5</span>, <span class="cm-variable">sum</span>(<span class="cm-number">4</span>, <span class="cm-number">5</span>)), <span class="cm-number">4</span>))))); <span class="cm-comment">// 72</span>
</code></pre>
<p>In this kata, we will implement a function that allows us to perform this by applying a fluid style:</p>
<pre><code class="language-javascript"><span class="cm-variable">c</span>.<span class="cm-property">sum</span>(<span class="cm-number">4</span>, <span class="cm-number">5</span>).<span class="cm-property">sum</span>(<span class="cm-number">5</span>).<span class="cm-property">minus</span>(<span class="cm-number">4</span>).<span class="cm-property">sum</span>(<span class="cm-number">7</span>).<span class="cm-property">addOne</span>().<span class="cm-property">double</span>().<span class="cm-property">double</span>().<span class="cm-property">execute</span>(); <span class="cm-comment">// 72</span>
</code></pre>
<p>Your job is implement the <code>chain</code> function:</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">chain</span>(<span class="cm-def">fns</span>) {
}

<span class="cm-keyword">const</span> <span class="cm-def">c</span> <span class="cm-operator">=</span> <span class="cm-variable">chain</span>({<span class="cm-property">sum</span>, <span class="cm-property">minus</span>, <span class="cm-property">double</span>, <span class="cm-property">addOne</span>});
</code></pre>
<p>As you can see, this function receives the methods to be chained and returns an object that allows you to call the chained methods. The result is obtained by calling the <code>execute</code> method.</p>
<p>Chained functions receive an arbitrary number of arguments. The first function in the chain receives all its arguments. In the other functions, the first argument is the result of the previous function and then it only receives the remainder arguments (second, third, etc.). The tests always pass the appropriate arguments and you do not have to worry about checking this.</p>
<p>Note that the chain can be reused (the internal state is not stored):</p>
<pre><code class="language-javascript"><span class="cm-variable">c</span>.<span class="cm-property">sum</span>(<span class="cm-number">3</span>, <span class="cm-number">4</span>).<span class="cm-property">execute</span>(); <span class="cm-comment">//7</span>
<span class="cm-variable">c</span>.<span class="cm-property">sum</span>(<span class="cm-number">1</span>, <span class="cm-number">2</span>).<span class="cm-property">execute</span>(); <span class="cm-comment">//3</span>
</code></pre>
<p>Other examples:</p>
<pre><code class="language-javascript"><span class="cm-keyword">const</span> <span class="cm-def">c1</span> <span class="cm-operator">=</span> <span class="cm-variable">c</span>.<span class="cm-property">sum</span>(<span class="cm-number">1</span>, <span class="cm-number">2</span>);
<span class="cm-variable">c1</span>.<span class="cm-property">execute</span>(); <span class="cm-comment">// == fns.sum(1, 2) == 3</span>
<span class="cm-variable">c1</span>.<span class="cm-property">double</span>().<span class="cm-property">execute</span>(); <span class="cm-comment">// == fns.double(fns.sum(1, 2)) == 6</span>
<span class="cm-variable">c1</span>.<span class="cm-property">addOne</span>().<span class="cm-property">execute</span>(); <span class="cm-comment">// == fns.addOne(fns.sum(1, 2)) == 4</span>
<span class="cm-variable">c1</span>.<span class="cm-property">execute</span>(); <span class="cm-comment">// == fns.sum(1, 2) == 3</span>

<span class="cm-keyword">const</span> <span class="cm-def">c2</span> <span class="cm-operator">=</span> <span class="cm-variable">c1</span>.<span class="cm-property">sum</span>(<span class="cm-number">5</span>);
<span class="cm-variable">c2</span>.<span class="cm-property">addOne</span>().<span class="cm-property">execute</span>(); <span class="cm-comment">// == fns.addOne(fns.sum(fns.sum(1, 2) 5)) == 9</span>
<span class="cm-variable">c2</span>.<span class="cm-property">sum</span>(<span class="cm-number">3</span>).<span class="cm-property">execute</span>(); <span class="cm-comment">// == fns.sum(c1.sum(fns.sum(1, 2), 5), 3) == 11</span>
<span class="cm-variable">c2</span>.<span class="cm-property">execute</span>(); <span class="cm-comment">// == fns.sum(fns.sum(1, 2), 5) == 8</span>

<span class="cm-variable">c1</span>.<span class="cm-property">execute</span>(); <span class="cm-comment">// == fns.sum(1, 2) == 3</span>
</code></pre>

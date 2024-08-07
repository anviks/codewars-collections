<p><a href="http://www.2ality.com/2011/09/currying-vs-part-eval.html" data-turbolinks="false" target="_blank">Currying and partial application</a> are two ways of transforming a function into another function with a generally smaller arity. While they are often confused with each other, they work differently. The goal is to learn to differentiate them.</p>
<h2 id="currying">Currying</h2>
<blockquote>
<p>Is the technique of transforming a function that takes multiple arguments in such a way that it can be called as a chain of functions each with a single argument.</p>
</blockquote>
<p>Currying takes a function:</p>
<pre><code>f: X × Y → R
</code></pre>
<p>and turns it into a function:</p>
<pre><code>f': X → (Y → R)
</code></pre>
<p>Instead of calling <code>f</code> with two arguments, we invoke <code>f'</code> with the first argument. The result is a function that we then call with the second argument to produce the result. Thus, if the uncurried <code>f</code> is invoked as:</p>
<pre><code>f(3, 5)
</code></pre>
<p>then the curried <code>f'</code> is invoked as:</p>
<p><code>f'(3)(5)</code></p>
<h3 id="example">Example</h3>
<p>Given this function:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">add</span>(<span class="cm-def">x</span>, <span class="cm-def">y</span>, <span class="cm-def">z</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable-2">x</span> <span class="cm-operator">+</span> <span class="cm-variable-2">y</span> <span class="cm-operator">+</span> <span class="cm-variable-2">z</span>;
}
</code></pre>
<pre><code class="language-python"><span class="cm-keyword">def</span> <span class="cm-def">add</span>(<span class="cm-variable">x</span>, <span class="cm-variable">y</span>, <span class="cm-variable">z</span>):
  <span class="cm-keyword">return</span> <span class="cm-variable">x</span> <span class="cm-operator">+</span> <span class="cm-variable">y</span> <span class="cm-operator">+</span> <span class="cm-variable">z</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-keyword">function</span> <span class="cm-def">add</span>(<span class="cm-variable-2">$x</span>, <span class="cm-variable-2">$y</span>, <span class="cm-variable-2">$z</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable-2">$x</span> <span class="cm-operator">+</span> <span class="cm-variable-2">$y</span> <span class="cm-operator">+</span> <span class="cm-variable-2">$z</span>;
}
</code></pre>
<p>We can call in a normal way:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">add</span>(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">add</span>(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt; 6</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">add</span>(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<p>But we can create a curried version of <code>add(a, b, c)</code>function:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">curriedAdd</span>(<span class="cm-def">a</span>) {
  <span class="cm-keyword">return</span> <span class="cm-keyword">function</span>(<span class="cm-def">b</span>) {
    <span class="cm-keyword">return</span> <span class="cm-keyword">function</span> (<span class="cm-def">c</span>) {
      <span class="cm-keyword">return</span> <span class="cm-variable">add</span>(<span class="cm-variable-2">a</span>, <span class="cm-variable-2">b</span>, <span class="cm-variable-2">c</span>);
    };
  };
}

<span class="cm-variable">curriedAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">curriedAdd</span> <span class="cm-operator">=</span> <span class="cm-keyword">lambda</span> <span class="cm-variable">a</span>: (<span class="cm-keyword">lambda</span> <span class="cm-variable">b</span>: (<span class="cm-keyword">lambda</span> <span class="cm-variable">c</span>: <span class="cm-variable">add</span>(<span class="cm-variable">a</span>,<span class="cm-variable">b</span>,<span class="cm-variable">c</span>)))
<span class="cm-variable">curriedAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># =&gt; 6</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-keyword">function</span> <span class="cm-def">curriedAdd</span>(<span class="cm-variable-2">$a</span>) {
  <span class="cm-keyword">return</span> <span class="cm-keyword">function</span>(<span class="cm-variable-2">$b</span>) <span class="cm-keyword">use</span> (<span class="cm-variable-2">$a</span>) {
    <span class="cm-keyword">return</span> <span class="cm-keyword">function</span>(<span class="cm-variable-2">$c</span>) <span class="cm-keyword">use</span> (<span class="cm-variable-2">$a</span>, <span class="cm-variable-2">$b</span>) {
      <span class="cm-keyword">return</span> <span class="cm-variable">add</span>(<span class="cm-variable-2">$a</span>, <span class="cm-variable-2">$b</span>, <span class="cm-variable-2">$c</span>);
    };
  };
}

<span class="cm-variable">curriedAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<h2 id="partial-application">Partial application</h2>
<blockquote>
<p>Is the process of fixing a number of arguments to a function, producing another function of smaller arity.</p>
</blockquote>
<p>Partial application takes a function:</p>
<pre><code>f: X × Y → R
</code></pre>
<p>and a fixed value <code>x</code> for the first argument to produce a new function</p>
<pre><code>f': Y → R
</code></pre>
<p><code>f'</code> does the same as <code>f</code>, but only has to fill in the second parameter which is why its arity is one less than the arity of <code>f</code>. One says that the first argument is bound to <code>x</code>.</p>
<h3 id="example-1">Example</h3>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">partialAdd</span>(<span class="cm-def">a</span>) {
  <span class="cm-keyword">return</span> <span class="cm-keyword">function</span>(<span class="cm-def">b</span>, <span class="cm-def">c</span>) {
    <span class="cm-keyword">return</span> <span class="cm-variable">add</span>(<span class="cm-variable-2">a</span>, <span class="cm-variable-2">b</span>, <span class="cm-variable-2">c</span>);
  };
}

<span class="cm-variable">partialAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">partialAdd</span> <span class="cm-operator">=</span> <span class="cm-keyword">lambda</span> <span class="cm-variable">a</span>: (<span class="cm-keyword">lambda</span> <span class="cm-operator">*</span><span class="cm-variable">args</span>: <span class="cm-variable">add</span>(<span class="cm-variable">a</span>,<span class="cm-operator">*</span><span class="cm-variable">args</span>))
<span class="cm-variable">partialAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt; 6</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-keyword">function</span> <span class="cm-def">partialAdd</span>(<span class="cm-variable-2">$a</span>) {
  <span class="cm-keyword">return</span> <span class="cm-keyword">function</span>(<span class="cm-variable-2">$b</span>, <span class="cm-variable-2">$c</span>) <span class="cm-keyword">use</span> (<span class="cm-variable-2">$a</span>) {
    <span class="cm-keyword">return</span> <span class="cm-variable">add</span>(<span class="cm-variable-2">$a</span>, <span class="cm-variable-2">$b</span>, <span class="cm-variable-2">$c</span>);
  };
}

<span class="cm-variable">partialAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<hr>
<p>Your work is to implement a generic <code>curryPartial()</code> function allows either currying or partial application.</p>
<p>For example:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">curriedAdd</span> <span class="cm-operator">=</span> <span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>);
<span class="cm-variable">curriedAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>

<span class="cm-keyword">var</span> <span class="cm-def">partialAdd</span> <span class="cm-operator">=</span> <span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>);
<span class="cm-variable">partialAdd</span>(<span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">curriedAdd</span> <span class="cm-operator">=</span> <span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)
<span class="cm-variable">curriedAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># =&gt; 6</span>

<span class="cm-variable">partialAdd</span> <span class="cm-operator">=</span> <span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)
<span class="cm-variable">partialAdd</span>(<span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt; 6</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable-2">$add</span> <span class="cm-operator">=</span> <span class="cm-keyword">function</span> (<span class="cm-variable-2">$a</span>, <span class="cm-variable-2">$b</span>, <span class="cm-variable-2">$c</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable-2">$a</span> <span class="cm-operator">+</span> <span class="cm-variable-2">$b</span> <span class="cm-operator">+</span> <span class="cm-variable-2">$c</span>;
};
<span class="cm-variable-2">$curriedAdd</span> <span class="cm-operator">=</span> <span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>);
<span class="cm-variable-2">$curriedAdd</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>

<span class="cm-keyword">function</span> <span class="cm-def">add</span>(<span class="cm-variable-2">$a</span>, <span class="cm-variable-2">$b</span>, <span class="cm-variable-2">$c</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable-2">$a</span> <span class="cm-operator">+</span> <span class="cm-variable-2">$b</span> <span class="cm-operator">+</span> <span class="cm-variable-2">$c</span>;
}
<span class="cm-variable-2">$partialAdd</span> <span class="cm-operator">=</span> <span class="cm-variable">curryPartial</span>(<span class="cm-string">'add'</span>, <span class="cm-number">1</span>);
<span class="cm-variable-2">$partialAdd</span>(<span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<p>We want the function be very flexible.</p>
<p>All these examples should produce the same result:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)(<span class="cm-number">1</span>, <span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)()(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)()(<span class="cm-number">1</span>)()()(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>

<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)()(<span class="cm-number">1</span>)()()(<span class="cm-number">2</span>)(<span class="cm-number">3</span>, <span class="cm-number">4</span>, <span class="cm-number">5</span>, <span class="cm-number">6</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>, <span class="cm-number">4</span>, <span class="cm-number">5</span>); <span class="cm-comment">//6</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)(<span class="cm-number">1</span>, <span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)()(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)()(<span class="cm-number">1</span>)()()(<span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6 </span>

<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>)()(<span class="cm-number">1</span>)()()(<span class="cm-number">2</span>)(<span class="cm-number">3</span>, <span class="cm-number">4</span>, <span class="cm-number">5</span>, <span class="cm-number">6</span>) <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>, <span class="cm-number">4</span>, <span class="cm-number">5</span>) <span class="cm-comment"># =&gt;6 </span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>)(<span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>)(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>)(<span class="cm-number">1</span>, <span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>)()(<span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>)()(<span class="cm-number">1</span>)()()(<span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6 </span>

<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>)()(<span class="cm-number">1</span>)()()(<span class="cm-number">2</span>)(<span class="cm-number">3</span>, <span class="cm-number">4</span>, <span class="cm-number">5</span>, <span class="cm-number">6</span>); <span class="cm-comment"># =&gt;6 </span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>, <span class="cm-number">3</span>, <span class="cm-number">4</span>, <span class="cm-number">5</span>); <span class="cm-comment"># =&gt;6 </span>
</code></pre>
<p>And also all of these:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>), <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>), <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>), <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)), <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment">//6</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>), <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>), <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>)(<span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>), <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">add</span>, <span class="cm-number">1</span>)), <span class="cm-number">2</span>, <span class="cm-number">3</span>) <span class="cm-comment"># =&gt;6</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>), <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>), <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>), <span class="cm-number">2</span>)(<span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>)(<span class="cm-number">2</span>), <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6</span>
<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable">curryPartial</span>(<span class="cm-variable-2">$add</span>, <span class="cm-number">1</span>)), <span class="cm-number">2</span>, <span class="cm-number">3</span>); <span class="cm-comment"># =&gt;6</span>
</code></pre>

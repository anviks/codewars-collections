<h2 id="caveat">Caveat</h2>
<p>Currying is not exactly what is described below. Stretch your mind!</p>
<h2 id="task">Task</h2>
<p>Create a function which accepts a single argument of another function and returns a "curried" version of that function.</p>
<p>Currying is a technique named (as is the language Haskell) after the mathematician Haskell Curry which allows a function's arguments to be fed to it through separate instances of running that function. For example, take the following function:</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">adder</span>(<span class="cm-def">arg1</span>, <span class="cm-def">arg2</span>) {
  <span class="cm-keyword">return</span> <span class="cm-variable-2">arg1</span> <span class="cm-operator">+</span> <span class="cm-variable-2">arg2</span>;
}
</code></pre>
<p>This function would normally be invoked like so:</p>
<pre><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">example</span> <span class="cm-operator">=</span> <span class="cm-variable">adder</span>(<span class="cm-number">1</span>,<span class="cm-number">3</span>); <span class="cm-comment">// 4</span>
</code></pre>
<p>A "curried" version of this function could be executed in either of the following ways</p>
<pre><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">example</span> <span class="cm-operator">=</span> <span class="cm-variable">adder</span>(<span class="cm-number">1</span>)(<span class="cm-number">4</span>); <span class="cm-comment">// 5</span>
</code></pre>
<p>Or:</p>
<pre><code class="language-javascript"><span class="cm-variable">adder</span>(<span class="cm-number">5</span>)
<span class="cm-keyword">var</span> <span class="cm-def">example2</span> <span class="cm-operator">=</span> <span class="cm-variable">adder</span>(<span class="cm-number">6</span>); <span class="cm-comment">// 11</span>
</code></pre>
<p>Your goal in this Kata is to produce a higher-order function that accepts another function as an argument and returns a "curried" version of that function.</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">adder</span> () {
  <span class="cm-keyword">return</span> [].<span class="cm-property">slice</span>.<span class="cm-property">call</span>(<span class="cm-variable-2">arguments</span>).<span class="cm-property">reduce</span>(<span class="cm-keyword">function</span>(<span class="cm-def">a</span>,<span class="cm-def">b</span>){
    <span class="cm-keyword">return</span> <span class="cm-variable-2">a</span> <span class="cm-operator">+</span> <span class="cm-variable-2">b</span>
  },<span class="cm-number">0</span>);
}

<span class="cm-keyword">var</span> <span class="cm-def">curryAdder</span> <span class="cm-operator">=</span> <span class="cm-variable">CurryIt</span>(<span class="cm-variable">adder</span>);
</code></pre>
<p>This "curried" version of the original function should expand its arguments when invoked with arguments. It should allow multiple arguments to be passed into each invocation.</p>
<p>It should execute the original function and then restore that function's original argument-less state when invoked without arguments.</p>
<p>See example here, assuming <code>curryAdder</code> from above has been created already:</p>
<pre><code class="language-javascript"><span class="cm-variable">curryAdder</span>(<span class="cm-number">1</span>);
<span class="cm-variable">curryAdder</span>(<span class="cm-number">1</span>,<span class="cm-number">2</span>,<span class="cm-number">3</span>);
<span class="cm-variable">curryAdder</span>(<span class="cm-number">2</span>)(<span class="cm-number">2</span>,<span class="cm-number">5</span>);
<span class="cm-keyword">var</span> <span class="cm-def">example</span> <span class="cm-operator">=</span> <span class="cm-variable">curryAdder</span>(); <span class="cm-comment">// 16</span>
<span class="cm-variable">curryAdder</span>(<span class="cm-number">1</span>)(<span class="cm-number">2</span>);
<span class="cm-keyword">var</span> <span class="cm-def">example2</span> <span class="cm-operator">=</span> <span class="cm-variable">curryAdder</span>(); <span class="cm-comment">// 3</span>
</code></pre>
<p>For fun, let's make sure this works with native global functions and methods too! (will involve some context)</p>
<pre><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">curryEval</span> <span class="cm-operator">=</span> <span class="cm-variable">CurryIt</span>(<span class="cm-variable">eval</span>);
<span class="cm-variable">curryEval</span>(<span class="cm-string">"var y = function(){return true}"</span>);
<span class="cm-variable">curryEval</span>();
<span class="cm-variable">y</span>(); <span class="cm-comment">// =&gt; true</span>
</code></pre>
<p>Context is to be fixed the first time the "curried" function is called after creation.</p>
<p>Happy coding! :)</p>

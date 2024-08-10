<p>Your task is to write a higher order function for chaining together
a list of unary functions. In other words, it should return a function
that does a left fold on the given functions.</p>
<pre><code class="language-python"><span class="cm-variable">chained</span>([<span class="cm-variable">a</span>,<span class="cm-variable">b</span>,<span class="cm-variable">c</span>,<span class="cm-variable">d</span>])(<span class="cm-builtin">input</span>)
</code></pre>
<p>Should yield the same result as</p>
<pre><code class="language-python"><span class="cm-variable">d</span>(<span class="cm-variable">c</span>(<span class="cm-variable">b</span>(<span class="cm-variable">a</span>(<span class="cm-builtin">input</span>))))
</code></pre>

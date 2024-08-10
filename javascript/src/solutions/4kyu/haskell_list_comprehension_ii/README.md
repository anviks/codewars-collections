<p>This is the second part. You should do the [previous part][previous] first.
 [previous]: <a href="http://www.codewars.com/kata/53c8b29750fe70e4a2000610" data-turbolinks="false" target="_blank">http://www.codewars.com/kata/53c8b29750fe70e4a2000610</a></p>
<p>Haskell List Comprehension can generate lists by applying filters and transformations.</p>
<p>In this kata we are going to do the same in JavaScript.</p>
<p>To do this, copy the solution you gave in the previous kata and modify it so that the <code>options</code> object can accept two parameters more:</p>
<ul>
<li><code>filters[]</code>: Array of functions. Each function receives an integer and returns a boolean. Only values that pass the filter, belong to the list.</li>
<li><code>transform(value)</code>: Is a function that takes a value and returns it muted.</li>
</ul>
<p>For example:</p>
<pre><code class="language-javascript"><span class="cm-comment">//Filter</span>
<span class="cm-keyword">function</span> <span class="cm-def">isPrime</span>(<span class="cm-def">num</span>) {
  <span class="cm-keyword">var</span> <span class="cm-def">result</span> <span class="cm-operator">=</span> <span class="cm-atom">true</span>;
  <span class="cm-keyword">if</span> (<span class="cm-variable-2">num</span> <span class="cm-operator">!==</span> <span class="cm-number">2</span>) {
    <span class="cm-keyword">if</span> (<span class="cm-variable-2">num</span> <span class="cm-operator">%</span> <span class="cm-number">2</span> <span class="cm-operator">===</span> <span class="cm-number">0</span>) {
      <span class="cm-variable-2">result</span> <span class="cm-operator">=</span> <span class="cm-atom">false</span>;
    } <span class="cm-keyword">else</span> {
      <span class="cm-keyword">for</span> (<span class="cm-keyword">var</span> <span class="cm-def">x</span><span class="cm-operator">=</span><span class="cm-number">3</span>; <span class="cm-variable-2">result</span> <span class="cm-operator">&amp;&amp;</span> <span class="cm-variable-2">x</span><span class="cm-operator">&lt;=</span><span class="cm-variable">Math</span>.<span class="cm-property">sqrt</span>(<span class="cm-variable-2">num</span>); <span class="cm-variable-2">x</span><span class="cm-operator">+=</span><span class="cm-number">2</span>) {
        <span class="cm-keyword">if</span> (<span class="cm-variable-2">num</span> <span class="cm-operator">%</span> <span class="cm-variable-2">x</span> <span class="cm-operator">===</span> <span class="cm-number">0</span>) {
          <span class="cm-variable-2">result</span> <span class="cm-operator">=</span> <span class="cm-atom">false</span>;
        }
      }
    }
  }  
  <span class="cm-keyword">return</span> <span class="cm-variable-2">result</span>;
}

<span class="cm-comment">//Transform</span>
<span class="cm-keyword">function</span> <span class="cm-def">arrayWrapper</span>(<span class="cm-def">num</span>) {
  <span class="cm-keyword">return</span> [<span class="cm-variable-2">num</span>];
}

<span class="cm-variable">ArrayComprehension</span>({
  <span class="cm-property">generator</span>: <span class="cm-string">"1..50"</span>,
  <span class="cm-property">filters</span>: [<span class="cm-variable">isPrime</span>],
  <span class="cm-property">transform</span>: <span class="cm-variable">arrayWrapper</span>
}); <span class="cm-comment">// returns [[2], [3], [5], [7], [11], [13], [17], [19], [23], [29], [31], [37], [41], [43], [47]]</span>
</code></pre>
<p>Cool, is'nt it?</p>

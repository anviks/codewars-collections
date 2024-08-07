<h1 id="write-number-in-expanded-form">Write Number in Expanded Form</h1>
<p>You will be given a number and you will need to return it as a string in <a href="https://www.mathsisfun.com/definitions/expanded-notation.html" data-turbolinks="false" target="_blank">Expanded Form</a>. For example:</p>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">expandedForm</span> <span class="cm-number">12</span>    <span class="cm-comment">-- Should return '10 + 2'</span>
<span class="cm-variable">expandedForm</span> <span class="cm-number">42</span>    <span class="cm-comment">-- Should return '40 + 2'</span>
<span class="cm-variable">expandedForm</span> <span class="cm-number">70304</span> <span class="cm-comment">-- Should return '70000 + 300 + 4'</span>
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">expandedForm</span>(<span class="cm-number">12</span>); <span class="cm-comment">// Should return '10 + 2'</span>
<span class="cm-variable">expandedForm</span>(<span class="cm-number">42</span>); <span class="cm-comment">// Should return '40 + 2'</span>
<span class="cm-variable">expandedForm</span>(<span class="cm-number">70304</span>); <span class="cm-comment">// Should return '70000 + 300 + 4'</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">expanded_form</span>(<span class="cm-number">12</span>) <span class="cm-comment"># Should return '10 + 2'</span>
<span class="cm-variable">expanded_form</span>(<span class="cm-number">42</span>) <span class="cm-comment"># Should return '40 + 2'</span>
<span class="cm-variable">expanded_form</span>(<span class="cm-number">70304</span>) <span class="cm-comment"># Should return '70000 + 300 + 4'</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">expanded_form</span>(<span class="cm-number">12</span>); <span class="cm-comment">// Should return "10 + 2"</span>
<span class="cm-variable">expanded_form</span>(<span class="cm-number">42</span>); <span class="cm-comment">// Should return "40 + 2"</span>
<span class="cm-variable">expanded_form</span>(<span class="cm-number">70304</span>); <span class="cm-comment">// Should return "70000 + 300 + 4"</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">expanded_form</span>(<span class="cm-number">12</span>); <span class="cm-comment"># Should return '10 + 2'</span>
<span class="cm-variable">expanded_form</span>(<span class="cm-number">42</span>); <span class="cm-comment"># Should return '40 + 2'</span>
<span class="cm-variable">expanded_form</span>(<span class="cm-number">70304</span>); <span class="cm-comment"># Should return '70000 + 300 + 4'</span>
</code></pre>
<pre style="display: none;"><code class="language-coffeescript"><span class="cm-variable">expandedForm</span><span class="cm-punctuation">(</span><span class="cm-number">12</span><span class="cm-punctuation">)</span><span class="cm-punctuation">;</span> <span class="cm-comment"># Should return '10 + 2'</span>
<span class="cm-variable">expandedForm</span><span class="cm-punctuation">(</span><span class="cm-number">42</span><span class="cm-punctuation">)</span><span class="cm-punctuation">;</span> <span class="cm-comment"># Should return '40 + 2'</span>
<span class="cm-variable">expandedForm</span><span class="cm-punctuation">(</span><span class="cm-number">70304</span><span class="cm-punctuation">)</span><span class="cm-punctuation">;</span> <span class="cm-comment"># Should return '70000 + 300 + 4'</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">Kata</span>.<span class="cm-variable">expandedForm</span>(<span class="cm-number">12</span>); <span class="cm-variable">#</span> <span class="cm-variable">Should</span> <span class="cm-keyword">return</span> <span class="cm-string">"10 + 2"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">expandedForm</span>(<span class="cm-number">42</span>); <span class="cm-variable">#</span> <span class="cm-variable">Should</span> <span class="cm-keyword">return</span> <span class="cm-string">"40 + 2"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">expandedForm</span>(<span class="cm-number">70304</span>); <span class="cm-variable">#</span> <span class="cm-variable">Should</span> <span class="cm-keyword">return</span> <span class="cm-string">"70000 + 300 + 4"</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">Kata</span>.<span class="cm-variable">ExpandedForm</span>(<span class="cm-number">12</span>); <span class="cm-variable">#</span> <span class="cm-variable">Should</span> <span class="cm-keyword">return</span> <span class="cm-string">"10 + 2"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">ExpandedForm</span>(<span class="cm-number">42</span>); <span class="cm-variable">#</span> <span class="cm-variable">Should</span> <span class="cm-keyword">return</span> <span class="cm-string">"40 + 2"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">ExpandedForm</span>(<span class="cm-number">70304</span>); <span class="cm-variable">#</span> <span class="cm-variable">Should</span> <span class="cm-keyword">return</span> <span class="cm-string">"70000 + 300 + 4"</span>
</code></pre>
<pre style="display: none;"><code class="language-fsharp"><span class="cm-variable">expandedForm</span> <span class="cm-number">12</span><span class="cm-variable">L</span> <span class="cm-comment">// Should return "10 + 2"</span>
<span class="cm-variable">expandedForm</span> <span class="cm-number">42</span><span class="cm-variable">L</span> <span class="cm-comment">// Should return "40 + 2"</span>
<span class="cm-variable">expandedForm</span> <span class="cm-number">70304</span><span class="cm-variable">L</span> <span class="cm-comment">// Should return "70000 + 300 + 4"</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable">expanded_form</span>(<span class="cm-number">12</span>);    <span class="cm-comment">// Should return "10 + 2"</span>
<span class="cm-variable">expanded_form</span>(<span class="cm-number">42</span>);    <span class="cm-comment">// Should return "40 + 2"</span>
<span class="cm-variable">expanded_form</span>(<span class="cm-number">70304</span>); <span class="cm-comment">// Should return "70000 + 300 + 4"</span>
</code></pre>
<p>NOTE: All numbers will be whole numbers greater than 0.</p>
<p>If you liked this kata, check out <a href="https://www.codewars.com/kata/write-number-in-expanded-form-part-2" data-turbolinks="false" target="_blank">part 2</a>!!</p>

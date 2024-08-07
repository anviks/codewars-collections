<p>Given a 2D array and a number of generations, compute n timesteps of <a href="http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" data-turbolinks="false" target="_blank">Conway's Game of Life</a>.</p>
<p>The rules of the game are:</p>
<ol>
<li>Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.</li>
<li>Any live cell with more than three live neighbours dies, as if by overcrowding.</li>
<li>Any live cell with two or three live neighbours lives on to the next generation.</li>
<li>Any dead cell with exactly three live neighbours becomes a live cell.</li>
</ol>
<p>Each cell's neighborhood is the 8 cells immediately around it (i.e. <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" data-turbolinks="false" target="_blank">Moore Neighborhood</a>). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return <code>[[]]</code>.)</p>
<p>For illustration purposes, 0 and 1 will be represented as <code>░░</code> and <code>▓▓</code> blocks respectively (PHP: plain black and white squares). You can take advantage of the <code>htmlize</code> function to get a text representation of the universe, e.g.:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">console</span>.<span class="cm-property">log</span>(<span class="cm-variable">htmlize</span>(<span class="cm-variable">cells</span>));
</code></pre>
<pre style="display: none;"><code class="language-coffeescript"><span class="cm-variable">console</span><span class="cm-punctuation">.</span><span class="cm-property">log</span> <span class="cm-variable">htmlize</span><span class="cm-punctuation">(</span><span class="cm-variable">cells</span><span class="cm-punctuation">)</span>
</code></pre>
<pre><code class="language-python"><span class="cm-builtin">print</span>(<span class="cm-variable">htmlize</span>(<span class="cm-variable">cells</span>))
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">trace</span> (<span class="cm-variable">htmlize</span> <span class="cm-variable">cells</span>)
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">System</span>.<span class="cm-variable">out</span>.<span class="cm-variable">println</span>(<span class="cm-variable">LifeDebug</span>.<span class="cm-variable">htmlize</span>(<span class="cm-variable">cells</span>));
</code></pre>
<pre style="display: none;"><code class="language-swift"><span class="cm-variable">print</span><span class="cm-punctuation">(</span><span class="cm-variable">htmlize</span><span class="cm-punctuation">(</span><span class="cm-variable">cells</span><span class="cm-punctuation">)</span><span class="cm-punctuation">)</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-keyword">echo</span> <span class="cm-variable">htmlize</span>(<span class="cm-variable-2">$cells</span>) . <span class="cm-string">"</span><span class="cm-string">\r\n"</span>;
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-type">char</span> <span class="cm-type">*</span><span class="cm-variable">universe</span> <span class="cm-operator">=</span> <span class="cm-variable">htmlize</span>(<span class="cm-variable">cells</span>, <span class="cm-variable">rows</span>, <span class="cm-variable">columns</span>);
<span class="cm-variable">printf</span>(<span class="cm-string">"%s"</span>, <span class="cm-variable">universe</span>);
<span class="cm-variable">free</span>(<span class="cm-variable">universe</span>);
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">Console</span>.<span class="cm-variable">WriteLine</span>(<span class="cm-variable">ConwayLife</span>.<span class="cm-variable">Htmlize</span>(<span class="cm-variable">cells</span>));
</code></pre>

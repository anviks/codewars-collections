<p>Write a simple parser that will parse and run Deadfish.  </p>
<p>Deadfish has 4 commands, each 1 character long:</p>
<ul>
<li><code>i</code> increments the value (initially <code>0</code>)</li>
<li><code>d</code> decrements the value</li>
<li><code>s</code> squares the value</li>
<li><code>o</code> outputs the value into the return array</li>
</ul>
<p>Invalid characters should be ignored.</p>
<pre><code class="language-javascript"><span class="cm-variable">parse</span>(<span class="cm-string">"iiisdoso"</span>) <span class="cm-operator">=&gt;</span> [ <span class="cm-number">8</span>, <span class="cm-number">64</span> ]
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">Deadfish</span>.<span class="cm-variable">Parse</span>(<span class="cm-string">"iiisdoso"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-keyword">new</span> <span class="cm-type">int</span>[] {<span class="cm-number">8</span>, <span class="cm-number">64</span>};
</code></pre>
<pre style="display: none;"><code class="language-python"><span class="cm-variable">parse</span>(<span class="cm-string">"iiisdoso"</span>)  <span class="cm-operator">==&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-number">64</span>]
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">parse</span> <span class="cm-string">"iiisdoso"</span> <span class="cm-keyword">-&gt;</span> [ <span class="cm-number">8</span>, <span class="cm-number">64</span> ]
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-variable">parse</span>(<span class="cm-string">"iiisdoso"</span>) <span class="cm-operator">==</span> {<span class="cm-number">8</span>, <span class="cm-number">64</span>}
</code></pre>
<pre style="display: none;"><code class="language-go"><span class="cm-variable">Parse</span>(<span class="cm-string">"iiisdoso"</span>) <span class="cm-operator">==</span> []<span class="cm-keyword">int</span>{<span class="cm-number">8</span>, <span class="cm-number">64</span>}
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">parse</span>(<span class="cm-string">"iiisdoso"</span>)  <span class="cm-operator">==&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-number">64</span>]
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">Deadfish</span>.<span class="cm-variable">parse</span>(<span class="cm-string">"iiisdoso"</span>) <span class="cm-operator">=-</span> <span class="cm-keyword">new</span> <span class="cm-type">int</span>[] {<span class="cm-number">8</span>, <span class="cm-number">64</span>};
</code></pre>
<pre style="display: none;"><code class="language-groovy"><span class="cm-variable">DeadFish</span>.<span class="cm-property">parse</span>(<span class="cm-string">"iiisdoso"</span>)  <span class="cm-operator">==&gt;</span>  [<span class="cm-number">8</span>, <span class="cm-number">64</span>]
</code></pre>
<pre style="display: none;"><code class="language-scala"><span class="cm-variable">Deadfish</span>.<span class="cm-variable">parse</span>(<span class="cm-string">"iiisdoso"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-type">List</span>(<span class="cm-number">8</span>, <span class="cm-number">64</span>)
</code></pre>
<pre style="display: none;"><code class="language-typescript"><span class="cm-variable">parse</span>(<span class="cm-string">"iiisdoso"</span>) <span class="cm-operator">=&gt;</span> [<span class="cm-number">8</span>, <span class="cm-number">64</span>]
</code></pre>
<pre style="display: none;"><code class="language-julia"><span class="cm-variable">deadfish</span>(<span class="cm-string">"iiisdoso</span><span class="cm-string">"</span>) <span class="cm-operator">--&gt;</span> [<span class="cm-number">8</span>, <span class="cm-number">64</span>]
</code></pre>
<pre style="display: none;"><code class="language-powershell"><span class="cm-identifier">Eval-DeadFish</span> <span class="cm-operator">-</span><span class="cm-keyword">Data</span> <span class="cm-string">"ooo"</span> <span class="cm-operator">--</span><span class="cm-operator">&gt;</span> <span class="cm-punctuation">@(</span><span class="cm-number">0</span><span class="cm-punctuation">,</span> <span class="cm-number">0</span><span class="cm-punctuation">,</span> <span class="cm-number">0</span><span class="cm-punctuation">)</span>  <span class="cm-comment"># [long[]]</span>
</code></pre>
<pre style="display: none;"><code class="language-factor"><span class="cm-string">"</span><span class="cm-string">iiisdoso"</span> <span class="cm-variable">deadfish</span> <span class="cm-builtin">-&gt;</span> <span class="cm-keyword">{</span> <span class="cm-number">8 64</span> <span class="cm-keyword">}</span>
</code></pre>

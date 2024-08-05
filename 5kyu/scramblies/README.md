<p>Complete the  function <code>scramble(str1, str2)</code> that returns <code>true</code> if a portion of <code>str1</code> characters can be rearranged to match <code>str2</code>, otherwise returns <code>false</code>.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>Only lower case letters will be used (a-z). No punctuation or digits will be included.</li>
<li>Performance needs to be considered.</li>
</ul>
<h2 id="examples">Examples</h2>
<pre><code class="language-python"><span class="cm-variable">scramble</span>(<span class="cm-string">'rkqodlw'</span>, <span class="cm-string">'world'</span>) <span class="cm-operator">==&gt;</span> <span class="cm-keyword">True</span>
<span class="cm-variable">scramble</span>(<span class="cm-string">'cedewaraaossoqqyt'</span>, <span class="cm-string">'codewars'</span>) <span class="cm-operator">==&gt;</span> <span class="cm-keyword">True</span>
<span class="cm-variable">scramble</span>(<span class="cm-string">'katas'</span>, <span class="cm-string">'steak'</span>) <span class="cm-operator">==&gt;</span> <span class="cm-keyword">False</span>
</code></pre>

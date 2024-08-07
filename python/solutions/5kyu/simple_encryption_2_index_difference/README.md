<p>For encrypting strings this region of chars is given (in this order!):</p>
<ul>
<li>all letters (ascending, first all UpperCase, then all LowerCase)</li>
<li>all digits (ascending)</li>
<li>the following chars: <code>.,:;-?! '()$%&amp;"</code></li>
</ul>
<p>These are 77 chars! (This region is zero-based.)<br></p>
<p>Write two methods: <br></p>
<pre style="display: none;"><code class="language-csharp"><span class="cm-type">string</span> <span class="cm-def">Encrypt</span>(<span class="cm-type">string</span> <span class="cm-variable">text</span>)
<span class="cm-type">string</span> <span class="cm-def">Decrypt</span>(<span class="cm-type">string</span> <span class="cm-variable">encryptedText</span>)
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">encrypt</span>(<span class="cm-def">text</span>)
<span class="cm-keyword">function</span> <span class="cm-def">decrypt</span>(<span class="cm-def">encryptedText</span>)
</code></pre>
<pre style="display: none;"><code class="language-typescript"><span class="cm-keyword">export</span> <span class="cm-keyword">function</span> <span class="cm-def">encrypt</span>(<span class="cm-def">text</span>:<span class="cm-type">string</span>):<span class="cm-type">string</span>
<span class="cm-keyword">export</span> <span class="cm-keyword">function</span> <span class="cm-def">decrypt</span>(<span class="cm-def">encryptedText</span>:<span class="cm-type">string</span>):<span class="cm-type">string</span>
</code></pre>
<pre><code class="language-python"><span class="cm-keyword">def</span> <span class="cm-def">encrypt</span>(<span class="cm-variable">text</span>)
<span class="cm-keyword">def</span> <span class="cm-def">decrypt</span>(<span class="cm-variable">encrypted_text</span>)
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-variable">std::string</span> <span class="cm-def">encrypt</span>(<span class="cm-variable">std::string</span> <span class="cm-variable">text</span>)
<span class="cm-variable">std::string</span> <span class="cm-def">decrypt</span>(<span class="cm-variable">std::string</span> <span class="cm-variable">text</span>)
</code></pre>
<pre style="display: none;"><code class="language-clojure"><span class="cm-bracket">(</span><span class="cm-builtin">encrypt</span> <span class="cm-bracket">(</span><span class="cm-builtin">text</span><span class="cm-bracket">)</span><span class="cm-bracket">)</span>
<span class="cm-bracket">(</span><span class="cm-builtin">decrypt</span> <span class="cm-bracket">(</span><span class="cm-builtin">text</span><span class="cm-bracket">)</span><span class="cm-bracket">)</span>
</code></pre>
<p>Prechecks:<br></p>
<ol>
<li>If the input-string has chars, that are not in the region, throw an Exception(C#, Python) or Error(JavaScript).<br></li>
<li>If the input-string is null or empty return exactly this value!<br></li>
</ol>
<p>For building the encrypted string:<br></p>
<ol>
<li>For every second char do a switch of the case.<br></li>
<li>For every char take the index from the region. Take the difference from the region-index of the char before (from the input text! Not from the fresh encrypted char before!). (Char2 = Char1-Char2)<br>
Replace the original char by the char of the difference-value from the region. In this step the first letter of the text is unchanged.<br></li>
<li>Replace the first char by the mirror in the given region. (<code>'A' -&gt; '"'</code>, <code>'B' -&gt; '&amp;'</code>, ...)</li>
</ol>
<p>Simple example:</p>
<ul>
<li>Input:  <code>"Business"</code></li>
<li>Step 1: <code>"BUsInEsS"</code></li>
<li>Step 2: <code>"B61kujla"</code><ul>
<li><code>B -&gt; U</code><ul>
<li><code>B (1) - U (20) = -19</code></li>
<li><code>-19 + 77 = 58</code></li>
<li><code>Region[58] = "6"</code></li>
</ul>
</li>
<li><code>U -&gt; s</code><ul>
<li><code>U (20) - s (44) = -24</code></li>
<li><code>-24 + 77 = 53</code></li>
<li><code>Region[53] = "1"</code></li>
</ul>
</li>
</ul>
</li>
<li>Step 3: <code>"&amp;61kujla"</code></li>
</ul>
<p>This kata is part of the Simple Encryption Series:<br>
<a href="https://www.codewars.com/kata/simple-encryption-number-1-alternating-split" data-turbolinks="false" target="_blank">Simple Encryption #1 - Alternating Split</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-2-index-difference" data-turbolinks="false" target="_blank">Simple Encryption #2 - Index-Difference</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-3-turn-the-bits-around" data-turbolinks="false" target="_blank">Simple Encryption #3 - Turn The Bits Around</a><br>
<a href="https://www.codewars.com/kata/simple-encryption-number-4-qwerty" data-turbolinks="false" target="_blank">Simple Encryption #4 - Qwerty</a><br></p>
<p>Have fun coding it and please don't forget to vote and rank this kata! :-)</p>

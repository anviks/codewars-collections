<p>The word <code>i18n</code> is a common abbreviation of <code>internationalization</code> in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, <code>a11y</code> is an abbreviation of <code>accessibility</code>.</p>
<p>Write a function that takes a string and turns any and all "words" (see below) within that string of <strong>length 4 or greater</strong> into an abbreviation, following these rules:</p>
<ul>
<li>A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").</li>
<li>The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" =&gt; "e6t r2e").</li>
</ul>
<h2 id="example">Example</h2>
<pre><code class="language-javascript"><span class="cm-variable">abbreviate</span>(<span class="cm-string">"elephant-rides are really fun!"</span>)
<span class="cm-comment">//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*</span>
<span class="cm-comment">// words (^):   "elephant" "rides" "are" "really" "fun"</span>
<span class="cm-comment">//                123456     123     1     1234     1</span>
<span class="cm-comment">// ignore short words:               X              X</span>

<span class="cm-comment">// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"</span>
<span class="cm-comment">// all non-word characters (*) remain in place</span>
<span class="cm-comment">//                     "-"      " "    " "     " "     "!"</span>
<span class="cm-operator">===</span> <span class="cm-string">"e6t-r3s are r4y fun!"</span>
</code></pre>

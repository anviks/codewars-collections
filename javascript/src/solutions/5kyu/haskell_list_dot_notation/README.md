<p>I would like to mimic some of the amazing things Haskell can do with lists.</p>
<p>There are lots of things to do, so I'm going to break the work into several katas.</p>
<p>I'll warn you that perhaps you will have to refactor some parts of the code going forward, so you need to write the cleanest code possible.</p>
<p>Haskell lists are similar to JavaScript arrays.</p>
<p>For example, this is ok in both programming languages:</p>
<pre><code class="language-haskell">[<span class="cm-number">1</span>,<span class="cm-builtin">-</span><span class="cm-number">3</span>,<span class="cm-number">4</span>]
</code></pre>
<p>But Haskell allows you to define lists like this:</p>
<pre><code class="language-haskell">[<span class="cm-number">1</span><span class="cm-keyword">..</span><span class="cm-number">5</span>] <span class="cm-comment">--equivalent to [1,2,3,4,5]</span>
</code></pre>
<p>Or this way:</p>
<pre><code class="language-haskell">[<span class="cm-number">1</span>,<span class="cm-number">4</span><span class="cm-keyword">..</span><span class="cm-number">11</span>] <span class="cm-comment">--equivalent to [1,4,7,10]</span>
</code></pre>
<p>This is also valid:</p>
<pre><code class="language-haskell">[<span class="cm-number">5</span>,<span class="cm-number">4</span><span class="cm-keyword">..</span><span class="cm-number">2</span>] <span class="cm-comment">--equivalent to [5,4,3,2]</span>
</code></pre>
<p>A formal definition provided by <a href="http://www.codewars.com/users/nivoliev" data-turbolinks="false" target="_blank">nivoliev</a>:</p>
<ul>
<li>a list of individual elements : the resulting list is the list made of the individual elements as in classical Javascript</li>
<li>a range in the form <code>start..end</code> : if <code>end &gt;= start</code>, the list is <code>[start, start+1, start+2, ..., end]</code> otherwise the result is <code>[]</code></li>
<li>a single element a followed by a range : let <code>step = start - a</code><ul>
<li>if <code>start === end</code> the list is <code>[a,start]</code></li>
<li>if step is positive and <code>end &gt; start</code> then the list is <code>[a, a+step, a+2*step, ...]</code> as long as <code>a+k*step &lt;= end</code></li>
<li>if step is negative and end &lt; start then the list is <code>[a, a+step, a+2*step, ...]</code> as long as <code>a-k*step &gt;= end</code></li>
</ul>
</li>
<li>otherwise the list is <code>[]</code></li>
</ul>
<p>Some clarifying examples:</p>
<pre><code class="language-haskell">[<span class="cm-number">2</span>,<span class="cm-number">3</span>,<span class="cm-builtin">-</span><span class="cm-number">5</span>,<span class="cm-number">3</span>] <span class="cm-comment">-- just like in JavaScript : [2,3,-5,3]</span>
[<span class="cm-number">1</span><span class="cm-keyword">..</span><span class="cm-number">5</span>] <span class="cm-comment">-- goes forward with step 1 : [1,2,3,4,5]</span>
[<span class="cm-number">1</span>,<span class="cm-number">3</span><span class="cm-keyword">..</span><span class="cm-number">7</span>] <span class="cm-comment">-- goes forward with step 2 (3 - 1) : [1,3,5,7]</span>
[<span class="cm-number">6</span>,<span class="cm-number">5</span><span class="cm-keyword">..</span><span class="cm-number">3</span>] <span class="cm-comment">-- goes back with step -1 = (5 - 6) : [6,5,4,3]</span>
[<span class="cm-number">6</span>,<span class="cm-number">4</span><span class="cm-keyword">..</span><span class="cm-number">0</span>] <span class="cm-comment">-- goes back with step -2 = (4 -6) : [6, 4, 2, 0]</span>
[<span class="cm-number">5</span><span class="cm-keyword">..</span><span class="cm-number">3</span>] <span class="cm-comment">-- default step is 1 while the range is decreasing : []</span>
[<span class="cm-number">10</span>,<span class="cm-number">1</span><span class="cm-keyword">..</span><span class="cm-number">10</span>] <span class="cm-comment">-- goes back with step -9 for an increasing range : [10]</span>
[<span class="cm-number">1</span>,<span class="cm-number">1</span><span class="cm-keyword">..</span><span class="cm-number">10</span>] <span class="cm-comment">-- goes forwaed with step is 0 = ( 1 - 1) : infitite list [1,1,...]. Do not worry about this case in this kata for this, we will deal with it in the third part.</span>
[<span class="cm-number">1</span><span class="cm-keyword">..</span><span class="cm-number">9</span>,<span class="cm-number">12</span><span class="cm-keyword">..</span><span class="cm-number">15</span>] <span class="cm-comment">-- invalid since one single range is allowed</span>
[<span class="cm-number">1</span>,<span class="cm-number">2</span><span class="cm-keyword">..</span><span class="cm-number">20</span>,<span class="cm-number">25</span>] <span class="cm-comment">-- invalid since a range has to be the final item</span>
[<span class="cm-number">1</span>,<span class="cm-number">2</span>,<span class="cm-number">3</span><span class="cm-keyword">..</span><span class="cm-number">20</span>] <span class="cm-comment">-- invalid since at most one inidivual element can be provided before a range</span>
<span class="cm-variable">//</span><span class="cm-variable-2">See</span> <span class="cm-variable">the</span> <span class="cm-variable">tests</span> <span class="cm-variable">for</span> <span class="cm-variable">more</span> <span class="cm-variable">examples</span>
</code></pre>
<p>Your work is to implement something like this in JavaScript.</p>
<p>With this purpose, I have defined the <code>ArrayComprehension</code> function.</p>
<pre><code class="language-javascript"><span class="cm-keyword">function</span> <span class="cm-def">ArrayComprehension</span>(<span class="cm-def">options</span>) {
  
}
</code></pre>
<p>The <code>options</code> parameter is an object with the <code>generator</code> key. The generator key is a string with list values:</p>
<pre><code class="language-javascript"><span class="cm-variable">ArrayComprehension</span>({<span class="cm-property">generator</span>: <span class="cm-string">'1,4,-3'</span>}); <span class="cm-comment">// returns [1,4,-3]</span>
<span class="cm-variable">ArrayComprehension</span>({<span class="cm-property">generator</span>: <span class="cm-string">'1..5'</span>}); <span class="cm-comment">// returns [1,2,3,4,5]</span>
<span class="cm-variable">ArrayComprehension</span>({<span class="cm-property">generator</span>: <span class="cm-string">'1,3..7'</span>}); <span class="cm-comment">// returns [1,3,5,7]</span>
<span class="cm-variable">ArrayComprehension</span>({<span class="cm-property">generator</span>: <span class="cm-string">'7,5..2'</span>}); <span class="cm-comment">// returns [7,5,3]</span>
</code></pre>
<p>It is assumed that the generator format is always right. Therefore, no need to check it.</p>

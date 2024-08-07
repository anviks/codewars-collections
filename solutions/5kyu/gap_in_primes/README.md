<p>The prime numbers are not regularly spaced. For example from <code>2</code> to <code>3</code> the gap is <code>1</code>.
From <code>3</code> to <code>5</code> the gap is <code>2</code>. From <code>7</code> to <code>11</code> it is <code>4</code>.
Between 2 and 50 we have the following pairs of 2-gaps primes:
<code>3-5, 5-7, 11-13, 17-19, 29-31, 41-43</code></p>
<p>A prime gap of length n is a run of n-1 consecutive composite numbers between two <strong>successive</strong> primes (see: <a href="http://mathworld.wolfram.com/PrimeGaps.html" data-turbolinks="false" target="_blank">http://mathworld.wolfram.com/PrimeGaps.html</a>).</p>
<p>We will write a function gap with parameters:</p>
<ul>
<li><p><code>g</code> (integer &gt;= 2) which indicates the gap we are looking for</p>
</li>
<li><p><code>m</code> (integer &gt; 2) which gives the start of the search (m inclusive)</p>
</li>
<li><p><code>n</code> (integer &gt;= m) which gives the end of the search (n inclusive)</p>
</li>
</ul>
<p>In the example above <code>gap(2, 3, 50)</code> will return <code>[3, 5] or (3, 5) or {3, 5}</code> which is the first pair between 3 and 50 with a 2-gap.</p>
<p>So this function should return the <strong>first</strong> pair of two prime numbers spaced with a gap of <code>g</code> between the limits <code>m</code>, <code>n</code> if these numbers exist otherwise `nil or null or None or Nothing (or ... depending on the language). </p>
<pre><code>In such a case (no pair of prime numbers with a gap of `g`)
In C: return [0, 0]
In C++, Lua, COBOL: return `{0, 0}`. 
In F#: return `[||]`. 
In Kotlin, Dart and Prolog: return `[]`.
In Pascal: return Type TGap (0, 0).
</code></pre>
<h4 id="examples">Examples:</h4>
<p>- 
<code>gap(2, 5, 7) --&gt; [5, 7] or (5, 7) or {5, 7}</code></p>
<ul>
<li><p><code>gap(2, 5, 5) --&gt; nil. In C++ {0, 0}. In F# [||]. In Kotlin, Dart and Prolog return </code>[]`</p>
</li>
<li><p><code>gap(4, 130, 200) --&gt; [163, 167] or (163, 167) or {163, 167}</code></p>
</li>
</ul>
<p>([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)</p>
<ul>
<li><p><code>gap(6,100,110) --&gt; nil or {0, 0} or ...</code> : between 100 and 110 we have <code>101, 103, 107, 109</code> but <code>101-107</code>is not a 6-gap because there is <code>103</code>in between and <code>103-109</code>is not a 6-gap because there is <code>107</code>in between.</p>
</li>
<li><p>You can see more examples of return in Sample Tests.</p>
</li>
</ul>
<h4 id="note-for-go">Note for Go</h4>
<p>For Go: nil slice is expected when there are no gap between m and n.
Example: gap(11,30000,100000) --&gt; nil</p>
<h4 id="ref">Ref</h4>
<p><a href="https://en.wikipedia.org/wiki/Prime_gap" data-turbolinks="false" target="_blank">https://en.wikipedia.org/wiki/Prime_gap</a></p>

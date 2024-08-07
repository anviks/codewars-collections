<p>Write a function that, given a string of text (possibly with punctuation and line-breaks),
returns an array of the top-3 most occurring words, in descending order of the number of occurrences.</p>
<h2 id="assumptions">Assumptions:</h2>
<ul>
<li>A word is a string of letters (A to Z) optionally containing one or more apostrophes (<code>'</code>) in ASCII.</li>
<li>Apostrophes can appear at the start, middle or end of a word (<code>'abc</code>, <code>abc'</code>, <code>'abc'</code>, <code>ab'c</code> are all valid)</li>
<li>Any other characters (e.g. <code>#</code>, <code>\</code>, <code>/</code> , <code>.</code> ...) are not part of a word and should be treated as whitespace.</li>
<li>Matches should be case-insensitive, and the words in the result should be lowercased.</li>
<li>Ties may be broken arbitrarily.</li>
<li>If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.</li>
</ul>
<h2 id="examples">Examples:</h2>
<pre><code>"In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."

--&gt; ["a", "of", "on"]


"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

--&gt; ["e", "ddd", "aa"]


"  //wont won't won't"

--&gt; ["won't", "wont"]
</code></pre>
<h2 id="bonus-points-not-really-but-just-for-fun">Bonus points (not really, but just for fun):</h2>
<ol>
<li>Avoid creating an array whose memory footprint is roughly as big as the input text.</li>
<li>Avoid sorting the entire array of unique words.</li>
</ol>

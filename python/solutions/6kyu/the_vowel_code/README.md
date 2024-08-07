<p><strong>Step 1:</strong> Create a function called <code>encode()</code> to replace all the lowercase vowels in a given string with numbers according to the following pattern:</p>
<pre><code>a -&gt; 1
e -&gt; 2
i -&gt; 3
o -&gt; 4
u -&gt; 5
</code></pre>
<p>For example, <code>encode("hello")</code> would return <code>"h2ll4"</code>. There is no need to worry about uppercase vowels in this kata.</p>
<p><strong>Step 2:</strong> Now create a function called <code>decode()</code> to turn the numbers back into vowels according to the same pattern shown above.</p>
<p>For example, <code>decode("h3 th2r2")</code> would return <code>"hi there"</code>.</p>
<p>For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.</p>

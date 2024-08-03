<p><em>(Revised version from previous series 6)</em></p>
<h1 id="number-pyramid">Number Pyramid:</h1>
<p>Image a number pyramid starts with <code>1</code>, and the numbers increasing by <code>1</code>. </p>
<p>Today, it has total <code>5000</code> levels.</p>
<p>For example, the top 4 levels of the pyramid looks like:</p>
<pre><code>    1
   2 3
  4 5 6
 7 8 9 10
</code></pre>
<hr>
<h1 id="left-and-right">Left and Right:</h1>
<p>Now from the center line, cut the pyramid into <code>Left</code> and <code>Right</code>.</p>
<p>In the above example, it will become:</p>
<pre><code>Left: # Right:
      #
   2  # 3
  4   #  6
 7 8  # 9 10

 (The numbers of center line was cut, do not go on any side.)
</code></pre>
<hr>
<h1 id="input">Input:</h1>
<p>You will be given a number <code>n</code>, it will not go beyond <code>5000</code> levels.</p>
<hr>
<h1 id="output">Output:</h1>
<p>You need to return the number is locating at <code>Left</code> or <code>Right</code> part.</p>
<ul>
<li><p>Return <code>'L'</code> for Left.</p>
</li>
<li><p>Return <code>'R'</code> for Right.</p>
</li>
<li><p>Return <code>'C'</code> for Center/been Cut</p>
</li>
</ul>
<p><strong>Examples:</strong></p>
<pre><code>left_right(1) --&gt; 'C'
left_right(2) --&gt; 'L'
left_right(3) --&gt; 'R'
left_right(4) --&gt; 'L'
left_right(5) --&gt; 'C'
left_right(6) --&gt; 'R'
</code></pre>
<hr>
<h1 id="golfing-message">Golfing Message:</h1>
<p>The length of your code should be less or equal to <code>72</code>.</p>
<p>The length of reference solution is <code>65</code> (Python) and <code>67</code> (JS).</p>
<hr>
<p>If you like this series, welcome to do <a href="https://www.codewars.com/collections/code-golf-number-pyramid-series" data-turbolinks="false" target="_blank">other kata</a> of it.</p>

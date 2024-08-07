<h2 id="task">Task</h2>
<p> You are given an odd integer <code>n</code> and a two-dimensional array <code>s</code>, which contains <code>n</code> equal-sized arrays of <code>0s</code> and <code>1s</code>.</p>
<p>Return an array of the same length as the elements of <code>n</code>, such that its <code>i</code>th element is the one that appears most frequently at the <code>i</code>th position of <code>s</code>' elements.</p>
<h2 id="code-limit">Code Limit</h2>
<p>Less than <code>55</code> characters.</p>
<h2 id="example">Example</h2>
<p>  For <code>n = 3, s = [[1,1,0], [1,0,0], [0,1,1]],</code></p>
<p>  the output should be <code>[1,1,0]</code></p>
<pre><code>1st  2nd  3rd
 1    1    0
 1    0    0
 0    1    1
 

At the 1st position 
there're two 1s and one 0, 
so in the 1st element of the resulting array is 1.

At the 2nd position
there're two 1s and one 0,
so in the 2nd element of the resulting array is 1.

At the 3rd position 
there're two 0s and one 1, 
so in the 3rd element of the resulting array is 0.
</code></pre>

<p>A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. 
Each book has a code <code>c</code> of 3, 4, 5 or more characters. The <strong>1st</strong> character of a code is a capital letter which defines the book category.</p>
<p>  In the bookseller's stocklist each code <code>c</code> is followed by a space and by a positive integer n (int n &gt;= 0) 
  which indicates the quantity of books of this code in stock.</p>
<p>For example an extract of a stocklist could be:</p>
<pre><code>L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
</code></pre>
<p>  You will be given a stocklist (e.g. : L) and a list of categories in capital letters 
  e.g : </p>
<pre><code>M = {"A", "B", "C", "W"} 
or
M = ["A", "B", "C", "W"] or ...
</code></pre>
<p>  and your task is to find all the books of L with codes 
  belonging to each category of M and to sum their quantity according to each category. </p>
<p>  For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket/Prolog a list of pairs):  </p>
<pre><code>(A : 20) - (B : 114) - (C : 50) - (W : 0)
</code></pre>
<p>  where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding
  to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.</p>
<p>  If L or M are empty return string is <code>""</code> (Clojure/Racket/Prolog should return an empty array/list instead).</p>
<h4 id="notes">Notes:</h4>
<ul>
<li>In the result codes and their values are in the same order as in M.</li>
<li>See "Samples Tests" for the return.</li>
</ul>

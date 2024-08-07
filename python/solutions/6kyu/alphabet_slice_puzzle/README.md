<p>In this kata, you need to code a function that takes two parameters, A and B, both representing letters from the English alphabet.</p>
<p>It is guaranteed that:</p>
<ol>
  <li>Both letters are the same case (Either both are uppercase or both are lowercase, never a mix)</li>
  <li>B is always a letter that comes after A in the alphabet (or is the same letter). For instance (A="A", B="F") and (A="g", B = "g") are valid parameter sets for the function. On the other hand (a="N" b="H") is not</li>
</ol>

<p>Your mission, if you accept it, is to write a function slice() that returns the inclusive slice of the English alphabet starting at A and ending at B. A few examples are provided for clarity:</p>
<pre><code>slice("A", "B") --&gt; "AB"
slice("D", "H") --&gt; "DEFGH"
slice("f", "f") --&gt; "f"
slice("x", "z") --&gt; "xyz"
</code></pre>
<p>Astute readers will probably think there may be a catch given the Kyu rating on this Kata. And you would be wrong! There is not ONE catch, not TWO, But THREE catches (a-ha-ha)</p>
<ol>
  <li>Your code can at most be two lines long</li>
  <li>You code can at most be 100 charaters long</li>
  <li>Finally, you may not use the quoting characters (' and ") as well as "str" or square braces in your code</li>
</ol>

<p>(Note to contributors: Please inform me if there is any hack I might have missed that would allow a too-trivial solution for this to exist.) </p>


<p>Happy coding!</p>

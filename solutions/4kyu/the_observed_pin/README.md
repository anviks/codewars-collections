<p>Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.</p>
<p>The keypad has the following layout:</p>
<pre><code>┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
</code></pre>
<p>He noted the PIN <code>1357</code>, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the <code>1</code> it could also be the <code>2</code> or <code>4</code>. And instead of the <code>5</code> it could also be the <code>2</code>, <code>4</code>, <code>6</code> or <code>8</code>.</p>
<p>He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.</p>
<p>* possible in sense of: the observed PIN itself and all variations considering the adjacent digits</p>
<p>Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#)  of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function <code>getPINs</code> (<code>get_pins</code> in python, <code>GetPINs</code> in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.</p>
<p>Detective, we are counting on you!</p>

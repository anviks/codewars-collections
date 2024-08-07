<p>1) 
Given some text, count each alphabetic character's occurrence in it, regardless of the case.</p>
<p>2) 
Let's suppose you have to use an old terminal window to represent the occurrencies of each character in a text-based horizontal bar graph. The terminal has a maximum width, provided as parameter (<code>max_units_on_screen</code>), and you have to abide by it. </p>
<p>For example, if the maximum width is 80, your longest bar in the graph will be scaled to this size and all the others have to be represented and scaled proportionally to this size.
Every unit of the bar will be represented by the character <code>#</code>.
See examples below for typical output format.</p>
<p>3) 
The bars of the graph have to be sorted by number of occurrencies (from biggest to lowest, before getting scaled), then by alphabetic order of the letter (from a to z). Approximation of decimal numbers will happen on the lowest integer (for example: <code>57.1</code>, <code>57.2</code>, <code>57.68</code>, <code>57.999</code> will all get reduced to <code>57</code> )</p>
<p>Example </p>
<p>Input: </p>
<pre><code>count_and_print_graph("just a short text", 4)
</code></pre>
<p>Output: </p>
<pre><code>t:####
s:##
a:#
e:#
h:#
j:#
o:#
r:#
u:#
x:#
</code></pre>
<p>Example 2</p>
<p>Input: </p>
<pre><code>count_and_print_graph("just a short text", 23)
</code></pre>
<p>Output: </p>
<pre><code>t:#######################
s:###########
a:#####
e:#####
h:#####
j:#####
o:#####
r:#####
u:#####
x:#####
</code></pre>

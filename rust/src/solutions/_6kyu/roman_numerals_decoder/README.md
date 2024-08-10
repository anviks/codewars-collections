<p>Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.</p>
<p><a href="https://en.wikipedia.org/wiki/Roman_numerals#Standard_form" data-turbolinks="false" target="_blank">Modern Roman numerals</a> are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.</p>
<h2 id="example">Example:</h2>
<pre><code>"MM"      -&gt; 2000
"MDCLXVI" -&gt; 1666
"M"       -&gt; 1000
"CD"      -&gt;  400
"XC"      -&gt;   90
"XL"      -&gt;   40
"I"       -&gt;    1
</code></pre>
<h2 id="help">Help:</h2>
<pre><code>Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
</code></pre>
<p><em>Courtesy of rosettacode.org</em></p>

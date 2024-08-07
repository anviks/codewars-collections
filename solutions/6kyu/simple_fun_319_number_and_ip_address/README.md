<h1 id="task">Task</h1>
<p>An IP address contains four numbers(0-255) and separated by dots. It can be converted to a number by this way:</p>
<p>Given a string <code>s</code> represents a number or an IP address. Your task is to convert it to another representation(<code>number to IP address</code> or <code>IP address to number</code>).</p>
<p>You can assume that all inputs are valid.</p>
<h1 id="example">Example</h1>
<p>Example IP address: <code>10.0.3.193</code></p>
<p>Convert each number to a 8-bit binary string
(may needs to pad leading zeros to the left side):</p>
<pre><code>10  --&gt;  00001010
0   --&gt;  00000000
3   --&gt;  00000011
193 --&gt;  11000001
</code></pre>
<p>Combine these four strings: <code>00001010 00000000 00000011 11000001</code> and then convert them to a decimal number:
<code>167773121</code></p>
<h1 id="inputoutput">Input/Output</h1>
<p><code>[input]</code> string <code>s</code></p>
<p>A number or IP address in string format.</p>
<p><code>[output]</code> a string</p>
<p>A converted number or IP address in string format.</p>
<h1 id="example-1">Example</h1>
<p>For <code>s = "10.0.3.193"</code>, the output should be <code>"167773121"</code>.</p>
<p>For <code>s = "167969729"</code>, the output should be <code>"10.3.3.193"</code>.</p>

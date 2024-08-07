<p>Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between <code>0</code> and <code>255</code>, inclusive.</p>
<h4 id="valid-inputs-examples">Valid inputs examples:</h4>
<pre><code>Examples of valid inputs:
1.2.3.4
123.45.67.89
</code></pre>
<h4 id="invalid-input-examples">Invalid input examples:</h4>
<pre><code>1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
</code></pre>
<h4 id="notes">Notes:</h4>
<ul>
<li>Leading zeros (e.g. <code>01.02.03.04</code>) are considered invalid</li>
<li>Inputs are guaranteed to be a single string</li>
</ul>

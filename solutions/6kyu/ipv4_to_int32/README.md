<p>Take the following IPv4 address:  <code>128.32.10.1</code>. This address has 4 octets where each octet is a single byte (or 8 bits).</p>
<ul>
<li>1st octet 128 has the binary representation: 10000000</li>
<li>2nd octet 32 has the binary representation: 00100000</li>
<li>3rd octet 10 has the binary representation: 00001010</li>
<li>4th octet 1 has the binary representation: 00000001</li>
</ul>
<p>So <code>128.32.10.1</code> == <code>10000000.00100000.00001010.00000001</code></p>
<p>Because the above IP address has 32 bits, we can represent it as the 32
bit number: 2149583361.</p>
<p>Write a function <code>ip_to_int32(ip)</code> ( <strong>JS</strong>: <code>ipToInt32(ip)</code> ) that takes an IPv4 address and returns
a 32 bit number.</p>
<h3 id="example">Example</h3>
<pre><code class="language-text">"128.32.10.1" =&gt; 2149583361
</code></pre>

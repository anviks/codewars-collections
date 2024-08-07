<p>An <a href="http://en.wikipedia.org/wiki/IP_address" data-turbolinks="false" target="_blank">IPv4 address</a> is a 32-bit number that identifies a device on the internet.</p>
<p>While computers read and write IP addresses as a 32-bit number, we prefer to read them in dotted-decimal notation, which is basically the number split into 4 chunks of 8 bits, converted to decimal, and delmited by a dot.</p>
<p>In this kata, you will create the function <code>ipToNum</code> (or <code>ip_to_num</code>, depending on the language) that takes an <code>ip</code> address and converts it to a number, as well as the function <code>numToIp</code> (or <code>num_to_ip</code>) that takes a number and converts it to an IP address string.  Input will always be valid.</p>
<h2 id="conversion-example">Conversion Example</h2>
<pre><code class="language-javascript"><span class="cm-comment">//original IP address</span>
<span class="cm-number">192.168</span><span class="cm-number">.1</span><span class="cm-number">.1</span>

<span class="cm-comment">//breaks down into 4 binary octets</span>
<span class="cm-number">11000000</span> . <span class="cm-number">10101000</span> . <span class="cm-number">
00000001</span> . <span class="cm-number">00000001</span>

<span class="cm-comment">//which are merged together (unsigned 32-bit binary)</span>
<span class="cm-number">11000000101010000000000100000001</span>

<span class="cm-comment">//and finally converted to base 10</span>
<span class="cm-number">3232235777</span>
</code></pre>
<p>Note that the binary octets are <em>unsigned</em> (so we can't have negative numbers).</p>
<h2 id="examples">Examples</h2>
<h3 id="iptonum--ip_to_num">ipToNum / ip_to_num</h3>
<pre><code>'192.168.1.1' converts to 3232235777
'10.0.0.0'    converts to  167772160
'176.16.0.1'  converts to 2953838593
</code></pre>
<h3 id="numtoip--num_to_ip">numToIp / num_to_ip</h3>
<pre><code>3232235777 converts to '192.168.1.1'
 167772160 converts to    '10.0.0.0'
2953838593 converts to  '176.16.0.1'
</code></pre>

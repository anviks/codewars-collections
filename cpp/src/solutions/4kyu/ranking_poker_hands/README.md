<p>A famous casino is suddenly faced with a sharp decline of their revenues. They decide to offer Texas hold'em also online. Can you help them by writing an algorithm that can rank poker hands? </p>
<h2 id="task">Task</h2>
<p>Create a poker hand that has a method to compare itself to another poker hand:</p>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">Result</span> <span class="cm-variable">PokerHand</span>.<span class="cm-variable">CompareWith</span>(<span class="cm-variable">PokerHand</span> <span class="cm-variable">hand</span>);
</code></pre>
<pre style="display: none;"><code class="language-fsharp"><span class="cm-variable">PokerHand</span><span class="cm-operator">.</span><span class="cm-variable">compareWith</span><span class="cm-operator">:</span> <span class="cm-variable">hand</span><span class="cm-operator">:</span> <span class="cm-variable">PokerHand</span> <span class="cm-operator">-</span><span class="cm-operator">&gt;</span> <span class="cm-variable">Result</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">Result</span> <span class="cm-variable">PokerHand</span>.<span class="cm-variable">compareWith</span>(<span class="cm-variable">PokerHand</span> <span class="cm-variable">hand</span>);
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">PokerHand</span>.<span class="cm-property">prototype</span>.<span class="cm-property">compareWith</span> <span class="cm-operator">=</span> <span class="cm-keyword">function</span>(<span class="cm-def">hand</span>){<span class="cm-meta">...</span>};
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-variable">Result</span> <span class="cm-def">compare</span> (<span class="cm-variable">Hand</span><span class="cm-operator">*</span> <span class="cm-variable">player</span>, <span class="cm-variable">Hand</span><span class="cm-operator">*</span> <span class="cm-variable">opponent</span>);
</code></pre>
<pre><code class="language-cpp"><span class="cm-variable">Result</span> <span class="cm-def">compare</span> (<span class="cm-keyword">const</span> <span class="cm-variable">PokerHand</span> <span class="cm-operator">&amp;</span><span class="cm-variable">player</span>, <span class="cm-keyword">const</span> <span class="cm-variable">PokerHand</span> <span class="cm-operator">&amp;</span><span class="cm-variable">opponent</span>);
</code></pre>
<pre style="display: none;"><code class="language-python"><span class="cm-variable">compare_with</span>(<span class="cm-variable-2">self</span>, <span class="cm-variable">other_hand</span>)
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">compare_with</span>(<span class="cm-variable">other_hand</span>)
</code></pre>
<pre style="display: none;"><code class="language-elixir"><span class="cm-tag">PokerHand</span><span class="cm-operator">.</span><span class="cm-property">compare</span>(<span class="cm-tag">String</span> <span class="cm-variable">player</span>, <span class="cm-tag">String</span> <span class="cm-variable">opponent</span>)
</code></pre>
<p>A poker hand has a constructor that accepts a string containing 5 cards:</p>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">PokerHand</span> <span class="cm-variable">hand</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">PokerHand</span>(<span class="cm-string">"KS 2H 5C JD TD"</span>);
</code></pre>
<pre style="display: none;"><code class="language-fsharp"><span class="cm-keyword">let</span> <span class="cm-variable">hand</span> <span class="cm-operator">=</span> <span class="cm-variable">PokerHand</span>(<span class="cm-string">"KS 2H 5C JD TD"</span>)
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">PokerHand</span> <span class="cm-variable">hand</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">PokerHand</span>(<span class="cm-string">"KS 2H 5C JD TD"</span>);
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">hand</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">PokerHand</span>(<span class="cm-string">"KS 2H 5C JD TD"</span>);
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-variable">Hand</span> <span class="cm-operator">*</span><span class="cm-variable">hand</span> <span class="cm-operator">=</span> <span class="cm-variable">PokerHand</span> (<span class="cm-string">"KS 2H 5C JD TD"</span>);
</code></pre>
<pre><code class="language-cpp"><span class="cm-variable">PokerHand</span> <span class="cm-def">hand</span> (<span class="cm-string">"KS 2H 5C JD TD"</span>);
</code></pre>
<pre style="display: none;"><code class="language-python"><span class="cm-variable">PokerHand</span>(<span class="cm-string">"KS 2H 5C JD TD"</span>)
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-tag">PokerHand</span><span class="cm-operator">.</span><span class="cm-property">new</span>(<span class="cm-string">"KS 2H 5C JD TD"</span>)
</code></pre>
<pre style="display: none;"><code class="language-elixir"><span class="cm-comment"># no constructor in elixir, pass the string into the compare</span>
<span class="cm-string">"KS 2H 5C JD TD"</span>
</code></pre>
<p>The characteristics of the string of cards are:</p>
<ul>
<li>Each card consists of two characters, where</li>
<li>The first character is the value of the card: <code>2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)</code></li>
<li>The second character represents the suit: <code>S(pades), H(earts), D(iamonds), C(lubs)</code></li>
<li>A space is used as card separator between cards</li>
</ul>
<p>The result of your poker hand compare can be one of these 3 options:</p>
<pre style="display: none;"><code class="language-csharp"><span class="cm-keyword">public</span> <span class="cm-keyword">enum</span> <span class="cm-variable">Result</span> 
{ 
    <span class="cm-variable">Win</span>, 
    <span class="cm-variable">Loss</span>, 
    <span class="cm-variable">Tie</span> 
}
</code></pre>
<pre style="display: none;"><code class="language-fsharp"><span class="cm-keyword">type</span> <span class="cm-variable">Result</span> <span class="cm-operator">=</span>
<span class="cm-operator">|</span> <span class="cm-variable">Win</span> <span class="cm-operator">=</span> <span class="cm-number">0</span> 
<span class="cm-operator">|</span> <span class="cm-variable">Loss</span> <span class="cm-operator">=</span> <span class="cm-number">1</span>
<span class="cm-operator">|</span> <span class="cm-variable">Tie</span> <span class="cm-operator">=</span> <span class="cm-number">2</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-keyword">public</span> <span class="cm-keyword">enum</span> <span class="cm-def">Result</span>
{
    <span class="cm-variable">WIN</span>,
    <span class="cm-variable">LOSS</span>,
    <span class="cm-variable">TIE</span>
}
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">Result</span> <span class="cm-operator">=</span> 
{
    <span class="cm-string cm-property">"win"</span>: <span class="cm-number">1</span>,
    <span class="cm-string cm-property">"loss"</span>: <span class="cm-number">2</span>,
    <span class="cm-string cm-property">"tie"</span>: <span class="cm-number">3</span>
}
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-keyword">typedef</span> <span class="cm-keyword">enum</span> { <span class="cm-variable">Win</span>, <span class="cm-variable">Loss</span>, <span class="cm-variable">Tie</span> } <span class="cm-variable">Result</span>;
</code></pre>
<pre><code class="language-cpp"><span class="cm-keyword">enum</span> <span class="cm-keyword">class</span> <span class="cm-def">Result</span> { <span class="cm-variable">Win</span>, <span class="cm-variable">Loss</span>, <span class="cm-variable">Tie</span> };
</code></pre>
<pre style="display: none;"><code class="language-python">[ <span class="cm-string">"Win"</span>, <span class="cm-string">"Tie"</span>, <span class="cm-string">"Loss"</span> ]
</code></pre>
<pre style="display: none;"><code class="language-ruby">[ <span class="cm-string">"Win"</span>, <span class="cm-string">"Tie"</span>, <span class="cm-string">"Loss"</span> ]
</code></pre>
<pre style="display: none;"><code class="language-elixir"><span class="cm-variable-2">@result</span> <span class="cm-string">%{win: 1, loss: 2, tie: 3}</span>
</code></pre>
<h2 id="notes">Notes</h2>
<ul>
<li>Apply the <a href="https://en.wikipedia.org/wiki/Texas_hold_%27em" data-turbolinks="false" target="_blank">Texas Hold'em</a> rules for ranking the cards.</li>
<li>Low aces are valid in this kata.</li>
<li>There is no ranking for the suits.</li>
</ul>
<p>If you finished this kata, you might want to continue with <a href="https://www.codewars.com/kata/sortable-poker-hands" data-turbolinks="false" target="_blank">Sortable Poker Hands</a></p>

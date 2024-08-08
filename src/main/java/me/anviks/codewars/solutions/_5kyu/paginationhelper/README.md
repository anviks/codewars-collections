<p>For this exercise you will be strengthening your page-fu mastery.  You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array. </p>
<p>The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant. </p>
<p>The following are some examples of how this class is used:</p>
<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">helper</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">PaginationHelper</span>([<span class="cm-string">'a'</span>,<span class="cm-string">'b'</span>,<span class="cm-string">'c'</span>,<span class="cm-string">'d'</span>,<span class="cm-string">'e'</span>,<span class="cm-string">'f'</span>], <span class="cm-number">4</span>);
<span class="cm-variable">helper</span>.<span class="cm-property">pageCount</span>(); <span class="cm-comment">// should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-property">itemCount</span>(); <span class="cm-comment">// should == 6</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageItemCount</span>(<span class="cm-number">0</span>); <span class="cm-comment">// should == 4</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageItemCount</span>(<span class="cm-number">1</span>); <span class="cm-comment">// last page - should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageItemCount</span>(<span class="cm-number">2</span>); <span class="cm-comment">// should == -1 since the page is invalid</span>

<span class="cm-comment">// pageIndex takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageIndex</span>(<span class="cm-number">5</span>); <span class="cm-comment">// should == 1 (zero based index)</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageIndex</span>(<span class="cm-number">2</span>); <span class="cm-comment">// should == 0</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageIndex</span>(<span class="cm-number">20</span>); <span class="cm-comment">// should == -1</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageIndex</span>(<span class="cm-operator">-</span><span class="cm-number">10</span>); <span class="cm-comment">// should == -1</span>
</code></pre>
<pre style="display: none;"><code class="language-crystal"><span class="cm-variable">helper</span> <span class="cm-operator">=</span> <span class="cm-tag">PaginationHelper</span>(<span class="cm-tag">Char</span>)<span class="cm-operator">.</span><span class="cm-property">new</span>([<span class="cm-atom">'a'</span>,<span class="cm-atom">'b'</span>,<span class="cm-atom">'c'</span>,<span class="cm-atom">'d'</span>,<span class="cm-atom">'e'</span>,<span class="cm-atom">'f'</span>], <span class="cm-number">4</span>);
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_count</span>() <span class="cm-comment"># should == 2</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">item_count</span>() <span class="cm-comment"># should == 6</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_item_count</span>(<span class="cm-number">0</span>) <span class="cm-comment"># should == 4</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_item_count</span>(<span class="cm-number">1</span>) <span class="cm-comment"># last page - should == 2</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_item_count</span>(<span class="cm-number">2</span>) <span class="cm-comment"># should == -1 since the page is invalid</span>

<span class="cm-comment"># pageIndex takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_index</span>(<span class="cm-number">5</span>) <span class="cm-comment"># should == 1 (zero based index)</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_index</span>(<span class="cm-number">2</span>) <span class="cm-comment"># should == 0</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_index</span>(<span class="cm-number">20</span>) <span class="cm-comment"># should == -1</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_index</span>(<span class="cm-operator">-</span><span class="cm-number">10</span>) <span class="cm-comment"># should == -1</span>
</code></pre>
<pre><code class="language-java"><span class="cm-variable">PaginationHelper</span><span class="cm-operator">&lt;</span><span class="cm-type">Character</span><span class="cm-operator">&gt;</span> <span class="cm-variable">helper</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">PaginationHelper</span>(<span class="cm-variable">Arrays</span>.<span class="cm-variable">asList</span>(<span class="cm-string">'a'</span>, <span class="cm-string">'b'</span>, <span class="cm-string">'c'</span>, <span class="cm-string">'d'</span>, <span class="cm-string">'e'</span>, <span class="cm-string">'f'</span>), <span class="cm-number">4</span>);
<span class="cm-variable">helper</span>.<span class="cm-variable">pageCount</span>(); <span class="cm-comment">// should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">itemCount</span>(); <span class="cm-comment">// should == 6</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageItemCount</span>(<span class="cm-number">0</span>); <span class="cm-comment">// should == 4</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageItemCount</span>(<span class="cm-number">1</span>); <span class="cm-comment">// last page - should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageItemCount</span>(<span class="cm-number">2</span>); <span class="cm-comment">// should == -1 since the page is invalid</span>

<span class="cm-comment">// pageIndex takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageIndex</span>(<span class="cm-number">5</span>); <span class="cm-comment">// should == 1 (zero based index)</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageIndex</span>(<span class="cm-number">2</span>); <span class="cm-comment">// should == 0</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageIndex</span>(<span class="cm-number">20</span>); <span class="cm-comment">// should == -1</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageIndex</span>(<span class="cm-operator">-</span><span class="cm-number">10</span>); <span class="cm-comment">// should == -1</span>
</code></pre>
<pre style="display: none;"><code class="language-coffeescript"><span class="cm-variable">helper</span> <span class="cm-punctuation">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">PaginationHelper</span><span class="cm-punctuation">(</span><span class="cm-punctuation">[</span><span class="cm-string">'a'</span><span class="cm-punctuation">,</span><span class="cm-string">'b'</span><span class="cm-punctuation">,</span><span class="cm-string">'c'</span><span class="cm-punctuation">,</span><span class="cm-string">'d'</span><span class="cm-punctuation">,</span><span class="cm-string">'e'</span><span class="cm-punctuation">,</span><span class="cm-string">'f'</span><span class="cm-punctuation">]</span><span class="cm-punctuation">,</span> <span class="cm-number">4</span><span class="cm-punctuation">)</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">pageCount</span><span class="cm-punctuation">(</span><span class="cm-punctuation">)</span> <span class="cm-comment"># should == 2</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">itemCount</span><span class="cm-punctuation">(</span><span class="cm-punctuation">)</span> <span class="cm-comment"># should == 6</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">pageItemCount</span><span class="cm-punctuation">(</span><span class="cm-number">0</span><span class="cm-punctuation">)</span> <span class="cm-comment"># should == 4</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">pageItemCount</span><span class="cm-punctuation">(</span><span class="cm-number">1</span><span class="cm-punctuation">)</span> <span class="cm-comment"># last page - should == 2</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">pageItemCount</span><span class="cm-punctuation">(</span><span class="cm-number">2</span><span class="cm-punctuation">)</span> <span class="cm-comment"># should == -1 since the page is invalid</span>

<span class="cm-comment"># pageIndex takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">pageIndex</span><span class="cm-punctuation">(</span><span class="cm-number">5</span><span class="cm-punctuation">)</span> <span class="cm-comment"># should == 1 (zero based index)</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">pageIndex</span><span class="cm-punctuation">(</span><span class="cm-number">2</span><span class="cm-punctuation">)</span> <span class="cm-comment"># should == 0</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">pageIndex</span><span class="cm-punctuation">(</span><span class="cm-number">20</span><span class="cm-punctuation">)</span> <span class="cm-comment"># should == -1</span>
<span class="cm-variable">helper</span><span class="cm-punctuation">.</span><span class="cm-property">pageIndex</span><span class="cm-punctuation">(</span><span class="cm-number">-10</span><span class="cm-punctuation">)</span> <span class="cm-comment"># should == -1</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">helper</span> <span class="cm-operator">=</span> <span class="cm-tag">PaginationHelper</span><span class="cm-operator">.</span><span class="cm-property">new</span>([<span class="cm-string">'a'</span>,<span class="cm-string">'b'</span>,<span class="cm-string">'c'</span>,<span class="cm-string">'d'</span>,<span class="cm-string">'e'</span>,<span class="cm-string">'f'</span>], <span class="cm-number">4</span>)
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_count</span>() <span class="cm-comment"># should == 2</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">item_count</span>() <span class="cm-comment"># should == 6</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_item_count</span>(<span class="cm-number">0</span>) <span class="cm-comment"># should == 4</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_item_count</span>(<span class="cm-number">1</span>) <span class="cm-comment"># last page - should == 2</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_item_count</span>(<span class="cm-number">2</span>) <span class="cm-comment"># should == -1 since the page is invalid</span>

<span class="cm-comment"># page_index takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_index</span>(<span class="cm-number">5</span>) <span class="cm-comment"># should == 1 (zero based index)</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_index</span>(<span class="cm-number">2</span>) <span class="cm-comment"># should == 0</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_index</span>(<span class="cm-number">20</span>) <span class="cm-comment"># should == -1</span>
<span class="cm-variable">helper</span><span class="cm-operator">.</span><span class="cm-property">page_index</span>(<span class="cm-operator">-</span><span class="cm-number">10</span>) <span class="cm-comment"># should == -1 because negative indexes are invalid</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">collection</span>   <span class="cm-keyword">=</span> [<span class="cm-string">'a'</span>,<span class="cm-string">'b'</span>,<span class="cm-string">'c'</span>,<span class="cm-string">'d'</span>,<span class="cm-string">'e'</span>,<span class="cm-string">'f'</span>]
<span class="cm-variable">itemsPerPage</span> <span class="cm-keyword">=</span> <span class="cm-number">4</span>

<span class="cm-variable">pageCount</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span>       `<span class="cm-variable">shouldBe</span>` <span class="cm-number">2</span>
<span class="cm-variable">itemCount</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span>       `<span class="cm-variable">shouldBe</span>` <span class="cm-number">6</span>

<span class="cm-variable">pageItemCount</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span> <span class="cm-number">0</span> `<span class="cm-variable">shouldBe</span>` <span class="cm-builtin">Just</span> <span class="cm-number">4</span> <span class="cm-comment">-- four of six items</span>
<span class="cm-variable">pageItemCount</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span> <span class="cm-number">1</span> `<span class="cm-variable">shouldBe</span>` <span class="cm-builtin">Just</span> <span class="cm-number">2</span> <span class="cm-comment">-- the last two items</span>
<span class="cm-variable">pageItemCount</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span> <span class="cm-number">3</span> `<span class="cm-variable">shouldBe</span>` <span class="cm-builtin">Nothing</span> <span class="cm-comment">-- page doesn't exist</span>

<span class="cm-variable">pageIndex</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span>  <span class="cm-number">0</span>    `<span class="cm-variable">shouldBe</span>` <span class="cm-builtin">Just</span> <span class="cm-number">0</span> <span class="cm-comment">-- zero based index</span>
<span class="cm-variable">pageIndex</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span>  <span class="cm-number">5</span>    `<span class="cm-variable">shouldBe</span>` <span class="cm-builtin">Just</span> <span class="cm-number">1</span> 
<span class="cm-variable">pageIndex</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span> <span class="cm-number">20</span>    `<span class="cm-variable">shouldBe</span>` <span class="cm-builtin">Nothing</span>
<span class="cm-variable">pageIndex</span> <span class="cm-variable">collection</span> <span class="cm-variable">itemsPerPage</span> (<span class="cm-builtin">-</span><span class="cm-number">20</span>) `<span class="cm-variable">shouldBe</span>` <span class="cm-builtin">Nothing</span>
</code></pre>
<pre style="display: none;"><code class="language-python"><span class="cm-variable">helper</span> <span class="cm-operator">=</span> <span class="cm-variable">PaginationHelper</span>([<span class="cm-string">'a'</span>,<span class="cm-string">'b'</span>,<span class="cm-string">'c'</span>,<span class="cm-string">'d'</span>,<span class="cm-string">'e'</span>,<span class="cm-string">'f'</span>], <span class="cm-number">4</span>)
<span class="cm-variable">helper</span>.<span class="cm-property">page_count</span>() <span class="cm-comment"># should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-property">item_count</span>() <span class="cm-comment"># should == 6</span>
<span class="cm-variable">helper</span>.<span class="cm-property">page_item_count</span>(<span class="cm-number">0</span>) <span class="cm-comment"># should == 4</span>
<span class="cm-variable">helper</span>.<span class="cm-property">page_item_count</span>(<span class="cm-number">1</span>) <span class="cm-comment"># last page - should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-property">page_item_count</span>(<span class="cm-number">2</span>) <span class="cm-comment"># should == -1 since the page is invalid</span>

<span class="cm-comment"># page_index takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span>.<span class="cm-property">page_index</span>(<span class="cm-number">5</span>) <span class="cm-comment"># should == 1 (zero based index)</span>
<span class="cm-variable">helper</span>.<span class="cm-property">page_index</span>(<span class="cm-number">2</span>) <span class="cm-comment"># should == 0</span>
<span class="cm-variable">helper</span>.<span class="cm-property">page_index</span>(<span class="cm-number">20</span>) <span class="cm-comment"># should == -1</span>
<span class="cm-variable">helper</span>.<span class="cm-property">page_index</span>(<span class="cm-operator">-</span><span class="cm-number">10</span>) <span class="cm-comment"># should == -1 because negative indexes are invalid</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-keyword">var</span> <span class="cm-def">helper</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">PaginationHelper</span><span class="cm-operator">&lt;</span><span class="cm-type">char</span><span class="cm-operator">&gt;</span>(<span class="cm-keyword">new</span> <span class="cm-variable">List</span><span class="cm-operator">&lt;</span><span class="cm-type">char</span><span class="cm-operator">&gt;</span>{<span class="cm-string">'a'</span>, <span class="cm-string">'b'</span>, <span class="cm-string">'c'</span>, <span class="cm-string">'d'</span>, <span class="cm-string">'e'</span>, <span class="cm-string">'f'</span>}, <span class="cm-number">4</span>);
<span class="cm-variable">helper</span>.<span class="cm-variable">PageCount</span>; <span class="cm-comment">// should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">ItemCount</span>; <span class="cm-comment">// should == 6</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">PageItemCount</span>(<span class="cm-number">0</span>); <span class="cm-comment">// should == 4</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">PageItemCount</span>(<span class="cm-number">1</span>); <span class="cm-comment">// last page - should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">PageItemCount</span>(<span class="cm-number">2</span>); <span class="cm-comment">// should == -1 since the page is invalid</span>

<span class="cm-comment">// pageIndex takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">PageIndex</span>(<span class="cm-number">5</span>); <span class="cm-comment">// should == 1 (zero based index)</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">PageIndex</span>(<span class="cm-number">2</span>); <span class="cm-comment">// should == 0</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">PageIndex</span>(<span class="cm-number">20</span>); <span class="cm-comment">// should == -1</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">PageIndex</span>(<span class="cm-operator">-</span><span class="cm-number">10</span>); <span class="cm-comment">// should == -1</span>
</code></pre>
<pre style="display: none;"><code class="language-kotlin"><span class="cm-keyword">val</span> <span class="cm-def">helper</span> <span class="cm-operator">=</span> <span class="cm-variable">PaginationHelper</span><span class="cm-operator">&lt;</span><span class="cm-type">Char</span><span class="cm-operator">&gt;</span>(<span class="cm-variable">listOf</span>(<span class="cm-string">'a'</span>, <span class="cm-string">'b'</span>, <span class="cm-string">'c'</span>, <span class="cm-string">'d'</span>, <span class="cm-string">'e'</span>, <span class="cm-string">'f'</span>), <span class="cm-number">4</span>)
<span class="cm-variable">helper</span>.<span class="cm-variable">pageCount</span> <span class="cm-comment">// should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">itemCount</span> <span class="cm-comment">// should == 6</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageItemCount</span>(<span class="cm-number">0</span>) <span class="cm-comment">// should == 4</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageItemCount</span>(<span class="cm-number">1</span>) <span class="cm-comment">// last page - should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageItemCount</span>(<span class="cm-number">2</span>) <span class="cm-comment">// should == -1 since the page is invalid</span>

<span class="cm-comment">// pageIndex takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageIndex</span>(<span class="cm-number">5</span>) <span class="cm-comment">// should == 1 (zero based index)</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageIndex</span>(<span class="cm-number">2</span>) <span class="cm-comment">// should == 0</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageIndex</span>(<span class="cm-number">20</span>) <span class="cm-comment">// should == -1</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">pageIndex</span>(<span class="cm-operator">-</span><span class="cm-number">10</span>) <span class="cm-comment">// should == -1</span>
</code></pre>
<pre style="display: none;"><code class="language-typescript"><span class="cm-keyword">let</span> <span class="cm-def">helper</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">PaginationHelper</span>([<span class="cm-string">"a"</span>, <span class="cm-string">"b"</span>, <span class="cm-string">"c"</span>, <span class="cm-string">"d"</span>, <span class="cm-string">"e"</span>, <span class="cm-string">"f"</span>], <span class="cm-number">4</span>)
<span class="cm-variable">helper</span>.<span class="cm-property">pageCount</span>() <span class="cm-comment">// should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-property">itemCount</span>() <span class="cm-comment">// should == 6</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageItemCount</span>(<span class="cm-number">0</span>) <span class="cm-comment">// should == 4</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageItemCount</span>(<span class="cm-number">1</span>) <span class="cm-comment">// last page - should == 2</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageItemCount</span>(<span class="cm-number">2</span>) <span class="cm-comment">// should == -1 since the page is invalid</span>

<span class="cm-comment">// pageIndex takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageIndex</span>(<span class="cm-number">5</span>) <span class="cm-comment">// should == 1 (zero based index)</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageIndex</span>(<span class="cm-number">2</span>) <span class="cm-comment">// should == 0</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageIndex</span>(<span class="cm-number">20</span>) <span class="cm-comment">// should == -1</span>
<span class="cm-variable">helper</span>.<span class="cm-property">pageIndex</span>(<span class="cm-operator">-</span><span class="cm-number">10</span>) <span class="cm-comment">// should == -1</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-keyword">let</span> <span class="cm-def">helper</span> <span class="cm-operator">=</span> <span class="cm-variable">PaginationHelper</span>::<span class="cm-variable">new</span>(<span class="cm-variable-3">vec!</span>[<span class="cm-string-2">'a'</span>, <span class="cm-string-2">'b'</span>, <span class="cm-string-2">'c'</span>, <span class="cm-string-2">'d'</span>, <span class="cm-string-2">'e'</span>, <span class="cm-string-2">'f'</span>], <span class="cm-number">4</span>);
<span class="cm-variable">helper</span>.<span class="cm-variable">page_count</span>() <span class="cm-comment">// should be 2</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">item_count</span>() <span class="cm-comment">// should be 6</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">page_item_count</span>(<span class="cm-number">0</span>) <span class="cm-comment">// should be Some(4)</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">page_item_count</span>(<span class="cm-number">1</span>) <span class="cm-comment">// should be Some(2) (last page)</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">page_item_count</span>(<span class="cm-number">2</span>) <span class="cm-comment">// should be None (since the page is invalid)</span>

<span class="cm-comment">// page_index takes an item index and returns the page that it belongs on</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">page_index</span>(<span class="cm-number">5</span>) <span class="cm-comment">// should be Some(1) (zero based index)</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">page_index</span>(<span class="cm-number">2</span>) <span class="cm-comment">// should be Some(0)</span>
<span class="cm-variable">helper</span>.<span class="cm-variable">page_index</span>(<span class="cm-number">20</span>) <span class="cm-comment">// should be None (since the item is invalid)</span>
</code></pre>

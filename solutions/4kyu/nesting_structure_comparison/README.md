<p>Complete the function/method (depending on the language) to return <code>true</code>/<code>True</code> when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.</p>
<p>For example:</p>
<pre style="display: none;"><code class="language-javascript"> <span class="cm-comment">// should return true</span>
[ <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span> ].<span class="cm-property">sameStructureAs</span>( [ <span class="cm-number">2</span>, <span class="cm-number">2</span>, <span class="cm-number">2</span> ] );          
[ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ].<span class="cm-property">sameStructureAs</span>( [ <span class="cm-number">2</span>, [ <span class="cm-number">2</span>, <span class="cm-number">2</span> ] ] );  

 <span class="cm-comment">// should return false </span>
[ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ].<span class="cm-property">sameStructureAs</span>( [ [ <span class="cm-number">2</span>, <span class="cm-number">2</span> ], <span class="cm-number">2</span> ] );  
[ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ].<span class="cm-property">sameStructureAs</span>( [ [ <span class="cm-number">2</span> ], <span class="cm-number">2</span> ] );  

<span class="cm-comment">// should return true</span>
[ [ [ ], [ ] ] ].<span class="cm-property">sameStructureAs</span>( [ [ [ ], [ ] ] ] ); 

<span class="cm-comment">// should return false</span>
[ [ [ ], [ ] ] ].<span class="cm-property">sameStructureAs</span>( [ [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ] );     
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">same_structure_as</span>([<span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span>], [<span class="cm-number">2</span>, <span class="cm-number">2</span>, <span class="cm-number">2</span>]); <span class="cm-comment">// =&gt; true</span>
<span class="cm-variable">same_structure_as</span>([<span class="cm-number">1</span>, [<span class="cm-number">1</span>, <span class="cm-number">1</span>]], [<span class="cm-number">2</span>, [<span class="cm-number">2</span>, <span class="cm-number">2</span>]]); <span class="cm-comment">// =&gt; true</span>
<span class="cm-variable">same_structure_as</span>([<span class="cm-number">1</span>, [<span class="cm-number">1</span>, <span class="cm-number">1</span>]], [[<span class="cm-number">2</span>, <span class="cm-number">2</span>], <span class="cm-number">2</span>]); <span class="cm-comment">// =&gt; false</span>
<span class="cm-variable">same_structure_as</span>([<span class="cm-number">1</span>, [<span class="cm-number">1</span>, <span class="cm-number">1</span>]], [[<span class="cm-number">2</span>], <span class="cm-number">2</span>]); <span class="cm-comment">// =&gt; false</span>
<span class="cm-variable">same_structure_as</span>([[[], []]], [[[], []]]); <span class="cm-comment">// =&gt; true</span>
<span class="cm-variable">same_structure_as</span>([[[], []]], [[<span class="cm-number">1</span>, <span class="cm-number">1</span>]]); <span class="cm-comment">// =&gt; false</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-comment"># should return true</span>
[ <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span> ]<span class="cm-operator">.</span><span class="cm-property">same_structure_as</span>( [ <span class="cm-number">2</span>, <span class="cm-number">2</span>, <span class="cm-number">2</span> ] )
[ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ]<span class="cm-operator">.</span><span class="cm-property">same_structure_as</span>( [ <span class="cm-number">2</span>, [ <span class="cm-number">2</span>, <span class="cm-number">2</span> ] ] )

<span class="cm-comment"># should return false </span>
[ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ]<span class="cm-operator">.</span><span class="cm-property">same_structure_as</span>( [ [ <span class="cm-number">2</span>, <span class="cm-number">2</span> ], <span class="cm-number">2</span> ] )
[ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ]<span class="cm-operator">.</span><span class="cm-property">same_structure_as</span>( [ [ <span class="cm-number">2</span> ], <span class="cm-number">2</span> ] )

<span class="cm-comment"># should return true</span>
[ [ [ ], [ ] ] ]<span class="cm-operator">.</span><span class="cm-property">same_structure_as</span>( [ [ [ ], [ ] ] ] ); 

<span class="cm-comment"># should return false</span>
[ [ [ ], [ ] ] ]<span class="cm-operator">.</span><span class="cm-property">same_structure_as</span>( [ [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ] )   
</code></pre>
<pre><code class="language-python"><span class="cm-comment"># should return True</span>
<span class="cm-variable">same_structure_as</span>([ <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span> ], [ <span class="cm-number">2</span>, <span class="cm-number">2</span>, <span class="cm-number">2</span> ] )
<span class="cm-variable">same_structure_as</span>([ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ], [ <span class="cm-number">2</span>, [ <span class="cm-number">2</span>, <span class="cm-number">2</span> ] ] )

<span class="cm-comment"># should return False </span>
<span class="cm-variable">same_structure_as</span>([ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ], [ [ <span class="cm-number">2</span>, <span class="cm-number">2</span> ], <span class="cm-number">2</span> ] )
<span class="cm-variable">same_structure_as</span>([ <span class="cm-number">1</span>, [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ], [ [ <span class="cm-number">2</span> ], <span class="cm-number">2</span> ] )

<span class="cm-comment"># should return True</span>
<span class="cm-variable">same_structure_as</span>([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

<span class="cm-comment"># should return False</span>
<span class="cm-variable">same_structure_as</span>([ [ [ ], [ ] ] ], [ [ <span class="cm-number">1</span>, <span class="cm-number">1</span> ] ] )
</code></pre>

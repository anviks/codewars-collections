<p>Write a function called <code>sumIntervals</code>/<code>sum_intervals</code> that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.</p>
<h3 id="intervals">Intervals</h3>
<p>Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: <code>[1, 5]</code> is an interval from <code>1</code> to <code>5</code>. The length of this interval is <code>4</code>.</p>
<h3 id="overlapping-intervals">Overlapping Intervals</h3>
<p>List containing overlapping intervals:</p>
<pre><code class="language-c">[
   [<span class="cm-number">1</span>, <span class="cm-number">4</span>],
   [<span class="cm-number">7</span>, <span class="cm-number">10</span>],
   [<span class="cm-number">3</span>, <span class="cm-number">5</span>]
]
</code></pre>
<p>The sum of the lengths of these intervals is <code>7</code>. Since <code>[1, 4]</code> and <code>[3, 5]</code> overlap, we can treat the interval as <code>[1, 5]</code>, which has a length of <code>4</code>.</p>
<h3 id="examples">Examples:</h3>
<pre><code class="language-c"><span class="cm-variable">sumIntervals</span>( [
   [<span class="cm-number">1</span>, <span class="cm-number">2</span>],
   [<span class="cm-number">6</span>, <span class="cm-number">10</span>],
   [<span class="cm-number">11</span>, <span class="cm-number">15</span>]
] ) <span class="cm-operator">=&gt;</span> <span class="cm-number">9</span>

<span class="cm-variable">sumIntervals</span>( [
   [<span class="cm-number">1</span>, <span class="cm-number">4</span>],
   [<span class="cm-number">7</span>, <span class="cm-number">10</span>],
   [<span class="cm-number">3</span>, <span class="cm-number">5</span>]
] ) <span class="cm-operator">=&gt;</span> <span class="cm-number">7</span>

<span class="cm-variable">sumIntervals</span>( [
   [<span class="cm-number">1</span>, <span class="cm-number">5</span>],
   [<span class="cm-number">10</span>, <span class="cm-number">20</span>],
   [<span class="cm-number">1</span>, <span class="cm-number">6</span>],
   [<span class="cm-number">16</span>, <span class="cm-number">19</span>],
   [<span class="cm-number">5</span>, <span class="cm-number">11</span>]
] ) <span class="cm-operator">=&gt;</span> <span class="cm-number">19</span>

<span class="cm-variable">sumIntervals</span>( [
   [<span class="cm-number">0</span>, <span class="cm-number">20</span>],
   [<span class="cm-operator">-</span><span class="cm-number">100000000</span>, <span class="cm-number">10</span>],
   [<span class="cm-number">30</span>, <span class="cm-number">40</span>]
] ) <span class="cm-operator">=&gt;</span> <span class="cm-number">100000030</span>
</code></pre>
<h3 id="tests-with-large-intervals">Tests with large intervals</h3>
<p>Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range <code>[-1000000000, 1000000000]</code>.</p>

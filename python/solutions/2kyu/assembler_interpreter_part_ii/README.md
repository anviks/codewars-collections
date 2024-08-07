<p>This is the second part of this kata series. First part is <a href="https://www.codewars.com/kata/simple-assembler-interpreter/" data-turbolinks="false" target="_blank">here</a>.</p>
<p>We want to create an interpreter of assembler which will support the following instructions:</p>
<ul>
<li><code>mov x, y</code> - copy y (either an integer or the value of a register) into register x.</li>
<li><code>inc x</code> - increase the content of register x by one.</li>
<li><code>dec x</code> - decrease the content of register x by one.</li>
<li><code>add x, y</code> - add the content of the register x with y (either an integer or the value of a register) and stores the result in x (i.e. register[x] += y).</li>
<li><code>sub x, y</code> - subtract y (either an integer or the value of a register) from the register x and stores the result in x (i.e. register[x] -= y).</li>
<li><code>mul x, y</code> - same with multiply (i.e. register[x] *= y).</li>
<li><code>div x, y</code> - same with integer division (i.e. register[x] /= y).</li>
<li><code>label:</code> - define a label position (<code>label = identifier + ":"</code>, an identifier being a string that does not match any other command). Jump commands and <code>call</code> are aimed to these labels positions in the program.</li>
<li><code>jmp lbl</code> - jumps to the label <code>lbl</code>.</li>
<li><code>cmp x, y</code> - compares x (either an integer or the value of a register) and y (either an integer or the value of a register). The result is used in the conditional jumps (<code>jne</code>, <code>je</code>, <code>jge</code>, <code>jg</code>, <code>jle</code> and <code>jl</code>)</li>
<li><code>jne lbl</code> - jump to the label <code>lbl</code> if the values of the previous <code>cmp</code> command were not equal.</li>
<li><code>je lbl</code> - jump to the label <code>lbl</code> if the values of the previous <code>cmp</code> command were equal.</li>
<li><code>jge lbl</code> - jump to the label <code>lbl</code> if x was greater or equal than y in the previous <code>cmp</code> command.</li>
<li><code>jg lbl</code> - jump to the label <code>lbl</code> if x was greater than y in the previous <code>cmp</code> command.</li>
<li><code>jle lbl</code> - jump to the label <code>lbl</code> if x was less or equal than y in the previous <code>cmp</code> command.</li>
<li><code>jl lbl</code> - jump to the label <code>lbl</code> if x was less than y in the previous <code>cmp</code> command.</li>
<li><code>call lbl</code> - call to the subroutine identified by <code>lbl</code>. When a <code>ret</code> is found in a subroutine, the instruction pointer should return to the instruction next to this <code>call</code> command.</li>
<li><code>ret</code> - when a <code>ret</code> is found in a subroutine, the instruction pointer should return to the instruction that called the current function.</li>
<li><code>msg 'Register: ', x</code> - this instruction stores the output of the program. It may contain text strings (delimited by single quotes) and registers. The number of arguments isn't limited and will vary, depending on the program.</li>
<li><code>end</code> - this instruction indicates that the program ends correctly, so the stored output is returned (if the program terminates without this instruction it should return the default output: see below).</li>
<li><code>; comment</code> - comments should not be taken in consideration during the execution of the program.</li>
</ul>
<br> 

<h2 id="output-format">Output format:</h2>
<p>The normal output format is a string (returned with the <code>end</code> command). For Scala and Rust programming languages it should be incapsulated into Option.</p>
<p>If the program does finish itself without using an <code>end</code> instruction, the default return value is:</p>
<pre><code class="language-python"><span class="cm-operator">-</span><span class="cm-number">1</span> (<span class="cm-keyword">as</span> <span class="cm-variable">an</span> <span class="cm-variable">integer</span>)
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-atom">null</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-atom">null</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-operator">-</span><span class="cm-number">1</span> (<span class="cm-variable">as</span> <span class="cm-variable">an</span> <span class="cm-variable">integer</span>)
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-string">"-1"</span> (<span class="cm-variable">as</span> <span class="cm-variable">a</span> <span class="cm-variable">string</span>)
</code></pre>
<pre style="display: none;"><code class="language-scala"><span class="cm-variable">None</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-builtin">None</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-builtin">Nothing</span>
</code></pre>
<pre style="display: none;"><code class="language-cobol">          result <span class="cm-builtin">=</span> <span class="cm-string">'</span><span class="cm-string">-1'</span> 
</code></pre>
<br> 

<h2 id="input-format">Input format:</h2>
<p>The function/method will take as input a multiline string of instructions, delimited with EOL characters. Please, note that the instructions may also have indentation for readability purposes.</p>
<p>For example:</p>
<pre><code class="language-python"><span class="cm-variable">program</span> <span class="cm-operator">=</span> <span class="cm-string">"""</span>
<span class="cm-string">; My first program</span>
<span class="cm-string">mov  a, 5</span>
<span class="cm-string">inc  a</span>
<span class="cm-string">call function</span>
<span class="cm-string">msg  '(5+1)/2 = ', a    ; output message</span>
<span class="cm-string">end</span>

<span class="cm-string">function:</span>
<span class="cm-string">    div  a, 2</span>
<span class="cm-string">    ret</span>
<span class="cm-string">"""</span>
<span class="cm-variable">assembler_interpreter</span>(<span class="cm-variable">program</span>)
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">program</span> <span class="cm-operator">=</span> <span class="cm-string">"\n; My first program\nmov  a, 5\ninc  a\ncall function\nmsg  '(5+1)/2 = ', a    ; output message\nend\n\nfunction:\n    div  a, 2\n    ret\n"</span>
<span class="cm-variable">AssemblerInterpreter</span>.<span class="cm-variable">interpret</span>(<span class="cm-variable">program</span>);

<span class="cm-comment">// Which is equivalent to (keep in mind that empty lines are not displayed in the console on CW, so you actually won't see the separation before "function:"...):</span>

; <span class="cm-variable">My</span> <span class="cm-variable">first</span> <span class="cm-variable">program</span>
<span class="cm-variable">mov</span>  <span class="cm-variable">a</span>, <span class="cm-number">5</span>
<span class="cm-variable">inc</span>  <span class="cm-variable">a</span>
<span class="cm-variable">call</span> <span class="cm-variable">function</span>
<span class="cm-variable">msg</span>  <span class="cm-string">'(5+1)/2 = '</span>, <span class="cm-variable">a</span>    ; <span class="cm-variable">output</span> <span class="cm-variable">message</span>
<span class="cm-variable">end</span>

<span class="cm-variable">function</span>:
    <span class="cm-variable">div</span>  <span class="cm-variable">a</span>, <span class="cm-number">2</span>
    <span class="cm-variable">ret</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">program</span> <span class="cm-operator">=</span> <span class="cm-string">"\n; My first program\nmov  a, 5\ninc  a\ncall function\nmsg  '(5+1)/2 = ', a    ; output message\nend\n\nfunction:\n    div  a, 2\n    ret\n"</span>
<span class="cm-variable">AssemblerInterpreter</span>.<span class="cm-variable">Interpret</span>(<span class="cm-variable">program</span>);

<span class="cm-comment">// Which is equivalent to (keep in mind that empty lines are not displayed in the console on CW, so you actually won't see the separation before "function:"...):</span>

; <span class="cm-variable">My</span> <span class="cm-variable">first</span> <span class="cm-variable">program</span>
<span class="cm-variable">mov</span>  <span class="cm-variable">a</span>, <span class="cm-number">5</span>
<span class="cm-variable">inc</span>  <span class="cm-variable">a</span>
<span class="cm-variable">call</span> <span class="cm-variable">function</span>
<span class="cm-variable">msg</span>  <span class="cm-string">'(5+1)/2 = '</span>, <span class="cm-variable">a</span>    ; <span class="cm-variable">output</span> <span class="cm-variable">message</span>
<span class="cm-variable">end</span>

<span class="cm-variable">function</span>:
    <span class="cm-variable">div</span>  <span class="cm-variable">a</span>, <span class="cm-number">2</span>
    <span class="cm-variable">ret</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">program</span> <span class="cm-operator">=</span> <span class="cm-string">"</span>
<span class="cm-string">; My first program</span>
<span class="cm-string">mov  a, 5</span>
<span class="cm-string">inc  a</span>
<span class="cm-string">call function</span>
<span class="cm-string">msg  '(5+1)/2 = ', a    ; output message</span>
<span class="cm-string">end</span>

<span class="cm-string">function:</span>
<span class="cm-string">    div  a, 2</span>
<span class="cm-string">    ret</span>
<span class="cm-string">"</span>
<span class="cm-variable">assembler_interpreter</span>(<span class="cm-variable">program</span>)
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-variable">program</span> <span class="cm-operator">=</span> <span class="cm-string">R"(</span>
<span class="cm-string">; My first program</span>
<span class="cm-string">mov  a, 5</span>
<span class="cm-string">inc  a</span>
<span class="cm-string">call function</span>
<span class="cm-string">msg  '(5+1)/2 = ', a    ; output message</span>
<span class="cm-string">end</span>

<span class="cm-string">function:</span>
    <span class="cm-string">div  a, 2</span>
    <span class="cm-string">ret)"</span>;
<span class="cm-variable">assembler_interpreter</span>(<span class="cm-variable">program</span>);
</code></pre>
<pre style="display: none;"><code class="language-scala"><span class="cm-keyword">val</span> <span class="cm-def">program</span> <span class="cm-operator">=</span> <span class="cm-string">"\n; My first program\nmov  a, 5\ninc  a\ncall function\nmsg  '(5+1)/2 = ', a    ; output message\nend\n\nfunction:\n    div  a, 2\n    ret\n"</span>
<span class="cm-variable">AssemblerInterpreter</span>.<span class="cm-variable">interpret</span>(<span class="cm-variable">program</span>);

<span class="cm-comment">// Which is equivalent to (keep in mind that empty lines are not displayed in the console on CW, so you actually won't see the separation before "function:"...):</span>

; <span class="cm-variable">My</span> <span class="cm-variable">first</span> <span class="cm-variable">program</span>
<span class="cm-variable">mov</span>  <span class="cm-variable">a</span>, <span class="cm-number">5</span>
<span class="cm-variable">inc</span>  <span class="cm-variable">a</span>
<span class="cm-variable">call</span> <span class="cm-variable">function</span>
<span class="cm-variable">msg</span>  <span class="cm-atom">'</span>(<span class="cm-number">5</span><span class="cm-operator">+</span><span class="cm-number">1</span>)<span class="cm-operator">/</span><span class="cm-number">2</span> <span class="cm-operator">=</span> <span class="cm-atom">'</span>, <span class="cm-variable">a</span>    ; <span class="cm-variable">output</span> <span class="cm-variable">message</span>
<span class="cm-variable">end</span>

<span class="cm-variable">function</span>:
    <span class="cm-variable">div</span>  <span class="cm-variable">a</span>, <span class="cm-number">2</span>
    <span class="cm-variable">ret</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-keyword">let</span> <span class="cm-def">program</span> <span class="cm-operator">=</span> <span class="cm-string">"</span><span class="cm-string">\n; My first program\nmov  a, 5\ninc  a\ncall function\nmsg  '(5+1)/2 = ', a    ; output message\nend\n\nfunction:\n    div  a, 2\n    ret\n</span><span class="cm-string">"</span>;
<span class="cm-variable">AssemblerInterpreter</span>::<span class="cm-variable">interpret</span>(<span class="cm-variable">program</span>);

<span class="cm-comment">// Which is equivalent to (keep in mind that empty lines are not displayed in the console on CW, so you actually won't see the separation before "function:"...):</span>

; <span class="cm-variable">My</span> <span class="cm-variable">first</span> <span class="cm-variable">program</span>
<span class="cm-variable">mov</span>  <span class="cm-variable">a</span>, <span class="cm-number">5</span>
<span class="cm-variable">inc</span>  <span class="cm-variable">a</span>
<span class="cm-variable">call</span> <span class="cm-variable">function</span>
<span class="cm-variable">msg</span>  '(<span class="cm-number">5</span><span class="cm-operator">+</span><span class="cm-number">1</span>)<span class="cm-operator">/</span><span class="cm-number">2</span> <span class="cm-operator">=</span> ', <span class="cm-variable">a</span>    ; <span class="cm-variable">output</span> <span class="cm-variable">message</span>
<span class="cm-variable">end</span>

<span class="cm-variable">function</span>:
    <span class="cm-variable">div</span>  <span class="cm-variable">a</span>, <span class="cm-number">2</span>
    <span class="cm-variable">ret</span>
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">program</span> <span class="cm-keyword">=</span> <span class="cm-string">"\n; My first program\nmov  a, 5\ninc  a\ncall function\nmsg  '(5+1)/2 = ', a    ; output message\nend\n\nfunction:\n    div  a, 2\n    ret\n"</span>
<span class="cm-variable">interpret</span> <span class="cm-variable">program</span>
</code></pre>
<pre style="display: none;"><code class="language-cobol">      <span class="cm-comment">* COBOL has no symbol for EOL literal, if you display the program string</span>
      <span class="cm-comment">* to the console, you will see something similar to this:</span>
      <span class="cm-string">"</span><span class="cm-string">; My first program</span>
      <span class="cm-string">mov  a, 5</span>
      <span class="cm-string">inc  a</span>
      <span class="cm-string">call function</span>
      <span class="cm-string">msg  '</span>(<span class="cm-number">5</span><span class="cm-number">+1</span>)<span class="cm-builtin">/</span><span class="cm-number">2</span> <span class="cm-builtin">=</span> <span class="cm-string">'</span><span class="cm-string">, a    ; output message</span>
      <span class="cm-string">end</span>

      <span class="cm-string">function:</span>
          <span class="cm-string">div  a, 2</span>
          <span class="cm-string">ret"</span>

      <span class="cm-comment">* EOL character (line feed) is ascii character 10 (`function char(11)` in COBOL)</span>
</code></pre>
<p>The above code would set register <code>a</code> to 5, increase its value by 1, calls the subroutine function, divide its value by 2, returns to the first call instruction, prepares the output of the program and then returns it with the <code>end</code> instruction. In this case, the output would be <code>(5+1)/2 = 3</code>.</p>

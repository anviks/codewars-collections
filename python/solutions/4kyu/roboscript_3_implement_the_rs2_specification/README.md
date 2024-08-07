<h1 id="roboscript-3---implement-the-rs2-specification">RoboScript #3 - Implement the RS2 Specification</h1>
<h2 id="disclaimer">Disclaimer</h2>
<p>The story presented in this Kata Series is purely fictional; any resemblance to actual programming languages, products, organisations or people should be treated as purely coincidental.</p>
<h2 id="about-this-kata-series">About this Kata Series</h2>
<p>This Kata Series is based on a fictional story about a computer scientist and engineer who owns a firm that sells a toy robot called MyRobot which can interpret its own (esoteric) programming language called RoboScript.  Naturally, this Kata Series deals with the software side of things (I'm afraid Codewars cannot test your ability to build a physical robot!).</p>
<h2 id="story">Story</h2>
<p>Last time, you implemented the RS1 specification which allowed your customers to write more concise scripts for their robots by allowing them to simplify consecutive repeated commands by postfixing a non-negative integer onto the selected command.  For example, if your customers wanted to make their robot move 20 steps to the right, instead of typing <code>FFFFFFFFFFFFFFFFFFFF</code>, they could simply type <code>F20</code> which made their scripts more concise.  However, you later realised that this simplification wasn't enough.  What if a set of commands/moves were to be repeated?  The code would still appear cumbersome.  Take the program that makes the robot move in a snake-like manner, for example.  The shortened code for it was <code>F4LF4RF4RF4LF4LF4RF4RF4LF4LF4RF4RF4</code> which still contained a lot of repeated commands.</p>
<h2 id="task">Task</h2>
<p>Your task is to allow your customers to further shorten their scripts and make them even more concise by implementing the newest specification of RoboScript (at the time of writing) that is RS2.  RS2 syntax is a superset of RS1 syntax which means that all valid RS1 code from the previous Kata of this Series should still work with your RS2 interpreter.  The only main addition in RS2 is that the customer should be able to group certain sets of commands using round brackets.  For example, the last example used in the previous Kata in this Series:</p>
<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">LF5RF3RF3RF7
</pre> 

<p>... can be expressed in RS2 as:</p>
<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">LF5(RF3)(RF3R)F7
</pre>

<p>Or ... </p>
<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">(L(F5(RF3))(((R(F3R)F7))))
</pre>

<p>Simply put, your interpreter should be able to deal with nested brackets of any level.</p>
<p>And of course, brackets are useless if you cannot use them to repeat a sequence of movements!  Similar to how individual commands can be postfixed by a non-negative integer to specify how many times to repeat that command, a sequence of commands grouped by round brackets <code>()</code> should also be repeated <code>n</code> times provided a non-negative integer is postfixed onto the brackets, like such:</p>
<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">(SEQUENCE_OF_COMMANDS)n
</pre>

<p>... is equivalent to ... </p>
<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">SEQUENCE_OF_COMMANDS...SEQUENCE_OF_COMMANDS (repeatedly executed "n" times)
</pre>

<p>For example, this RS1 program:</p>
<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">F4LF4RF4RF4LF4LF4RF4RF4LF4LF4RF4RF4
</pre>

<p>... can be rewritten in RS2 as:</p>
<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">F4L(F4RF4RF4LF4L)2F4RF4RF4
</pre>

<p>Or:</p>
<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">F4L((F4R)2(F4L)2)2(F4R)2F4
</pre>

<p>All 4 example tests have been included for you.  Good luck :D</p>
<h2 id="kata-in-this-series">Kata in this Series</h2>
<ol>
<li><a href="https://www.codewars.com/kata/roboscript-number-1-implement-syntax-highlighting" data-turbolinks="false" target="_blank">RoboScript #1 - Implement Syntax Highlighting</a></li>
<li><a href="https://www.codewars.com/kata/roboscript-number-2-implement-the-rs1-specification" data-turbolinks="false" target="_blank">RoboScript #2 - Implement the RS1 Specification</a></li>
<li><strong>RoboScript #3 - Implement the RS2 Specification</strong></li>
<li><a href="https://www.codewars.com/kata/594b898169c1d644f900002e" data-turbolinks="false" target="_blank">RoboScript #4 - RS3 Patterns to the Rescue</a></li>
<li><a href="https://www.codewars.com/kata/5a12755832b8b956a9000133" data-turbolinks="false" target="_blank">RoboScript #5 - The Final Obstacle (Implement RSU)</a></li>
</ol>

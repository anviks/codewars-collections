# [RoboScript #4 - RS3 Patterns to the Rescue](https://www.codewars.com/kata/594b898169c1d644f900002e)

## Disclaimer

The story presented in this Kata Series is purely fictional; any resemblance to actual programming languages, products, organisations or people should be treated as purely coincidental.

## About this Kata Series

This Kata Series is based on a fictional story about a computer scientist and engineer who owns a firm that sells a toy robot called MyRobot which can interpret its own (esoteric) programming language called RoboScript.  Naturally, this Kata Series deals with the software side of things (I'm afraid Codewars cannot test your ability to build a physical robot!).

## Story

Ever since you released [RS2](https://www.codewars.com/kata/58738d518ec3b4bf95000192) to the market, there have been much fewer complaints from RoboScript developers about the inefficiency of the language and the popularity of your programming language has continuously soared.  It has even gained so much attention that Zachary Mikowski, the CEO of the world-famous Doodle search engine, has contacted you to try out your product!  Initially, when you explain the RoboScript (RS2) syntax to him, he looks satisfied, but then he soon finds a major loophole in the efficiency of the RS2 language and brings forth the following program:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
(F2LF2R)2FRF4L(F2LF2R)2(FRFL)4(F2LF2R)2
</pre> 

As you can see from the program above, the movement sequence `(F2LF2R)2` has to be rewritten every time and no amount of RS2 syntax can simplify it because the movement sequences in between are different each time (`FRF4L` and `(FRFL)4`).  If only RoboScript had a movement sequence reuse feature that makes writing programs like these less repetitive ... 

## Task

Define and implement the RS3 specification whose syntax is a superset of [RS2](https://www.codewars.com/kata/58738d518ec3b4bf95000192) (and RS1) syntax.  Your interpreter should be named `execute()` and accept exactly 1 argument `code`, the RoboScript code to be executed.

### Patterns - The New Feature

To solve the problem outlined in the Story above, you have decided to introduce a new syntax feature to RS3 called the "pattern".  The "pattern" as defined in RS3 behaves rather like a primitive version of functions/methods in other programming languages - it allows the programmer to define and name (to a certain extent) a certain sequence of movements which can be easily referenced and reused later instead of rewriting the whole thing.

The basic syntax for defining a pattern is as follows:


<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
p(n)&lt;CODE_HERE&gt;q
</pre> 



Where:

- `p` is a "keyword" that declares the beginning of a pattern definition (much like the `function` keyword in JavaScript or the `def` keyword in Python)
- `(n)` is any non-negative integer (without the round brackets) which acts as a unique identifier for the pattern (much like a function/method name)
- `<CODE_HERE>` is any valid RoboScript code (without the angled brackets)
- `q` is a "keyword" that marks the end of a pattern definition (like the `end` keyword in Ruby)

For example, if I want to define `(F2LF2R)2` as a pattern and reuse it later in my code:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
p0(F2LF2R)2q
</pre> 

It can also be rewritten as below since `(n)` only serves as an identifier and its value doesn't matter:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
p312(F2LF2R)2q
</pre>

Like function/method definitions in other languages, merely defining a pattern (or patterns) in RS3 should cause no side effects, so:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
execute("p0(F2LF2R)2q");   # => '*'
execute("p312(F2LF2R)2q"); # => '*'
</pre> 

To invoke a pattern (i.e. make the MyRobot move according to the movement sequences defined inside the pattern), a capital `P` followed by the pattern identifier `(n)` is used:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
P0
</pre> 

(or `P312`, depending on which example you are using)

So:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
execute("p0(F2LF2R)2qP0");     # => "    *\r\n    *\r\n  ***\r\n  *  \r\n***  "
execute("p312(F2LF2R)2qP312"); # => "    *\r\n    *\r\n  ***\r\n  *  \r\n***  "
</pre> 

### Additional Rules for parsing RS3

It doesn't matter whether the invocation of the pattern or the pattern definition comes first - pattern definitions should **always** be parsed first, so:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
execute("P0p0(F2LF2R)2q");     # => "    *\r\n    *\r\n  ***\r\n  *  \r\n***  "
execute("P312p312(F2LF2R)2q"); # => "    *\r\n    *\r\n  ***\r\n  *  \r\n***  "
</pre> 

Of course, RoboScript code can occur anywhere before and/or after a pattern definition/invocation, so:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
execute("F3P0Lp0(F2LF2R)2qF2"); # => "       *\r\n       *\r\n       *\r\n       *\r\n     ***\r\n     *  \r\n******  "
</pre>

Much like a function/definition can be invoked multiple times in other languages, a pattern should also be able to be invoked multiple times in RS3.  So:

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
execute("(P0)2p0F2LF2RqP0"); # => "      *\r\n      *\r\n    ***\r\n    *  \r\n  ***  \r\n  *    \r\n***    "
</pre>

If a pattern is invoked which does not exist, your interpreter should `throw`/`raise` an exception (depending on the language you are attempting this Kata in) of any kind.  This could be anything and will not be tested, but *ideally* it should provide a useful message which describes the error in detail.

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
execute("p0(F2LF2R)2qP1");   # throws
execute("P0p312(F2LF2R)2q"); # throws
execute("P312");             # throws
</pre>

Much like any good programming language will allow you to define an unlimited number of functions/methods, your RS3 interpreter should also allow the user to define a virtually unlimited number of patterns.  A pattern definition should be able to invoke other patterns if required.  If the same pattern (i.e. both containing the same identifier `(n)`) is defined more than once, your interpreter should `throw`/`raise` an exception (depending on the language you are attempting this Kata in) of any kind.

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
execute("P1P2p1F2Lqp2F2RqP2P1");                      # => "  ***\r\n  * *\r\n*** *"
execute("p1F2Lqp2F2Rqp3P1(P2)2P1q(P3)3");             # => "  *** *** ***\r\n  * * * * * *\r\n*** *** *** *"
execute("p1F2Lqp1(F3LF4R)5qp2F2Rqp3P1(P2)2P1q(P3)3"); # throws exception
</pre>

Furthermore, your interpreter should be able to detect (potentially) infinite recursion, including mutual recursion.  Instead of just getting stuck in an infinite loop and timing out, your interpreter should `throw`/`raise` an exception (depending on the language you are attempting this Kata in) of any kind when the "stack" (or just the total number of pattern invocations) exceeds a particular very high (but sensible) threshold, *but only if said pattern with infinite recursion is invoked at least once*.

<pre style="background: #161616; color: #c5c8c6; font-family: 'CamingoCode-Regular', monospace; display: block; padding: 10px; margin-bottom: 15px; font-weight: normal; overflow-x: auto">
execute("p1F2RP1F2LqP1");      # throws
execute("p1F2LP2qp2F2RP1qP1"); # throws
execute("p1F2RP1F2Lq");        # does not throw
</pre>

For the sake of simplicity, you may assume that all programs passed into your interpreter contains valid syntax.  Furthermore, nesting pattern definitions is not allowed either (it is considered a syntax error) so your interpreter will not need to account for these.

## Kata in this Series

1. [RoboScript #1 - Implement Syntax Highlighting](https://www.codewars.com/kata/roboscript-number-1-implement-syntax-highlighting)
2. [RoboScript #2 - Implement the RS1 Specification](https://www.codewars.com/kata/roboscript-number-2-implement-the-rs1-specification)
3. [RoboScript #3 - Implement the RS2 Specification](https://www.codewars.com/kata/58738d518ec3b4bf95000192)
4. **RoboScript #4 - RS3 Patterns to the Rescue**
5. [RoboScript #5 - The Final Obstacle (Implement RSU)](https://www.codewars.com/kata/5a12755832b8b956a9000133)
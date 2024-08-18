# [Haskell List  Dot Notation](https://www.codewars.com/kata/53c8b29750fe70e4a2000610)

I would like to mimic some of the amazing things Haskell can do with lists.

There are lots of things to do, so I'm going to break the work into several katas.

I'll warn you that perhaps you will have to refactor some parts of the code going forward, so you need to write the cleanest code possible.

Haskell lists are similar to JavaScript arrays.

For example, this is ok in both programming languages:



But Haskell allows you to define lists like this:



Or this way:



This is also valid:



A formal definition provided by [nivoliev](http://www.codewars.com/users/nivoliev):

* a list of individual elements : the resulting list is the list made of the individual elements as in classical Javascript
* a range in the form `start..end` : if `end >= start`, the list is `[start, start+1, start+2, ..., end]` otherwise the result is `[]`
* a single element a followed by a range : let `step = start - a`
  * if `start === end` the list is `[a,start]`
  * if step is positive and `end > start` then the list is `[a, a+step, a+2*step, ...]` as long as `a+k*step <= end`
  * if step is negative and end < start then the list is `[a, a+step, a+2*step, ...]` as long as `a-k*step >= end`
* otherwise the list is `[]`

Some clarifying examples:



Your work is to implement something like this in JavaScript.

With this purpose, I have defined the `ArrayComprehension` function.



The `options` parameter is an object with the `generator` key. The generator key is a string with list values:



It is assumed that the generator format is always right. Therefore, no need to check it.
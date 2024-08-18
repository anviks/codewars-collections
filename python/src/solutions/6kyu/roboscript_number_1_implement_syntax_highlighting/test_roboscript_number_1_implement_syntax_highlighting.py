"""https://www.codewars.com/kata/58708934a44cfccca60000c4"""

from solution_roboscript_number_1_implement_syntax_highlighting import *

message = 'Given Code: {}\n\nResults'


def test_your_syntax_highlighter__should_work_for_the_provided_examples():
    code = 'FFFR345F2LL'
    expected = '<span style="color: pink">FFF</span><span style="color: green">R</span><span style="color: orange">345</span><span style="color: pink">F</span><span style="color: orange">2</span><span style="color: red">LL</span>'
    assert highlight(code) == expected, message.format(code)
    print(f'Correct highlighting: {expected}\nYour highlighting:    {highlight(code)}')
    code = 'F3RF5LF7'
    expected = '<span style="color: pink">F</span><span style="color: orange">3</span><span style="color: green">R</span><span style="color: pink">F</span><span style="color: orange">5</span><span style="color: red">L</span><span style="color: pink">F</span><span style="color: orange">7</span>'
    assert highlight(code) == expected, message.format(code)
    print(f'Correct highlighting: {expected}\nYour highlighting:    {highlight(code)}')

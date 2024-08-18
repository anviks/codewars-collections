"""https://www.codewars.com/kata/52223df9e8f98c7aa7000062"""

from solution_rot13 import *


def test_example_tests():
    assert rot13('EBG13 rknzcyr.') == 'ROT13 example.'
    assert (rot13(
        "How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")
            == "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
    assert rot13('123') == '123'
    assert (rot13('Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)')
            == 'This is actually the first kata I ever made. Thanks for finishing it! :)')
    assert rot13('@[`{') == '@[`{'

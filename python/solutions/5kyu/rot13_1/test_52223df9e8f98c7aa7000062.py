"""https://www.codewars.com/kata/52223df9e8f98c7aa7000062"""
import unittest

from solution import rot13


class ExampleTests(unittest.TestCase):
    def test_rot13(self):
        self.assertEqual(rot13("EBG13 rknzcyr."), "ROT13 example.")
        self.assertEqual(rot13(
            "How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."),
                         "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
        self.assertEqual(rot13("123"), "123")
        self.assertEqual(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"),
                         "This is actually the first kata I ever made. Thanks for finishing it! :)")
        self.assertEqual(rot13("@[`{"), "@[`{")

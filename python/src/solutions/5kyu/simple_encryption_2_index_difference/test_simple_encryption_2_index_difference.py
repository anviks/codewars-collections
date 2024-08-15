"""https://www.codewars.com/kata/simple-encryption-number-2-index-difference"""
import unittest

from solution_simple_encryption_2_index_difference import decrypt, encrypt


class BasicEncryptTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(encrypt("Business"), "&61kujla")
        self.assertEqual(
            encrypt("Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when finding a solution!"),
            "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w")
        self.assertEqual(encrypt("This is a test!"), "5MyQa9p0riYplZc")
        self.assertEqual(encrypt("This kata is very interesting!"), "5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p")


class BasicDecryptTests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(
            decrypt("$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w"),
            "Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when finding a solution!")
        self.assertEqual(decrypt("5MyQa9p0riYplZc"), "This is a test!")
        self.assertEqual(decrypt("5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p"), "This kata is very interesting!")


class NoneOrEmpty(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(encrypt(""), "")
        self.assertEqual(decrypt(""), "")
        self.assertIsNone(encrypt(None))
        self.assertIsNone(decrypt(None))


class NotAllowedChars(unittest.TestCase):
    def test_solution(self):
        with self.assertRaises(ValueError):
            encrypt("A5#")
        with self.assertRaises(ValueError):
            decrypt("A5#")

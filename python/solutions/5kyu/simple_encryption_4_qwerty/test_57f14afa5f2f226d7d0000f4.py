"""https://www.codewars.com/kata/simple-encryption-number-4-qwerty"""
import unittest
from solution import encrypt, decrypt


class ExampleTests(unittest.TestCase):
    def test_encryption_tests(self):
        self.assertEqual(encrypt("A", 111), "S")
        self.assertEqual(encrypt("Abc", 212), "Smb")
        self.assertEqual(encrypt("Wave", 0), "Wave") # -> 000
        self.assertEqual(encrypt("Wave", 345), "Tg.y")
        self.assertEqual(encrypt("Ball", 134), ">fdd")
        self.assertEqual(encrypt("Ball", 444), ">gff")
        
        self.assertEqual(encrypt("This is a test.", 348), "Iaqh qh g iyhi,")
        self.assertEqual(encrypt("Do the kata Kobayashi Maru Test. Endless fun and excitement when finding a solution.", 583),                  "Sr pgi jlpl Jr,lqlage Zlow Piapc I.skiaa dw. l.s ibnepizi.p ugi. de.se.f l arkwper.c")

    def test_decryption_tests(self):
        self.assertEqual(decrypt("S", 111), "A")
        self.assertEqual(decrypt("Smb", 212), "Abc")
        self.assertEqual(decrypt("Wave", 0), "Wave") # -> 000
        self.assertEqual(decrypt("Tg.y", 345), "Wave")
        self.assertEqual(decrypt(">fdd", 134), "Ball")
        self.assertEqual(decrypt(">gff", 444), "Ball")
        
        self.assertEqual(decrypt("Iaqh qh g iyhi,", 348), "This is a test.")
        self.assertEqual(decrypt("Sr pgi jlpl Jr,lqlage Zlow Piapc I.skiaa dw. l.s ibnepizi.p ugi. de.se.f l arkwper.c", 583),                  "Do the kata Kobayashi Maru Test. Endless fun and excitement when finding a solution.")

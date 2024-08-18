"""https://www.codewars.com/kata/simple-encryption-number-4-qwerty"""

from solution_simple_encryption_number_4_qwerty import *


def test_example_tests__encryption_tests():
    assert encrypt('A', 111) == 'S'
    assert encrypt('Abc', 212) == 'Smb'
    assert encrypt('Wave', 0) == 'Wave'
    assert encrypt('Wave', 345) == 'Tg.y'
    assert encrypt('Ball', 134) == '>fdd'
    assert encrypt('Ball', 444) == '>gff'
    assert encrypt('This is a test.', 348) == 'Iaqh qh g iyhi,'
    assert (encrypt('Do the kata Kobayashi Maru Test. Endless fun and excitement when finding a solution.', 583)
            == 'Sr pgi jlpl Jr,lqlage Zlow Piapc I.skiaa dw. l.s ibnepizi.p ugi. de.se.f l arkwper.c')


def test_example_tests__decryption_tests():
    assert decrypt('S', 111) == 'A'
    assert decrypt('Smb', 212) == 'Abc'
    assert decrypt('Wave', 0) == 'Wave'
    assert decrypt('Tg.y', 345) == 'Wave'
    assert decrypt('>fdd', 134) == 'Ball'
    assert decrypt('>gff', 444) == 'Ball'
    assert decrypt('Iaqh qh g iyhi,', 348) == 'This is a test.'
    assert (decrypt('Sr pgi jlpl Jr,lqlage Zlow Piapc I.skiaa dw. l.s ibnepizi.p ugi. de.se.f l arkwper.c', 583)
            == 'Do the kata Kobayashi Maru Test. Endless fun and excitement when finding a solution.')

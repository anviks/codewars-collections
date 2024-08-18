"""https://www.codewars.com/kata/526156943dfe7ce06200063e"""

from solution_my_smallest_code_interpreter_aka_brainf_star_star_k import *


def test_example():
    assert brain_luck(',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars'
    assert brain_luck(',[.[-],]', 'Codewars' + chr(0)) == 'Codewars'
    assert brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)) == chr(72)

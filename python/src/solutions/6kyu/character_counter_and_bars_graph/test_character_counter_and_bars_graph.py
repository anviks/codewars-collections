"""https://www.codewars.com/kata/5826773bfad36332bf0002f9"""

from solution_character_counter_and_bars_graph import *


def test_fixed_tests__basic_test_cases():
    text2 = "Let's suppose you have to use an old terminal window"
    max2 = 5
    solution2 = 'e:#####\no:#####\ns:####\na:###\nl:###\nn:###\nt:###\nu:###\nd:##\ni:##\np:##\nw:##\nh:#\nm:#\nr:#\nv:#\ny:#'
    assert count_and_print_graph(text2, max2) == solution2

    text3 = "Let's suppose you have to use an old terminal window"
    max3 = 24
    solution3 = 'e:########################\no:########################\ns:###################\na:##############\nl:##############\nn:##############\nt:##############\nu:##############\nd:#########\ni:#########\np:#########\nw:#########\nh:####\nm:####\nr:####\nv:####\ny:####'
    assert count_and_print_graph(text3, max3) == solution3

    text4 = 'The Free Software Foundation uses the name GNU/Linux to describe the operating system, which has led to some controversy.'
    max4 = 35
    solution4 = 'e:###################################\nt:#######################\no:#####################\ns:#####################\nn:################\nh:##############\nr:##############\na:###########\ni:###########\nu:#########\nc:#######\nd:#######\nf:#######\nm:#######\ng:####\nl:####\nw:####\ny:####\nb:##\np:##\nv:##\nx:##'
    assert count_and_print_graph(text4, max4) == solution4

    text5 = 'abcda bcdbbd aooooo@ )(%& $%8 7235 4892'
    max5 = 10
    solution5 = 'o:##########\nb:########\na:######\nd:######\nc:####'
    assert count_and_print_graph(text5, max5) == solution5

    text6 = 'just a short text'
    max6 = 4
    solution6 = 't:####\ns:##\na:#\ne:#\nh:#\nj:#\no:#\nr:#\nu:#\nx:#'
    assert count_and_print_graph(text6, max6) == solution6

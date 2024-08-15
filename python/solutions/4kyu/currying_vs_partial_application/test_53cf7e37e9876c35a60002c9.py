"""https://www.codewars.com/kata/currying-vs-partial-application"""

import unittest

from solution import curry_partial


class SolutionTests(unittest.TestCase):
    def test_function_with_three_random_parameters(self):
        def add(a, b, c):
            return a + b + c

        a = 1
        b = 2
        c = 3

        sum_ = a + b + c

        self.assertEqual(add(a, b, c), sum_)
        self.assertEqual(curry_partial(add)(a)(b)(c), sum_)
        self.assertEqual(curry_partial(add, a)(b)(c), sum_)
        self.assertEqual(curry_partial(add, a)(b, c), sum_)
        self.assertEqual(curry_partial(add, a, b, c), sum_)
        self.assertEqual(curry_partial(add, a, b, c, 20), sum_)
        self.assertEqual(curry_partial(add)(a, b, c), sum_)
        self.assertEqual(curry_partial(add)()(a, b, c), sum_)
        self.assertEqual(curry_partial(add)()(a)()()(b, c), sum_)
        self.assertEqual(curry_partial(add)()(a)()()(b, c, 5, 6, 7), sum_)

        self.assertEqual(curry_partial(curry_partial(curry_partial(add, a), b), c), sum_)
        self.assertEqual(curry_partial(curry_partial(add, a, b), c), sum_)
        self.assertEqual(curry_partial(curry_partial(add, a), b, c), sum_)

        self.assertEqual(curry_partial(curry_partial(add, a), b)(c), sum_)
        self.assertEqual(curry_partial(curry_partial(add, a)(b), c), sum_)

        self.assertEqual(curry_partial(curry_partial(curry_partial(add, a)), b, c), sum_)

    def test_function_with_two_random_parameters(self):
        add = lambda x, y: x + y

        a = 1
        b = 2

        sum_ = a + b

        self.assertEqual(add(a, b), sum_)
        self.assertEqual(curry_partial(add)(a)(b), sum_)
        self.assertEqual(curry_partial(add, a, b), sum_)
        self.assertEqual(curry_partial(add, a, b, 20), sum_)
        self.assertEqual(curry_partial(add)(a, b), sum_)
        self.assertEqual(curry_partial(add)()(a, b), sum_)
        self.assertEqual(curry_partial(add)()(a)()()(b), sum_)
        self.assertEqual(curry_partial(add)()(a)()()(b, 5, 6, 7), sum_)

        self.assertEqual(curry_partial(curry_partial(add, a), b), sum_)

    def test_function_with_one_random_parameter(self):
        double = lambda x: x + x

        a = 5
        result = a * 2

        self.assertEqual(double(a), result)
        self.assertEqual(curry_partial(double)(a), result)
        self.assertEqual(curry_partial(double, a), result)
        self.assertEqual(curry_partial(double)()(a), result)

    def test_function_with_no_parameters(self):
        a = 5

        def double():
            return a * 2

        result = a * 2

        self.assertEqual(double(), result)
        self.assertEqual(curry_partial(double), result)

    def test_function_with_four_random_parameters(self):
        def add(a, b, c, d):
            return 4 * a + 3 * b + 2 * c + d

        a = 4
        b = 3
        c = 2
        d = 1

        sum_ = 4 * a + 3 * b + 2 * c + d

        self.assertEqual(add(a, b, c, d), sum_)
        self.assertEqual(curry_partial(add)(a)(b)(c)(d), sum_)
        self.assertEqual(curry_partial(add)(a, b)(c)(d), sum_)
        self.assertEqual(curry_partial(add, a, b)(c)(d), sum_)
        self.assertEqual(curry_partial(add, a, b)(c, d), sum_)
        self.assertEqual(curry_partial(curry_partial(add, a, b), c, d), sum_)
        self.assertEqual(curry_partial(curry_partial(add, a, b)(c), d), sum_)
        self.assertEqual(curry_partial(curry_partial(add, a)(b, c), d), sum_)
        self.assertEqual(curry_partial(curry_partial(curry_partial(add, a), b), c, d), sum_)
        self.assertEqual(curry_partial(curry_partial(curry_partial(add, a), b), c)(d), sum_)
        self.assertEqual(curry_partial(curry_partial(curry_partial(curry_partial(add, a), b), c), d), sum_)

    def test_state_isn_t_preserved(self):
        def add(a, b, c):
            return a + b + c

        add1 = curry_partial(add, 1)
        self.assertEqual(add1(2, 3), 6)
        self.assertEqual(add1(4, 5), 10)

        add2 = curry_partial(add)(2)
        self.assertEqual(add2(3, 4), 9)
        self.assertEqual(add2(5)(6), 13)

        it0 = [curry_partial(add)]
        it1 = [it0[0](0), it0[0](1)]
        it2 = [it1[0](0), it1[1](0),
               it1[0](2), it1[1](2)]
        it3 = [it2[0](0), it2[1](0), it2[2](0), it2[3](0),
               it2[0](4), it2[1](4), it2[2](4), it2[3](4)]

        self.assertEqual(it3, [0, 1, 2, 3, 4, 5, 6, 7], "tree of calls")

    def test_should_ignore_additional_parameters(self):
        a = 5

        def double():
            return a * 2

        result = a * 2

        self.assertEqual(curry_partial(curry_partial(double), 1), result)

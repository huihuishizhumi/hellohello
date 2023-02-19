from unittest import TestCase

from src.calc import Calculator


class TestCalculator(TestCase):
    def test_compute_should_return_3_when_1_plus_2(self):
        # given
        x, y, op = 1, 2, '+'

        # when
        ret = Calculator().compute(x, y, op)

        # then
        self.assertEqual(3, ret)

    def test_compute_should_return_1_when_3_minus_2(self):
        # given
        x, y, op = 3, 2, '-'

        # when
        ret = Calculator().compute(x, y, op)

        # then
        self.assertEqual(1, ret)

    def test_compute_should_return_6_when_2_multiple_3(self):
        # given
        x, y, op = 2, 3, '*'

        # when
        ret = Calculator().compute(x, y, op)

        # then
        self.assertEqual(6, ret)

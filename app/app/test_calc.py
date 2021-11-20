from django.test import TestCase

from app.calc import add


class CalcTest(TestCase):

    def test_dd_two_numbers(self):
        self.assertEqual(add(3, 5), 8)

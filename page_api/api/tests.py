from django.test import TestCase

# Create your tests here.
from page_api.api.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(3, 5), 8)

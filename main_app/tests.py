from django.test import SimpleTestCase
from .utils import extract_first_two_digit_number


class ExtractFirstTwoDigitNumberTests(SimpleTestCase):
    def test_returns_first_two_digit_number(self):
        self.assertEqual(extract_first_two_digit_number("abc 12 def 34"), 12)

    def test_returns_none_when_no_two_digit_number(self):
        self.assertIsNone(extract_first_two_digit_number("a1 b2 c3"))

    def test_ignores_numbers_with_more_than_two_digits(self):
        self.assertEqual(extract_first_two_digit_number("a 7 123 45"), 45)


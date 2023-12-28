"""
Sample Tests
"""
from django.test import SimpleTestCase

from app import calculator


class CalculatorTest(SimpleTestCase):
    """Test the calculator module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        result = calculator.add(5, 6)

        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        """Test substracting numbers."""
        result = calculator.subtract(10, 15)

        self.assertEqual(result, 5)

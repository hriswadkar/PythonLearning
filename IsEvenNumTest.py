import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from IsEvenNum import is_even, main

class IsEvenNumTests(unittest.TestCase):
    def test_is_even_with_even_number(self):
        self.assertTrue(is_even(4))

    def test_is_even_with_odd_number(self):
        self.assertFalse(is_even(5))

    def test_main_prints_even_message(self):
        output = io.StringIO()
        with redirect_stdout(output):
            with patch('builtins.input', return_value='4'):
                main()
        self.assertIn("4 is an even number.", output.getvalue())

    def test_main_prints_odd_message(self):
        output = io.StringIO()
        with redirect_stdout(output):
            with patch('builtins.input', return_value='5'):
                main()
        self.assertIn("5 is an odd number.", output.getvalue())
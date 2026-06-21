import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from IsPalindrome import is_palindrome, main


class IsPalindromeTests(unittest.TestCase):
    def test_is_palindrome_with_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_is_palindrome_with_non_palindrome(self):
        self.assertFalse(is_palindrome("python"))

    def test_is_palindrome_ignores_case_and_spaces(self):
        self.assertTrue(is_palindrome("Never odd or even"))

    def test_main_prints_palindrome_message(self):
        output = io.StringIO()
        with redirect_stdout(output):
            with patch("builtins.input", return_value="madam"):
                main()
        self.assertIn("madam is a palindrome.", output.getvalue())

    def test_main_prints_non_palindrome_message(self):
        output = io.StringIO()
        with redirect_stdout(output):
            with patch("builtins.input", return_value="python"):
                main()
        self.assertIn("python is not a palindrome.", output.getvalue())


if __name__ == "__main__":
    unittest.main()

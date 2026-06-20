import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from CountVowels import count_vowels, main

class CountVowelsTests(unittest.TestCase):
    def test_count_vowels_with_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_count_vowels_without_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_count_vowels_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_uppercase(self):
        self.assertEqual(count_vowels("HELLO"), 2)

    def test_count_vowels_numbers_and_special_chars(self):
        self.assertEqual(count_vowels("h3ll0!"), 0)

    def test_count_vowels_none_raises(self):
        with self.assertRaises(TypeError):
            count_vowels(None)

    def test_main_prints_vowel_count(self):
        output = io.StringIO()
        with redirect_stdout(output):
            with patch('builtins.input', return_value='hello'):
                main()
        self.assertIn("The string contains 2 vowel(s).", output.getvalue())
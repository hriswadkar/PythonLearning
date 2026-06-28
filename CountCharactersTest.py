import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from CountCharacters import count_characters, main

class CountCharactersTests(unittest.TestCase):
    def test_count_characters_basic(self):
        self.assertEqual(count_characters("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_count_characters_empty_string(self):
        self.assertEqual(count_characters(""), {})

    def test_count_characters_with_spaces(self):
        self.assertEqual(count_characters("hello world"), {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

    def test_count_characters_with_special_chars(self):
        self.assertEqual(count_characters("H3ll0!"), {'h': 1, '3': 1, 'l': 2, '0': 1, '!': 1})

    def test_count_characters_case_sensitive(self):
        self.assertEqual(count_characters("Hello"), {'H': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_count_characters_none_raises(self):
        with self.assertRaises(TypeError):
            count_characters(None)

    def test_count_characters_non_string_raises(self):
        with self.assertRaises(TypeError):
            count_characters(123)

    def test_count_characters_with_unicode(self):
        self.assertEqual(count_characters("héllo"), {'h': 1, 'é': 1, 'l': 2, 'o': 1})

    def test_count_characters_with_repeated_chars(self):
        self.assertEqual(count_characters("banana"), {'b': 1, 'a': 3, 'n': 2})

    def test_count_characters_with_all_same_chars(self):
        self.assertEqual(count_characters("aaaaa"), {'a': 5})


    def test_count_characters_with_mixed_content(self):
        self.assertEqual(count_characters("Hello, World! 123"), {
            'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 2, 'W': 1, 'r': 1, 'd': 1, '!': 1, '1': 1, '2': 1, '3': 1
        })

    def test_count_characters_with_newlines_and_tabs(self):
        self.assertEqual(count_characters("Hello\nWorld\t!"), {
            'H': 1, 'e': 1, 'l': 3, 'o': 2, '\n': 1, 'W': 1, 'r': 1, 'd': 1, '\t': 1, '!': 1
        })

    def test_count_characters_with_non_ascii(self):
        self.assertEqual(count_characters("こんにちは"), {'こ': 1, 'ん': 1, 'に': 1, 'ち': 1, 'は': 1})

    def test_count_characters_with_mixed_case(self):
        self.assertEqual(count_characters("AaAaA"), {'A': 3, 'a': 2})

    def test_count_characters_with_long_string(self):
        long_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 100
        character_count = count_characters(long_string)
        self.assertEqual(character_count['L'], 100)
        self.assertEqual(character_count['o'], 300)
        self.assertEqual(character_count[' '], 700)

    

    def test_main_prints_character_count(self):
        output = io.StringIO()
        with redirect_stdout(output):
            with patch('builtins.input', return_value='hello'):
                main()
        self.assertIn("'h': 1", output.getvalue())
        self.assertIn("'e': 1", output.getvalue())
        self.assertIn("'l': 2", output.getvalue())
        self.assertIn("'o': 1", output.getvalue())
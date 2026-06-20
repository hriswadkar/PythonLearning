import io
import unittest
from contextlib import redirect_stdout

from FirstProgram.FirstProgram import build_table, main


class FirstProgramTests(unittest.TestCase):
    def test_build_table_returns_table_of_two(self):
        self.assertEqual(
            build_table(2),
            [
                "2 x 1 = 2",
                "2 x 2 = 4",
                "2 x 3 = 6",
                "2 x 4 = 8",
                "2 x 5 = 10",
                "2 x 6 = 12",
                "2 x 7 = 14",
                "2 x 8 = 16",
                "2 x 9 = 18",
                "2 x 10 = 20",
            ],
        )

    def test_main_prints_table_of_two(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual(
            output.getvalue(),
            "Table of 2\n"
            "2 x 1 = 2\n"
            "2 x 2 = 4\n"
            "2 x 3 = 6\n"
            "2 x 4 = 8\n"
            "2 x 5 = 10\n"
            "2 x 6 = 12\n"
            "2 x 7 = 14\n"
            "2 x 8 = 16\n"
            "2 x 9 = 18\n"
            "2 x 10 = 20\n",
        )


if __name__ == "__main__":
    unittest.main()

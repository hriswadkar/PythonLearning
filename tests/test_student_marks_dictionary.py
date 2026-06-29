import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from StudentMarksDictionary import save_student_marks_to_file, main


class StudentMarksDictionaryTests(unittest.TestCase):
    def test_save_student_marks_to_file_writes_json(self):
        student_marks = {"Asha": [90.0, 95.5], "Ben": [78.0]}

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "marks.json"
            save_student_marks_to_file(student_marks, str(file_path))

            self.assertEqual(json.loads(file_path.read_text(encoding="utf-8")), student_marks)

    def test_main_can_save_student_marks(self):
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "student_marks.json"
            with redirect_stdout(output):
                with patch(
                    "builtins.input",
                    side_effect=["Asha: 90, Ben: 80", "done", "y", str(file_path)],
                ):
                    main()

            saved_data = json.loads(file_path.read_text(encoding="utf-8"))

        self.assertEqual(saved_data, {"Asha": [90.0], "Ben": [80.0]})
        self.assertIn("Student marks saved to", output.getvalue())


if __name__ == "__main__":
    unittest.main()
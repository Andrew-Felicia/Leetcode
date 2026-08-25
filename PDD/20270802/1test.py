import subprocess
import sys
import unittest
from pathlib import Path


SOLUTION_FILE = Path(__file__).with_name("1prac.py")


class TestACMInputOutput(unittest.TestCase):
    def check_output(self, test_input, expected_output, timeout=3):
        result = subprocess.run(
            [sys.executable, str(SOLUTION_FILE)],
            input=test_input,
            text=True,
            capture_output=True,
            timeout=timeout,
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=f"Program crashed:\n{result.stderr}",
        )
        self.assertEqual(result.stdout.strip(), str(expected_output))

    def test_single_a(self):
        self.check_output("1\nA\n", 0)

    def test_single_b(self):
        self.check_output("1\nB\n", 0)

    def test_balanced_pair(self):
        self.check_output("2\nAB\n", 2)

    def test_entire_string_is_balanced(self):
        self.check_output("4\nAABB\n", 4)
        self.check_output("6\nABBAAB\n", 6)
        self.check_output("6\nBABABA\n", 6)

    def test_no_balanced_substring(self):
        self.check_output("4\nAAAA\n", 0)
        self.check_output("4\nBBBB\n", 0)

    def test_part_of_string_is_balanced(self):
        self.check_output("5\nAAABB\n", 4)
        self.check_output("5\nBAAAA\n", 2)
        self.check_output("7\nAAABABB\n", 6)

    def test_input_with_extra_whitespace(self):
        self.check_output("\n  4  \n  ABAB  \n", 4)

    def test_large_input(self):
        s = "AB" * 50_000
        self.check_output(f"{len(s)}\n{s}\n", 100_000, timeout=5)


if __name__ == "__main__":
    unittest.main()


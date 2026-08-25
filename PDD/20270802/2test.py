import subprocess
import sys
import unittest
from pathlib import Path


SOLUTION_FILE = Path(__file__).with_name("2.py")


class TestConstructSmallestACM(unittest.TestCase):
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

    def test_single_rating(self):
        self.check_output("1\n3\n", "3")

    def test_two_different_ratings(self):
        self.check_output("2\n2 1\n", "1 2")

    def test_two_equal_ratings_are_impossible(self):
        self.check_output("2\n1 1\n", "-1")

    def test_smallest_alternating_answer(self):
        self.check_output("5\n2 1 2 1 1\n", "1 2 1 2 1")

    def test_all_ratings_are_different(self):
        self.check_output("5\n5 4 3 2 1\n", "1 2 3 4 5")

    def test_lexicographically_smallest_answer(self):
        self.check_output("4\n3 1 2 1\n", "1 2 1 3")
        self.check_output("5\n3 1 2 1 3\n", "1 2 3 1 3")

    def test_smallest_rating_cannot_be_first(self):
        self.check_output("5\n2 1 2 2 3\n", "2 1 2 3 2")

    def test_repeated_largest_rating(self):
        self.check_output("6\n5 1 5 2 3 4\n", "1 2 3 5 4 5")

    def test_feasible_boundary(self):
        self.check_output(
            "7\n1 1 1 1 2 2 2\n",
            "1 2 1 2 1 2 1",
        )

    def test_impossible_when_one_rating_appears_too_often(self):
        self.check_output("6\n1 1 1 1 2 2\n", "-1")

    def test_input_with_extra_whitespace(self):
        self.check_output(
            "\n  4  \n  1   2\n1   2  \n",
            "1 2 1 2",
        )

    def test_large_input(self):
        ratings = ["1", "2"] * 50_000
        test_input = f"{len(ratings)}\n{' '.join(ratings)}\n"
        expected_output = " ".join(ratings)

        self.check_output(test_input, expected_output, timeout=5)


if __name__ == "__main__":
    unittest.main()
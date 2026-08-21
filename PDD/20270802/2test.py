import random
import subprocess
import sys
import unittest
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path


SOLUTION_FILE = "2.py"
FOLDER = Path(__file__).resolve().parent


def run_solution(s, timeout=3):
    """Run 1.py exactly like an online judge would run it."""
    if isinstance(s, str):
        values = s.split()
    else:
        values = [str(value) for value in s]

    test_input = f"{len(values)}\n{' '.join(values)}\n"

    result = subprocess.run(
        [sys.executable, SOLUTION_FILE],
        input=test_input,
        text=True,
        capture_output=True,
        timeout=timeout,
        cwd=FOLDER,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{SOLUTION_FILE} exited with code {result.returncode}\n"
            f"stderr:\n{result.stderr}"
        )

    return result.stdout.strip()


@lru_cache(maxsize=None)
def brute_force(state, previous=-1):
    """Find the exact lexicographically smallest answer for a small case."""
    if sum(state) == 0:
        return ()

    for rating in range(5):
        if rating == previous or state[rating] == 0:
            continue

        next_state = list(state)
        next_state[rating] -= 1
        suffix = brute_force(tuple(next_state), rating)

        if suffix is not None:
            return (rating + 1,) + suffix

    return None


def counts_to_input(counts):
    values = []
    for rating, count in enumerate(counts, start=1):
        values.extend([rating] * count)
    return values


def parse_output(output):
    if output == "-1":
        return None
    return list(map(int, output.split()))


class SolutionTestCase(unittest.TestCase):
    def assert_valid(self, values, answer):
        self.assertIsNotNone(answer)
        self.assertEqual(len(answer), len(values))
        self.assertEqual(Counter(answer), Counter(values))
        self.assertTrue(
            all(answer[i] != answer[i - 1] for i in range(1, len(answer)))
        )

    def assert_exact(self, values):
        counts = tuple(values.count(rating) for rating in range(1, 6))
        expected = brute_force(counts)
        actual = parse_output(run_solution(values))
        self.assertEqual(actual, None if expected is None else list(expected))


class TestEdgeCases(SolutionTestCase):
    def test_single_values(self):
        for rating in range(1, 6):
            with self.subTest(rating=rating):
                self.assertEqual(run_solution([rating]), str(rating))

    def test_two_equal_values(self):
        for rating in range(1, 6):
            with self.subTest(rating=rating):
                self.assertEqual(run_solution([rating, rating]), "-1")

    def test_two_different_values(self):
        self.assertEqual(run_solution([5, 2]), "2 5")

    def test_forced_alternation(self):
        self.assertEqual(run_solution([1, 1, 1, 2, 2]), "1 2 1 2 1")

    def test_balanced_counts(self):
        self.assertEqual(run_solution([1, 1, 1, 2, 2, 2]), "1 2 1 2 1 2")

    def test_all_five_values(self):
        self.assertEqual(run_solution([5, 4, 3, 2, 1]), "1 2 3 4 5")

    def test_lexicographic_trap(self):
        # Choosing 1 first would make the remaining suffix impossible.
        self.assertEqual(run_solution([1, 2, 2, 2, 3]), "2 1 2 3 2")

    def test_maximum_legal_dominance(self):
        self.assertEqual(run_solution([1, 1, 1, 1, 2, 3, 4]), "1 2 1 3 1 4 1")

    def test_one_over_legal_dominance(self):
        self.assertEqual(run_solution([1, 1, 1, 1, 1, 2, 3, 4]), "-1")

    def test_only_high_ratings(self):
        self.assertEqual(run_solution([3, 3, 4, 4, 5]), "3 4 3 4 5")

    def test_string_argument(self):
        self.assertEqual(run_solution("1 1 2 2 3"), "1 2 1 2 3")


class TestExhaustiveSmallCases(SolutionTestCase):
    def test_all_small_count_combinations(self):
        # Tests all 3^5 - 1 = 242 non-empty multisets in separate processes.
        for counts in product(range(3), repeat=5):
            if sum(counts) == 0:
                continue

            values = counts_to_input(counts)
            random.Random(str(counts)).shuffle(values)

            with self.subTest(counts=counts):
                self.assert_exact(values)


class TestRandomStress(SolutionTestCase):
    def test_random_small_against_brute_force(self):
        rng = random.Random(20270802)

        for case_number in range(200):
            values = [rng.randint(1, 5) for _ in range(rng.randint(1, 14))]
            with self.subTest(case=case_number, values=values):
                self.assert_exact(values)

    def test_random_medium_cases(self):
        rng = random.Random(42)

        for case_number in range(100):
            counts = [rng.randint(0, 100) for _ in range(5)]
            if sum(counts) == 0:
                counts[rng.randrange(5)] = 1

            values = counts_to_input(counts)
            rng.shuffle(values)
            answer = parse_output(run_solution(values))
            possible = max(counts) <= (sum(counts) + 1) // 2

            with self.subTest(case=case_number, counts=counts):
                if possible:
                    self.assert_valid(values, answer)
                else:
                    self.assertIsNone(answer)


class TestMaximumConstraints(SolutionTestCase):
    def test_one_million_balanced(self):
        values = counts_to_input([200_000] * 5)
        answer = parse_output(run_solution(values, timeout=10))
        self.assert_valid(values, answer)

    def test_one_million_maximum_legal_dominance(self):
        values = counts_to_input([500_000, 125_000, 125_000, 125_000, 125_000])
        answer = parse_output(run_solution(values, timeout=10))
        self.assert_valid(values, answer)

    def test_one_million_impossible(self):
        values = counts_to_input([500_001, 499_999, 0, 0, 0])
        self.assertEqual(run_solution(values, timeout=10), "-1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
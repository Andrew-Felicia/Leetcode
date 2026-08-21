"""Black-box tests for 4.py. Run with: python3 4test.py"""

import random
import subprocess
import sys
import unittest
from functools import lru_cache
from itertools import product
from pathlib import Path


SOLUTION_FILE = "4.py"
FOLDER = Path(__file__).resolve().parent


def run_solution(cases, timeout=3):
    lines = [str(len(cases))]

    for a in cases:
        lines.append(str(len(a)))
        lines.append(" ".join(map(str, a)))

    result = subprocess.run(
        [sys.executable, SOLUTION_FILE],
        input="\n".join(lines) + "\n",
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

    output = result.stdout.split()
    if len(output) != len(cases):
        raise AssertionError(
            f"Expected {len(cases)} answers, received {len(output)}: {output!r}"
        )

    try:
        return list(map(int, output))
    except ValueError as error:
        raise AssertionError(f"Every answer must be an integer: {output!r}") from error


@lru_cache(maxsize=None)
def independent_sets(n):
    if n == 1:
        return ((0,),)

    result = []
    for mask in range(1, 1 << n):
        valid = True

        for city in range(n):
            next_city = (city + 1) % n
            if (mask >> city) & 1 and (mask >> next_city) & 1:
                valid = False
                break

        if valid:
            result.append(tuple(i for i in range(n) if (mask >> i) & 1))

    return tuple(result)


@lru_cache(maxsize=None)
def brute_force(state):
    """Try every valid replenishment group; only suitable for small cases."""
    if not any(state):
        return 0

    answer = sum(state)

    for selected in independent_sets(len(state)):
        next_state = list(state)
        changed = False

        for city in selected:
            if next_state[city] > 0:
                next_state[city] -= 1
                changed = True

        if changed:
            answer = min(answer, 1 + brute_force(tuple(next_state)))

    return answer


def formula(a):
    if len(a) == 1:
        return a[0]

    edge_bound = max(a[i] + a[(i + 1) % len(a)] for i in range(len(a)))

    if len(a) % 2 == 0:
        return edge_bound

    independent_size = len(a) // 2
    total_bound = (sum(a) + independent_size - 1) // independent_size
    return max(edge_bound, total_bound)


class TestEdgeCases(unittest.TestCase):
    def test_one_warehouse_zero_work(self):
        self.assertEqual(run_solution([[0]]), [0])

    def test_one_warehouse(self):
        self.assertEqual(run_solution([[17]]), [17])

    def test_one_warehouse_maximum_value(self):
        self.assertEqual(run_solution([[10**9]]), [10**9])

    def test_two_warehouses(self):
        self.assertEqual(run_solution([[4, 7]]), [11])

    def test_triangle(self):
        self.assertEqual(run_solution([[2, 3, 4]]), [9])

    def test_all_zero(self):
        self.assertEqual(run_solution([[0, 0, 0, 0, 0]]), [0])

    def test_even_cycle(self):
        self.assertEqual(run_solution([[4, 2, 3, 1]]), [6])

    def test_even_cycle_nonadjacent_large_values(self):
        self.assertEqual(run_solution([[5, 0, 5, 0]]), [5])

    def test_wraparound_edge(self):
        self.assertEqual(run_solution([[10, 0, 0, 0, 8, 1]]), [11])

    def test_odd_cycle_needs_global_bound(self):
        # At most two warehouses can be selected in one round.
        self.assertEqual(run_solution([[1, 1, 1, 1, 1]]), [3])

    def test_odd_cycle_edge_bound_is_stronger(self):
        self.assertEqual(run_solution([[10, 1, 0, 0, 1]]), [11])

    def test_large_answer_above_32_bit(self):
        self.assertEqual(run_solution([[10**9, 10**9, 10**9]]), [3 * 10**9])

    def test_multiple_cases_in_one_input(self):
        cases = [[3], [4, 7], [1, 1, 1, 1, 1], [5, 0, 5, 0]]
        self.assertEqual(run_solution(cases), [3, 11, 3, 5])


class TestExhaustiveSmallCases(unittest.TestCase):
    def test_every_small_multiset_against_brute_force(self):
        cases = []
        expected = []

        # 3 + 3^2 + ... + 3^7 = 3,279 cases.
        for n in range(1, 8):
            for a in product(range(3), repeat=n):
                cases.append(list(a))
                expected.append(brute_force(a))

        self.assertEqual(run_solution(cases, timeout=10), expected)


class TestRandomStress(unittest.TestCase):
    def test_random_small_cases_against_brute_force(self):
        rng = random.Random(20270802)
        cases = []
        expected = []

        for _ in range(500):
            n = rng.randint(1, 8)
            a = [rng.randint(0, 3) for _ in range(n)]
            cases.append(a)
            expected.append(brute_force(tuple(a)))

        self.assertEqual(run_solution(cases, timeout=10), expected)

    def test_random_medium_cases(self):
        rng = random.Random(42)
        cases = []

        for _ in range(1000):
            n = rng.randint(1, 200)
            cases.append([rng.randint(0, 10**9) for _ in range(n)])

        self.assertEqual(run_solution(cases, timeout=10), [formula(a) for a in cases])

    def test_rotation_does_not_change_answer(self):
        rng = random.Random(314159)
        cases = []
        pairs = []

        for _ in range(200):
            n = rng.randint(2, 100)
            a = [rng.randint(0, 10_000) for _ in range(n)]
            shift = rng.randrange(n)
            rotated = a[shift:] + a[:shift]
            pairs.append((len(cases), len(cases) + 1))
            cases.extend([a, rotated])

        answers = run_solution(cases, timeout=10)
        for original, rotated in pairs:
            self.assertEqual(answers[original], answers[rotated])


class TestMaximumConstraints(unittest.TestCase):
    def test_two_hundred_thousand_even_cycle(self):
        n = 200_000
        a = [10**9 if i % 2 == 0 else 0 for i in range(n)]
        self.assertEqual(run_solution([a], timeout=10), [10**9])

    def test_large_odd_cycle(self):
        n = 199_999
        a = [1] * n
        self.assertEqual(run_solution([a], timeout=10), [3])

    def test_many_cases_totaling_two_hundred_thousand_values(self):
        cases = []
        for case in range(200):
            cases.append([(i * 97 + case) % 10**9 for i in range(1000)])

        self.assertEqual(run_solution(cases, timeout=10), [formula(a) for a in cases])


if __name__ == "__main__":
    unittest.main(verbosity=2)

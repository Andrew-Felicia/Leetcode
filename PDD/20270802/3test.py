"""Black-box tests for 3.py. Run with: python3 3test.py"""

import random
import subprocess
import sys
import unittest
from pathlib import Path


SOLUTION_FILE = "3sol.py"
FOLDER = Path(__file__).resolve().parent


def run_solution(n, edges, timeout=3):
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{u} {v} {w}" for u, v, w in edges)
    test_input = "\n".join(lines) + "\n"

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

    output = result.stdout.strip()
    try:
        return int(output)
    except ValueError as error:
        raise AssertionError(f"Expected one integer, received: {output!r}") from error


def reference_answer(n, edges):
    """Independent all-pairs shortest-path oracle for small graphs."""
    infinity = 10**18
    distance = [[infinity] * n for _ in range(n)]

    for city in range(n):
        distance[city][city] = 0

    for u, v, w in edges:
        u -= 1
        v -= 1
        distance[u][v] = min(distance[u][v], w)

    for middle in range(n):
        for start in range(n):
            if distance[start][middle] == infinity:
                continue
            through_middle = distance[start][middle]
            for end in range(n):
                candidate = through_middle + distance[middle][end]
                if candidate < distance[start][end]:
                    distance[start][end] = candidate

    answer = infinity
    for u, v, _ in edges:
        before = distance[0][u - 1]
        after = distance[v - 1][n - 1]
        if before < infinity and after < infinity:
            answer = min(answer, before + after)

    return -1 if answer == infinity else answer


class TestEdgeCases(unittest.TestCase):
    def test_no_edges(self):
        self.assertEqual(run_solution(2, []), -1)

    def test_single_edge_becomes_free(self):
        self.assertEqual(run_solution(2, [(1, 2, 10_000)]), 0)

    def test_simple_chain(self):
        self.assertEqual(run_solution(3, [(1, 2, 5), (2, 3, 7)]), 5)

    def test_coupon_on_first_edge(self):
        edges = [(1, 2, 100), (2, 3, 4), (3, 4, 3)]
        self.assertEqual(run_solution(4, edges), 7)

    def test_coupon_on_last_edge(self):
        edges = [(1, 2, 3), (2, 3, 4), (3, 4, 100)]
        self.assertEqual(run_solution(4, edges), 7)

    def test_best_route_changes_after_coupon(self):
        edges = [
            (1, 2, 5),
            (2, 4, 100),
            (1, 3, 50),
            (3, 4, 51),
        ]
        self.assertEqual(run_solution(4, edges), 5)

    def test_direct_edge_always_gives_zero(self):
        edges = [(1, 2, 3), (2, 4, 4), (1, 4, 9999)]
        self.assertEqual(run_solution(4, edges), 0)

    def test_directed_edges_cannot_be_reversed(self):
        edges = [(2, 1, 1), (2, 3, 1), (3, 4, 1)]
        self.assertEqual(run_solution(4, edges), -1)

    def test_parallel_edges(self):
        edges = [(1, 2, 9), (1, 2, 2), (2, 3, 8)]
        self.assertEqual(run_solution(3, edges), 2)

    def test_cycle(self):
        edges = [(1, 2, 8), (2, 1, 1), (2, 3, 6), (3, 2, 1), (3, 4, 7)]
        self.assertEqual(run_solution(4, edges), 13)

    def test_self_loop_does_not_help(self):
        edges = [(1, 1, 100), (1, 2, 6), (2, 3, 7)]
        self.assertEqual(run_solution(3, edges), 6)

    def test_unreachable_destination_with_other_edges(self):
        edges = [(1, 2, 1), (2, 3, 1), (4, 5, 1)]
        self.assertEqual(run_solution(5, edges), -1)

    def test_large_total_cost(self):
        edges = [(city, city + 1, 10_000) for city in range(1, 100)]
        self.assertEqual(run_solution(100, edges), 980_000)


class TestRandomGraphs(unittest.TestCase):
    def test_random_small_graphs_against_reference(self):
        rng = random.Random(20270802)

        for case_number in range(300):
            n = rng.randint(2, 8)
            m = rng.randint(0, min(30, n * n))
            edges = [
                (rng.randint(1, n), rng.randint(1, n), rng.randint(1, 30))
                for _ in range(m)
            ]

            expected = reference_answer(n, edges)
            actual = run_solution(n, edges)

            with self.subTest(case=case_number, n=n, edges=edges):
                self.assertEqual(actual, expected)

    def test_random_dags_against_reference(self):
        rng = random.Random(314159)

        for case_number in range(150):
            n = rng.randint(2, 15)
            edges = []

            for u in range(1, n):
                for v in range(u + 1, n + 1):
                    if rng.random() < 0.25:
                        edges.append((u, v, rng.randint(1, 10_000)))

            expected = reference_answer(n, edges)
            actual = run_solution(n, edges)

            with self.subTest(case=case_number, n=n, edges=edges):
                self.assertEqual(actual, expected)


class TestMaximumConstraints(unittest.TestCase):
    def test_chain_with_one_hundred_thousand_cities(self):
        n = 100_000
        edges = [(city, city + 1, 10_000) for city in range(1, n)]
        self.assertEqual(run_solution(n, edges, timeout=10), 999_980_000)

    def test_nearly_two_hundred_thousand_edges(self):
        n = 100_000
        edges = []
        for city in range(1, n):
            edges.append((city, city + 1, 1))
            edges.append((city, city + 1, 10_000))

        self.assertEqual(len(edges), 199_998)
        self.assertEqual(run_solution(n, edges, timeout=10), 99_998)

    def test_large_unreachable_graph(self):
        n = 100_000
        edges = [(city, city + 1, 1) for city in range(1, 50_000)]
        self.assertEqual(run_solution(n, edges, timeout=10), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
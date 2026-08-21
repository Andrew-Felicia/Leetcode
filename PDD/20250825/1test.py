import random
import subprocess
import sys

SOLUTION_FILE = "1.py"


def run_solution(test_input, timeout=3):
    result = subprocess.run(
        [sys.executable, SOLUTION_FILE],
        input=test_input,
        text=True,
        capture_output=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return result.stdout.strip()


def check(test_input, expected, timeout=3):
    actual = run_solution(test_input, timeout)
    expected = str(expected).strip()
    if actual != expected:
        raise AssertionError(
            f"input:\n{test_input}\nexpected: {expected!r}\nactual: {actual!r}"
        )


from itertools import combinations


def oracle(n, bonus, edges):
    best = -10**30
    for mask in range(1 << (n-1)):
        kept = sum(edges[i][2] for i in range(n-1) if mask >> i & 1)
        components = n - mask.bit_count()
        best = max(best, kept + bonus[components-1])
    return best


random.seed(7)
cases = []
expected = []
for n in range(1, 9):
    for _ in range(25):
        bonus = [random.randint(-20, 30) for _ in range(n)]
        edges = [(random.randint(1, i), i+1, random.randint(-10, 20)) for i in range(1, n)]
        cases.append((n, bonus, edges))
        expected.append(str(oracle(n, bonus, edges)))
text = str(len(cases)) + "\n"
for n, bonus, edges in cases:
    text += str(n) + "\n" + " ".join(map(str, bonus)) + "\n"
    text += "".join(f"{u} {v} {w}\n" for u, v, w in edges)
check(text, "\n".join(expected), timeout=8)
print("all tree-cut tests passed")

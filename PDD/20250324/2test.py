import random
import subprocess
import sys

SOLUTION_FILE = "2.py"


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


def oracle(a, m, k, d):
    best = -10**30
    n = len(a)
    for removed_count in range(d + 1):
        for removed in combinations(range(n), removed_count):
            removed = set(removed)
            left = [a[i] for i in range(n) if i not in removed]
            left.sort(reverse=True)
            value = sum(left) - (k + 1) * sum(left[:m])
            best = max(best, value)
    return best


check("4\n2 0 3 0\n1 9\n2 2 1 0\n4 7\n3 1 2 1\n9 4 1\n4 9 5 4\n1 2 3 4\n", "10\n-11\n-7\n0")
random.seed(2)
cases = []
expected = []
for _ in range(150):
    n = random.randint(2, 8)
    m = random.randint(0, n)
    d = random.randint(0, n)
    k = random.randint(1, 5)
    a = [random.randint(1, 20) for _ in range(n)]
    cases.append(f"{n} {m} {k} {d}\n" + " ".join(map(str, a)))
    expected.append(str(oracle(a, m, k, d)))
check(str(len(cases)) + "\n" + "\n".join(cases) + "\n", "\n".join(expected))
print("all game tests passed")

import random
import subprocess
import sys

SOLUTION_FILE = "3.py"


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


from itertools import product


def oracle(a):
    upper = max(a) + len(a) + 3
    best = 10**9
    for b in product(*[range(x, upper + 1) for x in a]):
        if any(all(b[i] < b[i+1] for i in range(p)) and
               all(b[i] > b[i+1] for i in range(p, len(b)-1))
               for p in range(1, len(b)-1)):
            best = min(best, sum(y-x for x, y in zip(a, b)))
    return best


fixed = [[2, 2, 2], [1, 2, 1], [3, 1, 3], [5, 4, 3, 2, 1], [1, 1, 1, 1]]
for a in fixed:
    check(f"{len(a)}\n" + " ".join(map(str, a)) + "\n", oracle(a))
random.seed(5)
for _ in range(45):
    n = random.randint(3, 6)
    a = [random.randint(1, 5) for _ in range(n)]
    check(f"{n}\n" + " ".join(map(str, a)) + "\n", oracle(a))
large = [10**8] * 100000
check("100000\n" + " ".join(map(str, large)) + "\n", 2_499_950_001, timeout=6)
print("all mountain tests passed")

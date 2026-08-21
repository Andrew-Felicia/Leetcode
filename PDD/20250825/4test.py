import random
import subprocess
import sys

SOLUTION_FILE = "4.py"


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


def oracle(s):
    z = s.count("0"); o = len(s)-z
    return min(len(s), 2*min(z,o) + (z != o))


fixed = ["0", "1", "00", "01", "10010", "0"*50, "01"*50, "0"*40+"1"*60]
for s in fixed:
    check(f"{len(s)}\n{s}\n", oracle(s))
random.seed(10)
for _ in range(300):
    s = "".join(random.choice("01") for _ in range(random.randint(1, 1000)))
    check(f"{len(s)}\n{s}\n", oracle(s))
print("all alternating-string tests passed")

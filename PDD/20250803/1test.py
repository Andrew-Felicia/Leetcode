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


def oracle(n):
    n += 1
    while len(set(str(n))) != len(str(n)):
        n += 1
    return n


values = [0, 1, 8, 9, 10, 11, 98, 99, 101, 987, 1881, 2211, 98765, 999999]
values += [random.randint(0, 1_000_000) for _ in range(500)]
check(str(len(values)) + "\n" + "\n".join(map(str, values)) + "\n",
      "\n".join(str(oracle(x)) for x in values), timeout=8)
print("all password tests passed")

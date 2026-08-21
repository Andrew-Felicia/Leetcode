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


def oracle(a):
    evens = sum(x % 2 == 0 for x in a)
    if evens < len(a): return evens
    def twos(x):
        c = 0
        while x % 2 == 0: x //= 2; c += 1
        return c
    return len(a)-1 + min(map(twos, a))


cases = [[1], [2], [8], [1, 3, 5], [1, 2, 4], [12, 8, 20], [2**60]*20]
random.seed(8)
cases += [[random.randint(1, 10**9) for _ in range(random.randint(1, 50))]
          for _ in range(400)]
text = str(len(cases)) + "\n" + "".join(
    f"{len(a)}\n" + " ".join(map(str, a)) + "\n" for a in cases)
check(text, "\n".join(str(oracle(a)) for a in cases))
print("all odd-array tests passed")

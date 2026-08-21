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


from functools import lru_cache


def palindromes(s):
    return [(i, j) for i in range(len(s)) for j in range(i, len(s))
            if s[i:j+1] == s[i:j+1][::-1]]


@lru_cache(None)
def oracle(s):
    if not s:
        return 0
    return 1 + min(oracle(s[:i] + s[j+1:]) for i, j in palindromes(s))


fixed = ["a", "aa", "ab", "aba", "abba", "abc", "abca", "aabb", "abacaba"]
check(str(len(fixed)) + "\n" + "\n".join(fixed) + "\n",
      "\n".join(str(oracle(s)) for s in fixed))
random.seed(3)
strings = ["".join(random.choice("abc") for _ in range(random.randint(1, 9)))
           for _ in range(120)]
check(str(len(strings)) + "\n" + "\n".join(strings) + "\n",
      "\n".join(str(oracle(s)) for s in strings), timeout=8)
unique = "".join(chr(0x1000 + i) for i in range(500))
check("1\n" + unique + "\n", 500, timeout=8)
print("all palindrome-deletion tests passed")

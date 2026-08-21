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


def oracle(points):
    n = len(points)
    reach = [[False] * n for _ in range(n)]
    for i, (x, y, r) in enumerate(points):
        reach[i][i] = True
        for j, (xx, yy, _) in enumerate(points):
            reach[i][j] |= (x-xx)**2 + (y-yy)**2 <= r*r
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][k] and reach[k][j]
    return max(map(sum, reach))


cases = [[(0, 0, 1), (2, 0, 1)],
         [(0, 0, 1), (0, 1, 1), (3, 0, 1)],
         [(0, 0, 4), (2, 0, 1), (3, 0, 1), (5, 0, 1)]]
random.seed(4)
for _ in range(120):
    n = random.randint(1, 8)
    cases.append([(random.randint(0, 8), random.randint(0, 8), random.randint(1, 6))
                  for _ in range(n)])
text = str(len(cases)) + "\n"
for case in cases:
    text += str(len(case)) + "\n" + "".join("%d %d %d\n" % p for p in case)
check(text, "\n".join(str(oracle(c)) for c in cases), timeout=8)
print("all activation tests passed")

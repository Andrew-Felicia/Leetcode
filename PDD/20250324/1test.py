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


def oracle(n, edges):
    reach = [[False] * n for _ in range(n)]
    for u, v in edges:
        reach[u][v] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] |= reach[k][j]
    return sum(all(u == v or reach[u][v] or reach[v][u] for v in range(n)) for u in range(n))


check("2 1\n1 2\n", 2)
check("4 0\n", 0)
check("4 3\n1 2\n1 3\n2 4\n", 1)
check("7 7\n1 2\n2 3\n3 4\n4 7\n2 5\n5 4\n6 4\n", 2)

random.seed(1)
for n in range(2, 10):
    for _ in range(40):
        order = list(range(n))
        random.shuffle(order)
        pos = {u: i for i, u in enumerate(order)}
        edges = [(u, v) for u in range(n) for v in range(n)
                 if pos[u] < pos[v] and random.random() < 0.25]
        text = f"{n} {len(edges)}\n" + "".join(f"{u+1} {v+1}\n" for u, v in edges)
        check(text, oracle(n, edges))

print("all super-node tests passed")

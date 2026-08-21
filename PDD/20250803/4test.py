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


import heapq


def oracle(n, a, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = [10**30] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]: continue
        for v, w in graph[u]:
            if w <= d + a[u] and max(d, w) < dist[v]:
                dist[v] = max(d, w)
                heapq.heappush(heap, (dist[v], v))
    return -1 if dist[n] == 10**30 else dist[n]


check("5 6\n2 5 2 0 1\n1 2 1\n2 5 5\n1 3 2\n3 4 4\n1 4 3\n4 5 3\n", 4)
random.seed(6)
for _ in range(120):
    n = random.randint(2, 10)
    a = [0] + [random.randint(0, 8) for _ in range(n)]
    edges = [(u, v, random.randint(0, 12)) for u in range(1, n)
             for v in range(u+1, n+1) if random.random() < .25]
    text = f"{n} {len(edges)}\n" + " ".join(map(str, a[1:])) + "\n"
    text += "".join(f"{u} {v} {w}\n" for u, v, w in edges)
    check(text, oracle(n, a, edges))
print("all package-route tests passed")

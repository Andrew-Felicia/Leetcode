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


from collections import deque


def oracle(a, x):
    start = (tuple(a), x)
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        (arr, held), distance = queue.popleft()
        if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
            return distance
        for i, value in enumerate(arr):
            if value < held:
                changed = list(arr)
                changed[i], new_held = held, value
                state = (tuple(changed), new_held)
                if state not in seen:
                    seen.add(state)
                    queue.append((state, distance + 1))
    return -1


cases = [(5, [2,1,3,2,4]), (3, [1,3,2]), (1, [5,4,3]), (9, [1])]
random.seed(9)
for _ in range(150):
    cases.append((random.randint(1, 6), [random.randint(1, 6)
                                        for _ in range(random.randint(1, 7))]))
for x, a in cases:
    text = f"{len(a)} {x}\n" + " ".join(map(str, a)) + "\n"
    check(text, oracle(a, x))
large = list(range(1, 2_000_001))
check(f"{len(large)} 2000000001\n" + " ".join(map(str, large)) + "\n", 0, timeout=8)
print("all gift-swap tests passed")

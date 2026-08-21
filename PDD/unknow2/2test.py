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
def oracle(c, x):
    costs=[v*(len(c)-i) for i,v in enumerate(c)]
    return max(r for r in range(len(c)+1)
               if any(sum(costs[i] for i in chosen)<=x
                      for chosen in combinations(range(len(c)),r)))

check("3 8\n2 2 2\n", 2)
random.seed(12)
for _ in range(200):
    n=random.randint(1,10); x=random.randint(1,200); c=[random.randint(1,20) for _ in range(n)]
    check(f"{n} {x}\n"+" ".join(map(str,c))+"\n", oracle(c,x))
check("200000 1000000000000000000\n"+"300 "*200000+"\n", 200000, timeout=6)
print("all animal tests passed")

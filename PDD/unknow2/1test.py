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


MOD = 998244353
def oracle(a, m):
    return sum((a[i]+a[j]) % m == 0 for i in range(len(a))
               for j in range(i+1, len(a))) % MOD

fixed = [(2, [1,3]), (1, [1,2,3,4]), (5, [5,10,15]), (2, [1,1,1,1])]
for m, a in fixed:
    check(f"{len(a)} {m}\n" + " ".join(map(str,a)) + "\n", oracle(a,m))
random.seed(11)
for _ in range(250):
    m=random.randint(1,30); a=[random.randint(1,10**9) for _ in range(random.randint(1,80))]
    check(f"{len(a)} {m}\n"+" ".join(map(str,a))+"\n", oracle(a,m))
check("200000 1\n" + "1 "*200000 + "\n", (200000*199999//2)%MOD, timeout=6)
print("all divisible-pair tests passed")

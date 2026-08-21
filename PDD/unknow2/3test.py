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


def oracle(s,d,t):
    return min(max(d[i:j+1]) for i in range(len(s)) for j in range(i,len(s))
               if sum(s[i:j+1])>=t)

random.seed(13)
for _ in range(250):
    n=random.randint(1,20); s=[random.randint(1,20) for _ in range(n)]
    d=[random.randint(1,30) for _ in range(n)]; t=random.randint(1,sum(s))
    text=f"{n} {t}\n"+"".join(f"{x} {y}\n" for x,y in zip(s,d))
    check(text,oracle(s,d,t))
n=100000;s=[10**18]*n;d=list(range(1,n+1))
check(f"{n} {10**18}\n"+"".join(f"{x} {y}\n" for x,y in zip(s,d)),1,timeout=6)
print("all difficulty tests passed")

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


def oracle(a,m):
    # DP over boundaries: each final segment must contain no target-sum subarray.
    n=len(a); dp=[10**9]*(n+1);dp[0]=0
    for end in range(1,n+1):
        for start in range(end):
            ok=all(sum(a[i:j])!=m for i in range(start,end) for j in range(i+1,end+1))
            if ok: dp[end]=min(dp[end],dp[start]+(start>0))
    return dp[n]

check("4 -1\n3 -3 2 3\n",1)
random.seed(14)
for _ in range(300):
    n=random.randint(1,10);m=random.randint(-5,5)
    a=[]
    while len(a)<n:
        x=random.randint(-5,5)
        if x!=m:a.append(x)
    check(f"{n} {m}\n"+" ".join(map(str,a))+"\n",oracle(a,m))
print("all tree-insertion tests passed")

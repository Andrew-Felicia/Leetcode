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


def oracle(a,b,k):
    c=[[a[i]=='a' and b[j]=='a' for j in range(len(b))] for i in range(len(a))]
    ans=0
    for r1 in range(len(a)):
      for r2 in range(r1,len(a)):
       for c1 in range(len(b)):
        for c2 in range(c1,len(b)):
         if (r2-r1+1)*(c2-c1+1)==k and all(c[i][j] for i in range(r1,r2+1) for j in range(c1,c2+1)):ans+=1
    return ans

random.seed(16)
for _ in range(250):
    n=random.randint(1,7);m=random.randint(1,7);k=random.randint(1,n*m)
    a=''.join(random.choice('ab') for _ in range(n));b=''.join(random.choice('ab') for _ in range(m))
    check(f"{n} {m} {k}\n{a}\n{b}\n",oracle(a,b,k))
check("1000000 1000000 1\n"+"a"*1000000+"\n"+"a"*1000000+"\n",10**12,timeout=8)
print("all rectangle tests passed")

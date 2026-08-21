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


import heapq
def oracle(a):
 n=len(a)-1;d=[10**9]*(n+1);d[1]=0;h=[(0,1)]
 while h:
  x,u=heapq.heappop(h)
  if x!=d[u]:continue
  for v,w in ((a[u],0),(u-1,1),(u+1,1)):
   if 1<=v<=n and x+w<d[v]:d[v]=x+w;heapq.heappush(h,(x+w,v))
 return d[1:]

random.seed(17)
for n in range(1,60):
 for _ in range(8):
  a=[0]+[random.randint(1,n) for _ in range(n)]
  check(f"{n}\n"+" ".join(map(str,a[1:]))+"\n"," ".join(map(str,oracle(a))))
check("3\n1 2 3\n","0 1 2")
print("all teleporter tests passed")

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


from itertools import combinations
def oracle(parent,k):
 n=len(parent)
 for d in range(n):
  for r in range(k+1):
   for centers in combinations(range(n),r):
    ok=True
    for u in range(n):
     x=u;found=False
     for _ in range(d+1):
      if x in centers:found=True;break
      x=parent[x]
     if not found:ok=False;break
    if ok:return d

random.seed(22);cases=[]
for n in range(1,11):
 for _ in range(25):
  parent=[0]+[random.randrange(i) for i in range(1,n)];k=random.randint(1,n)
  cases.append((parent,k))
text=str(len(cases))+"\n";expected=[]
for p,k in cases:
 text+=f"{len(p)} {k}\n"+(" ".join(str(x+1) for x in p[1:])+"\n" if len(p)>1 else "\n")
 expected.append(str(oracle(p,k)))
check(text,"\n".join(expected),timeout=12)
print("all tree-cover tests passed")

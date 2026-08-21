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


from itertools import product
def oracle(tasks,m,t):
 best=0
 for choices in product(range(3),repeat=len(tasks)):
  x=y=count=0
  for choice,(a,b,c,d) in zip(choices,tasks):
   if choice==1:x+=a;y+=b;count+=1
   if choice==2:x+=c;y+=d;count+=1
  if x<=m and y<=t:best=max(best,count)
 return best

random.seed(20)
for _ in range(180):
 n=random.randint(1,8);m=random.randint(1,15);t=random.randint(1,15);tasks=[]
 for _ in range(n):
  c=random.randint(1,5);a=random.randint(c+1,8);b=random.randint(1,5);d=random.randint(b+1,8)
  tasks.append((a,b,c,d))
 text=f"{n} {m} {t}\n"+"".join("%d %d %d %d\n"%x for x in tasks)
 check(text,oracle(tasks,m,t))
print("all task-knapsack tests passed")

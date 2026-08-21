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


def oracle(intervals,slots):
 match=[-1]*len(slots)
 def augment(i,seen):
  for j,s in enumerate(slots):
   if j not in seen and intervals[i][0]<=s<=intervals[i][1]:
    seen.add(j)
    if match[j]<0 or augment(match[j],seen):match[j]=i;return True
  return False
 return sum(augment(i,set()) for i in range(len(intervals)))

random.seed(19);cases=[]
for _ in range(250):
 n=random.randint(1,7);m=random.randint(1,7)
 ints=[]
 for _ in range(n):l=random.randint(0,10);ints.append((l,random.randint(l,12)))
 cases.append((ints,[random.randint(0,12) for _ in range(m)]))
text=str(len(cases))+"\n";expected=[]
for ints,slots in cases:
 text+=f"{len(ints)} {len(slots)}\n"+"".join(f"{l} {r}\n" for l,r in ints)+" ".join(map(str,slots))+"\n"
 expected.append(str(oracle(ints,slots)))
check(text,"\n".join(expected),timeout=8)
print("all matching tests passed")
